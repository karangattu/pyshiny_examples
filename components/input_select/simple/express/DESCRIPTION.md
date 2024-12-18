This app demonstrates several key aspects of `input_select`:

1. Basic Usage:
   - First `input_select` uses a dictionary mapping city names to themselves
   - Second `input_select` uses a nested dictionary to create optgroups

2. Reactive Interactions:
   - The `city_details` function reactively updates based on user selections
   - Uses `input.selected_city()` and `input.data_view()` to determine output

3. Synthetic Data:
   - Created a pandas DataFrame with city information
   - No external files used for data

4. UI Layout:
   - Uses `layout_sidebar()` for clean organization
   - Sidebar contains selection inputs
   - Main area shows dynamic text output

Key Points from Function Reference:
- Used dictionary mapping for choices
- Demonstrated nested dictionary for optgroups
- Showed how to create dynamic, interactive selections

When you run this app, users can:
- Select a city from the dropdown
- Choose what type of information to view (population, area, income)
- See real-time updates based on their selections

Recommended Improvements:
- Add error handling
- Include more complex data views
- Add visualizations

Would you like me to elaborate on any part of the implementation?
## Preview the app on [Shinylive](https://shinylive.io/py/app/#h=0&code=NobwRAdghgtgpmAXAAjFADugdOgnmAGlQGMB7CAFzkqVQEsZ1SAnC5dKCAEygGdk+7LgB0IDJq2QQAro1wD+EdKNEAzZqRjJeACzoR54lm2ZwoxCnQBucNRq279uLHAAe6U735HJ+9NIoiU244ZiJpOhUIAGJkAGFTKCptXEodOEtiZB4KPgzRJSxmTi5NLF44OC4ACgAWACYASlFiOks4fgBeZGAAcgA5OAB3ZABNFgBrXqJegBlSfgBBCABzOAAbDunkXri9YigV0m3egAlSaV4KchOABR1SajpXXoBdURyoZG70LiwAESSUAAYsV4NUQKJkNCdq0KLheig4XQOgQoTDekx-OsknQbihgAAOAD6tQADGTiRSyUQAMzEgCcFKpFKI9WJAHZmdS2cTadzWcgAIzEgBsArJrzREBhOygiWJvAAjsSYHRNrxET1+fUsKKiABWMm6jls+ocvVEUW0i0Gw1Ci0MqXo6G9KBWFbE-RkeBa4CijlU2r65AGhnEwm02mGkn1Wqm0PsqOEw21YkGg21d4QAC+zQgolii0wyAAqgBJUQRHCHODE0joCi8aqWCibTrCMBxNrycsQVQsGC48jIACi7nWLFCnfzoiGbR0yGrONwFwoiroXDgACN5dVGogXch5xRF9XeJud3uD0fZbFSxfVsg-AFFRs4BZjwuBNk6BY8dAzDyKQqjIMQDx-h0t4wtWL7rhUmwWNU0GytCnYIR+VBcMScK4J2RAoahnZ7KQCxwD+3bwoehDIIRsqQjKqFMbKuFIj2yADswYHsfo3HtLwdEwjmhGzoxTFFhApCnqEz5KK+GGfiei4NhQKwaNI6ACWJqGwXJ8HvkhgloWAnzElYKJDPhtHacxtFgAAygZbCArkyAAGoWdRBE2cxDG2bZnYAEJ8H+yB9gOnYoH5-kxZ2WLSDiljkJFdm3A2CXDgWhBGf5nbymYKWdosiSdjlso5tKMVMZ2o5kJJapZOFpApdFVXMZ23qaLYtBFTYxRrGFEA+t1ZVCTlwk+dCol3sgABK1BblxXB0KoqihNQbBrv4TbILuFRcMgI4KUlEBabKAACwSLVgVCuBQR5bqBuHEluuTqs2N6TXx8jdHB5ROVUOE9vuhHmcM3yydtWCmWDQwg19hHPZ8EOfMAqO9LhbzfN0uHZgFX0rcgsPYzs8WJQBiI5aYFDSMwMqqJ2IC4TmyBpdimVRUjQJ9GTmVvFgVhQOs0gdMAkqIAQwlgIRGyE8TnTdG6iSU19srU7T9OM8zyDFWYnM9i93NK2YioqmqGr84Lwui5KLPKsg5tQdLX2y6B8uK51vqHqrMLq3THFaz2LOLH1taDcNKAACRMwb6Pup6ntwJbQsi7wYuvBLUtgBVyDgNA8C0GAphKhEpjwJQvA3XdNFgHVVA0CgztDhQ6CTm2dDbgUsh4KIHDcHwURtdnrxAA)
