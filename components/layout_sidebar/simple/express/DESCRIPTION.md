### Technical Breakdown:

1. **Data Generation**: 
   - Created synthetic data using NumPy and Pandas
   - Generated random integers and floats for demonstration

2. **Layout and Sidebar**:
   - Used `ui.layout_sidebar()` to create a sidebar layout
   - Implemented sidebar with interactive inputs:
     * Slider to control number of categories
     * Radio buttons to switch plot type
     * Checkbox group to select displayed columns

3. **Reactive Rendering**:
   - `@render.plot` for dynamic plot generation
   - `@render.data_frame` for interactive data table
   - Inputs dynamically control plot and table content

4. **Inputs Used**:
   - `input_slider`: Control number of categories
   - `input_radio_buttons`: Switch between bar and scatter plots
   - `input_checkbox_group`: Select columns to display

### Key Shiny for Python Features Demonstrated:
- Express mode syntax
- Reactive programming
- Dynamic plot rendering
- Interactive data exploration
- Sidebar layout

### Running the App
Simply save this script and run it with `shiny run app.py`. The app will launch in your default web browser, allowing interactive exploration of the synthetic dataset.
## Preview the app on [Shinylive](https://shinylive.io/py/app/#h=0&code=NobwRAdghgtgpmAXAAjFADugdOgnmAGlQGMB7CAFzkqVQEsZ1SAnC5CAV0d2SgGd26ADoQGTVsnRQIAE368B6GSLEs2MKBXQAbUhW10ARjlw69CydooiRAM2akYyPgAs6EHqonM4UYhToANzg7BydXd1wsOAAPdB8+AS82d3QOCiIOOiIfWThmGwgAYmQAcWp8zThnXEoXOADiZDkKKBEIbGZpGUcsPjg4GQAKABYAJgBKERaoZABeSRksABFNKAAxLvghkBFkfeQAcgBhKoBzFlxDlGBDgEFDokOAIUej47fD5c+AUUOAXQIewOhwAalBtBw4NdBFgurJevCZO4KEMAIwABiImKxyAArBMgRADkcAMpkHwwjpw7q9DiiWwsGBDXGYogEkQAXymEBEJVJDUkUDO1VI6AC5D4IiyOGFcAA+mKKHwhgF9HA5kIwKSxNpqjqZHBDFBmMgADJQXCkdLIZZwGCkLU8vnIY4+KrOOiG42m7SW63WCAAdzoFBcyBlfqt6XlfC9RpNQwmiGB+358Z9yDIlGogZJIbDEbofQzieTqZJyHT3pNyFS6SlxMr+xl9YosYMhuYQy1nBg8uI5xYdDgUsIyC1ADkuIZ8shSLZXUPmCOx0QK83N5uYO45miiBoYnM9RAhjNCchAhCoXMAMw8rcbg6tjoxrrI0jywzpCiSntgMx2woUwQnHLUAAVdDYAAVECtXXJstyQ5CDmALVnhNeCJ21QcKCoAowEBZw4D1fxBk1MAMIIh9NyfFtizbAd6mIABrQxSBieUzgcDh0H-VxSCDeUr0hUcsK1UkXEE201nExCUIUzdiCkuhiFHOYZiwMhIRgCA+CwX8DD4VELzoxTFP6UiqBkOY0LAU4qAuZhcHEsBwVErV-mdeSSgAWSgdwhQgEis3IKhKArAABXIuxwKCK0NRcNHceVAKTFN5JJEp1joKw5xmZBjX6GR52JPhO3yMzbFy-DBnlAqFk0+ooGGNssD7Adl1XJMaObMydAoLBqrODgfCGYa4wALw1IYAA4iAANgmXrKzMuhFzawD5WA9A4CTeYFnQzCkDMkkBqwH1xpq-I6pmW4HLgJyriI6q8p8GR6rWW53KhAEVq3c61T1f8qOQSDzAXZAfrEsB-s3c6Yj9WdtH-B6nqdU6DnO3AkZI-9oYxzKDhI-oMoU86+Fw-Crre26vpOZdnqIV7ao+u6wWvaEiMx8y+DmFmbrZ+nyRYLmACo8VxCF0BcKA5gxLAlp5yxBqBvaJKpudwbYSHobHOHmwR3GUa1NHLkJ8mrCwHGoGR-HOYt2iif2QG6DOFx2yjAMkzMnwKFG4lzrOYhbB93kfJk1pkFaQw9WQGLKvk6LqFimZ5XsWAQnkxLmjWbbbeB8tnarZAcre3Oo6KwZSucCrTW6YirOr7SuD0qrrvez6o8atYsGa1rX0GjrcMe4dRx632GgD5ABc7u62oEoSRKhFUJn+MBOSIcBoHgWgwB8ABHLIfHgSh9IoGIKHHMBs3Cq+UDAEQNC0KCDEMdouDwEQpFkfhCgUje-wgA)
