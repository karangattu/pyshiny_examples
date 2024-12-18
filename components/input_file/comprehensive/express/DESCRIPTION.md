This app demonstrates:

1. All parameters of `input_file`:
   - `id`: Unique identifier for each file input
   - `label`: Display label
   - `multiple`: Boolean to allow multiple file selection
   - `accept`: List of accepted file types
   - `width`: CSS width of the input
   - `button_label`: Custom label for the browse button
   - `placeholder`: Text shown when no file is selected
   - `capture`: Camera capture mode (user-facing camera)

2. Different use cases:
   - Basic single file upload
   - Multiple file upload with various file types
   - Camera capture for photos
   - Custom width file input

3. Display of file information:
   - Shows file name, size, and type for uploaded files
   - Handles both single and multiple file uploads
   - Uses DataFrames to display information in a structured format

4. Layout:
   - Uses card layout for organization
   - Responsive column layout
   - Clear headers and sections

To run this app:

1. Save it as `app.py`
2. Install required packages:
```bash
pip install shiny pandas
```
3. Run with:
```bash
shiny run app.py
```

The app will create a user interface with four different file upload sections, each demonstrating different parameters and capabilities of the `input_file` component. When files are uploaded, their information will be displayed in corresponding data tables below the upload sections.
## Preview the app on [Shinylive](https://shinylive.io/py/app/#h=0&code=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)
