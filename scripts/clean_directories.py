import os
from pathlib import Path

def clean_app_directories(root_directory):
    """
    Clean up directories containing app.py, app-express.py, or app-core.py files.
    Keep only the app file, PROMPT.md, and test_*.py files.
    
    Args:
        root_directory: Path to the root directory to start cleaning from
    """
    root_path = Path(root_directory)
    
    # Count statistics
    stats = {
        "dirs_processed": 0,
        "dirs_cleaned": 0,
        "files_deleted": 0,
        "files_kept": 0
    }
    
    print(f"Starting cleanup from: {root_path}")
    
    # Walk through all subdirectories
    for dirpath, dirnames, filenames in os.walk(root_path):
        current_dir = Path(dirpath)
        stats["dirs_processed"] += 1
        
        # Check if directory contains any app*.py file
        has_app_file = any(
            filename in ["app.py", "app-express.py", "app-core.py"] 
            for filename in filenames
        )
        
        if has_app_file:
            app_files = [f for f in filenames if f in ["app.py", "app-express.py", "app-core.py"]]
            stats["dirs_cleaned"] += 1
            print(f"\nCleaning directory: {current_dir}")
            
            # Process each file
            for filename in filenames:
                file_path = current_dir / filename
                
                # Determine if we should keep this file
                keep_file = (
                    filename in app_files or  # App file
                    filename == "PROMPT.md" or  # PROMPT.md
                    filename.startswith("test_") and filename.endswith(".py")  # test_*.py
                )
                
                if keep_file:
                    print(f"  Keeping: {filename}")
                    stats["files_kept"] += 1
                else:
                    try:
                        os.remove(file_path)
                        print(f"  Deleted: {filename}")
                        stats["files_deleted"] += 1
                    except Exception as e:
                        print(f"  Error deleting {filename}: {e}")
    
    # Print summary
    print("\n" + "="*50)
    print("Cleanup Summary:")
    print(f"Directories processed: {stats['dirs_processed']}")
    print(f"Directories cleaned: {stats['dirs_cleaned']}")
    print(f"Files kept: {stats['files_kept']}")
    print(f"Files deleted: {stats['files_deleted']}")
    print("="*50)


def delete_specific_files(root_directory, files_to_delete=None):
    """
    Delete specific files (like requirements.txt, DESCRIPTION.md) from all subdirectories.
    
    Args:
        root_directory: Path to the root directory to start from
        files_to_delete: List of filenames to delete (default: ['requirements.txt', 'DESCRIPTION.md'])
    """
    if files_to_delete is None:
        files_to_delete = ['requirements.txt', 'DESCRIPTION.md']
    
    root_path = Path(root_directory)
    
    # Count statistics
    stats = {
        "dirs_processed": 0,
        "files_deleted": 0,
        "files_not_found": 0
    }
    
    print(f"Starting deletion of specific files from: {root_path}")
    print(f"Files to delete: {', '.join(files_to_delete)}")
    
    # Walk through all subdirectories
    for dirpath, dirnames, filenames in os.walk(root_path):
        current_dir = Path(dirpath)
        stats["dirs_processed"] += 1
        
        # Check for target files
        for target_file in files_to_delete:
            file_path = current_dir / target_file
            
            if file_path.exists():
                try:
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")
                    stats["files_deleted"] += 1
                except Exception as e:
                    print(f"Error deleting {file_path}: {e}")
    
    # Print summary
    print("\n" + "="*50)
    print("Deletion Summary:")
    print(f"Directories processed: {stats['dirs_processed']}")
    print(f"Files deleted: {stats['files_deleted']}")
    print("="*50)


# Example usage
if __name__ == "__main__":
    # Use the parent directory of the scripts folder as the root directory
    root_dir = Path(__file__).parent.parent
    
    # Choose which function to run based on your needs
    action = input("Select action (1: Clean app directories, 2: Delete specific files, 3: Both): ")
    
    if action == '1' or action == '3':
        clean_app_directories(root_dir)
    
    if action == '2' or action == '3':
        # You can customize the list of files to delete
        custom_files = input("Enter filenames to delete (comma-separated) or press Enter for defaults: ")
        if custom_files.strip():
            files_list = [f.strip() for f in custom_files.split(',')]
            delete_specific_files(root_dir, files_list)
        else:
            delete_specific_files(root_dir)


