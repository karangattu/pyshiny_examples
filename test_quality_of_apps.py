import os
import logging
import socket
import subprocess
import threading
import time
import requests


def find_prompt_files(base_dir):
    # Walk through the directory tree and find prompt files but skip components directory
    for root, dirs, files in os.walk(base_dir):
        if "components" in root:
            continue
        for file in files:
            if file == "PROMPT.md":
                yield root, os.path.join(root, file)


def run_shiny_app(
    script_path,
    port=8000,
    timeout=8,
    success_timeout=5,
    verbose=True,
):
    """Runs a Shiny app in a subprocess and monitors its startup.

    This function launches a Shiny app from a script file, checks if the port is available,
    starts the app process, and monitors its logs for successful startup.

    Args:
        script_path (str): Path to the Shiny app script file to run
        port (int, optional): Port number to run the Shiny app on. Defaults to 8000.
        timeout (int, optional): Maximum time in seconds to wait for app startup. Defaults to 8.
        success_timeout (int, optional): Time in seconds to wait after successful startup. Defaults to 5.
        verbose (bool, optional): Whether to print detailed log messages. Defaults to True.

    Returns:
        tuple: A tuple containing:
            - bool: True if app started successfully, False otherwise
            - str: Status message indicating success or failure reason

    Example:
        >>> success, msg = run_shiny_app("app.py", port=8000)
        >>> if success:
        ...     print("App started successfully")
        ... else:
        ...     print(f"Failed to start app: {msg}")
    """
    if is_port_in_use(port):
        if verbose:
            logging.info(f"Error: Port {port} is already in use.")
        return False, f"Port {port} is already in use."

    process, process_created = start_shiny_app(script_path, port)
    if not process_created:
        if verbose:
            logging.info("Failed to start Shiny app process.")
        return False, "Failed to start Shiny app process."

    return monitor_app_logs(process, timeout, success_timeout, verbose)


def is_port_in_use(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(("localhost", port)) == 0


def start_shiny_app(script_path, port=8000):
    try:
        process = subprocess.Popen(
            ["shiny", "run", script_path, "--port", str(port)],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        return process, True
    except Exception as e:
        logging.info(f"Error starting Shiny app: {e}")
        return None, False


def monitor_app_logs(process, timeout, success_timeout, verbose):
    if not process:
        return False, "No process found"

    stdout_lines = []
    stderr_lines = []
    startup_successful = False
    monitor_active = threading.Event()
    monitor_active.set()

    def read_output(stream, lines_list):
        while monitor_active.is_set():
            try:
                line = stream.readline()
                if line:
                    lines_list.append(line.strip())
                    if verbose:
                        logging.info(f"STREAM: {line.strip()}")
                else:
                    time.sleep(0.1)
            except ValueError:
                break
            except Exception as e:
                if verbose:
                    logging.info(f"Exception in read_output thread: {e}")
                break

    stdout_thread = threading.Thread(
        target=read_output, args=(process.stdout, stdout_lines)
    )
    stderr_thread = threading.Thread(
        target=read_output, args=(process.stderr, stderr_lines)
    )

    stdout_thread.daemon = True
    stderr_thread.daemon = True

    stdout_thread.start()
    stderr_thread.start()

    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            response = requests.get(f"http://localhost:{8000}", timeout=5)
            if response.status_code == 200:
                if verbose:
                    logging.info("Shiny app started successfully within timeout.")
                startup_successful = True

                time.sleep(success_timeout)
                if verbose:
                    logging.info("Terminating app after successful startup...")
                process.terminate()
                process.wait(timeout=2)
                break
        except requests.exceptions.RequestException:
            time.sleep(0.1)

    monitor_active.clear()
    stdout_thread.join()
    stderr_thread.join()

    if process.poll() is None:
        if verbose:
            logging.info("Terminating app after timeout...")
        try:
            process.terminate()
            process.wait(timeout=2)
        except subprocess.TimeoutExpired:
            if verbose:
                logging.info("App did not terminate gracefully, killing...")
            process.kill()
            process.wait()

    if not startup_successful:
        error_message = ""
        for line in stderr_lines:
            error_message += line + "\n"
        if verbose:
            logging.info("Error starting Shiny app:")
            logging.info(error_message)
    else:
        error_message = ""

    if verbose:
        logging.info("\n--- App Termination Summary ---")
        logging.info(f"Exit Code: {process.returncode}")
        logging.info("--- Captured STDOUT ---")
        for line in stdout_lines:
            logging.info(line)
        logging.info("--- Captured STDERR ---")
        for line in stderr_lines:
            logging.info(line)

    return (startup_successful, error_message)


total_apps = 0
total_success = 0
total_error = 0

for directory in os.listdir():
    if os.path.isdir(directory):
        prompt_pairs = list(find_prompt_files(directory))
        if prompt_pairs:
            for dir_path, _ in prompt_pairs:

                total_apps += 1
                success, error_message = run_shiny_app(
                    f"{dir_path}/app.py", port=8000, timeout=5, success_timeout=5
                )
                if success:
                    total_success += 1
                else:
                    print(dir_path)
                    total_error += 1

print(f"Total apps: {total_apps}")
print(f"Success: {total_success}")
print(f"Error: {total_error}")
