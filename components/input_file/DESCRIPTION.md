This app demonstrates all the available parameters of `input_file`:

1. `id`: Unique identifier for the input
2. `label`: Display label for the input
3. `multiple`: Allows selecting multiple files
4. `accept`: Specifies allowed file types:
   - `.csv`, `.txt` for specific extensions
   - `text/plain` for MIME type
   - `application/pdf` for PDF files
   - `image/*` for any image type
5. `button_label`: Custom label for the browse button
6. `placeholder`: Text shown when no file is selected
7. `width`: CSS width of the input
8. `capture`: On mobile devices, this opens the camera (set to "user" for front-facing camera)

The app is minimal and focused on demonstrating the file input functionality:
- When files are selected, it displays their information in a DataGrid
- Shows file name, size, and type
- Includes filtering and row selection capabilities in the grid

This example avoids unnecessary components and external dependencies while showing all `input_file` parameters in action.
## Preview the app on [Shinylive](https://shinylive.io/py/app/#h=0&code=NobwRAdghgtgpmAXAAjFADugdOgnmAGlQGMB7CAFzkqVQEsZ1SAnC5dKCAEygGdk+7LgB0IAM2akYyXgAs6EXMgZNWyZnCjEKdAG5xREqTPmKscAB7oNvfipZsF6AK4UiG7nGZFndQ5Ok5BVwsClx0ODtGB2QAMToAGzgASXFSUVEAYmQAZTg2DgBzOGRSdB1yXlFfHChigH0yil4ACh0KJIBeYTB4pORUlzYAETgYdMJkMUSEqAAjLoAVZmc4AEoMiAB3OgpZZBriKGYuFrXEUWQrg7osI5P62U0uLxaevpKAVXQE0iguZCjcY9DYQa7IS7XbIfZQQIbIHZ7AQJBLsUi2OgLEocZiwfJeKpg641JyuerTJJvIngq50LjdMAUuAARh6BEhNOQszmcASDO+v3+cUSBkIHJpMGcCR0PzgnWWq3Z1JpWmIcHKnWAPTuvF0bIhYFCFgo+p6VGNAHoflAFKa0JgEnQjhUIFauGI7Qw6nALQAqHoAXSVnKuc1cFHI9W5vIZAGFZKR0SUPrwsGm2eLwda1QmEi9mAyALJSmX9Jn8I5gnkyXlwbRwERi5XgnZcPYMgAsAAYu+gLBnm9cjuVnBoGc5eF4euLQeKAAIaLQ6fR3KAJYjil5idjHSfkkWtc6Z67llCO3gUYAfVJiUgB5AAH2QADlyCVOrChlgmcyzsfaduECkGwp7-jSGgUKOYLoFwWDDFAFBQLEuLwH+g5XGB2SxouVACICCFIShJSIvsTKwrezAwAhdDkGBTL1Aot7IB+wABnRLBTCKsKcUkvAXOhNL0YxpBYBgETcC0IBgSGBrPniPQoEyWqQPJYBBtJIY9DkdAAF4lC0cy4FQvAbLQSk9LwumiupAkyT0izhKKikispYQRIGGlXAAvqCMkQVBQhwQRyF4i0QlpLOyoLtQ+ZYDwiHkkRm5wNu9GIViZz8TJ7rMTuzB7uWaEyXQ27uuYjBhFlMnXP5zBgh4sXwYhADizB0lS1UhjBQWISFqFkAkzgwBAvCaj0cnwHa2l6cgBlGZEplEPZjmBmswadTSTx0IUsgUAyADMPZ9gOG00q27Y9MyPYAKQnadJ6JFQ+XyiscDrfdNZJNoNEQPU4wvAykhbNOtnXL5Ia1fVMVeD1UCte1nnIO673VVtO17T0h29v2TanedsgMldXa3bjG0Uk9o0Km9iOTl9Lp-aQAM9EDIMyZF4LZAAglwAK8FIJQKBeKzfZU4okTcq4nJlYE1FRzAANZcKQWwQG8YDTurAmZNrAwjRQwsunxYHMlgyCxo6xDy8gADk8aJpOwq8WmWDW8gEafXWbBvqUzDIOMGg8ZEYEAEymzkziYA4DaB27jl8WbOQAGpEIsAAaixEAACsMsREJwAJesUhIyftpswsJlHUeQCIzAImCaL7Chu08bvzP0PK-MDAkdqbnwO+TBJu6QNbHMQ+x7JIzg7QcPx-C8ALlmBGsgmAXkBkAA)
