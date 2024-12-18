This app demonstrates:

1. Using all parameters of `input_dark_mode`:
   - `id`: To track the dark mode state
   - `mode`: Set to None to use system settings initially
   - Additional styling parameters through kwargs (class_ and style)

2. Features:
   - Reactive dark/light mode switching
   - Dynamic plot styling based on dark mode
   - Visual feedback showing current mode
   - Different chart types that adapt to dark/light mode
   - Informative cards with mode-specific styling
   - Font Awesome icons that change based on mode

3. Installation requirements:
```bash
pip install shiny matplotlib numpy
```

4. Key technical aspects:
   - Uses express mode for simpler syntax
   - Demonstrates reactive rendering based on dark mode changes
   - Shows proper handling of matplotlib plots in dark/light modes
   - Uses cards and layout components for organized UI
   - Includes Font Awesome icons for enhanced visual feedback

The app provides a complete demonstration of dark mode functionality while maintaining good UI/UX practices and proper reactive programming patterns.
## Preview the app on [Shinylive](https://shinylive.io/py/app/#h=0&code=NobwRAdghgtgpmAXAAjFADugdOgnmAGlQGMB7CAFzkqVQDMAnUmZAZwAsBLCXZTmdKQYVkDOFGIVOANzgAdCI2ZsuPLHAAe6Ma1Z8BQkd3QBXCkROciYiABM4DBQoDEyAApQA5nGSl0U8j06IWQKdh8MdAVLHC84AH0-ClYACgVkDNDOCgAbOABeOTAAESgGAGtkAFlSe2RiuBhSIoJ0zLpOHJyoACM8-IAVBhM4VohMtk57HrLB4fkIAEonCFcAQVtbZAAxchE1gHc4VmYfAGEAZQvQ0mQTVh9OMghWaM4scKhbeOeqSjTxpkYgAJAZVAAyAImEwA5AAeHLcSpiHKFMCsCi4PIcOBwChFZDsMR0NHsCgUdCsRAAempxFsEAAVqwsMQcqQTLY6N0xKzmNSoIyoBpqYieqxqcFKABaKBHE7wakANiwABYsAAmOm6AVdLAwbis3RFAB8MLaGWWSxWrjOYigVGQUGQtjKlSadVYB2yxHYyG9YSdXWQgl0nD6PnQZVgeIcrwgMWMZniroq8Q9cChmSmaIzLQyrgA8v5OOQoDlkABJYo3UIMCSVVPu2o+DEOhYTDP5ABy5FGBarEGynHLyAzyBSvYgPnuxzYuAxjTYeKkEE8rCtEzZUF08VzPWlAGZ88h1pth2WK5drtvdMcLWxMf0ilKKNLWJwAF5wFAARk1YgwAA3ASp7IGc9wUMoGJYtwngKFaCgBn6MTdLgHIUPEH7TGUKSLIgD7IXc7zYXAMwMHhBGAtCxEfKqaQlG61QtsgFwrnBrxgJuNG0UmmH1rYpbxD0ZhQS8WY8ZkRS+mUmGYug8iEA+klFGxeSSOB7CycgAy4ApLTKTxvqkE8xz5MARTgtwilEEUABCZT5qpxAOlQjhgAAuoZlorBMRGoVA6HJmQOQmDA4n4d5-rZCh7wuQwtiUVFEwxPF3yfPYFFFBBDA2CIpQVMxdQXBQDr3EU3GSRkAACNiZVgVAaPi1FVfYdAum66YtlhpUUPcSUtVVmRtn1ej5MgRQFeUBKcO1fH6i2eHIPk41FE2BJwDkDwTWAVmeGSRTJTxYh9Qw4x0NlJi5dQIgZigIAjfcAC+h2DTxUX+XFZSJZFb00al33xBlDgMRcsDoHkmmyRVR01XVDg4OyzVDRkbVsODeTxBDpAUANKPQvwgjCGODrY7k4Y4HpSNOnoEPI-j2YGMTCYCLwO7IBAUR-VVsPQq4ADi1AOO26MCJDrqlbzEwaMtHPYIiLxRsQmYAAxEL+avIBrKuVQzvDjZzWAfhAKQaLr+NS+0nCeEQwqy3TRsmD0ZOpObKOWwObEiCFQh6DMDxbOQHWFXm3OST7DDxHQniy0UfQNjNc2c2YC32EtK07Yi+34mAyCbdtRQHFwVCvQzmQR8JMerWARfZIpfBJ6YFCp5mizLdXWcHbn+c+EUziHgPg+l2XE1hzxtr2o6ZPIP7cCB+MDzqVQWzyR2I+zXwyfNzJwjxKv6fV1Z05FFRI-QsKiM46bRC4EQEf5BX0du0Nm0b-NO9yXprftztDnuafZ9MgX3IqbYAiBEAaw8jfMBECVZQOQPfR+nhn5VR7igMCFwXLkgcB7c+GgjZYLctfZAt8EGkHZAwB+5ChBR2Qbg3BrgSpYh8GESM1NZ7z2Ds2ewuCL4PEwnQCQcAI4pArj0OhY8aIdE8LECgvojZ4ijkIkRYiJFnwvlIYg5QsbRhgKkCOrAqEUNoSgySfD0DWVYMAGEPQcZQRgDCDyCjMIqOoZHJ+vD8GsAsdOKxMIoLoEcc4n4bjRFuJMZ4o2PjjjWLyHQCgQT+EhIoWE4xHjJF4KiZY6xDBrZkkSYo1xaS1Ej1wQ7KQuRMyqQxj4AAapwVgJhyxfgdKWCA+ZEHhPSWfB2Ghug9E2gxAAGk6DQDSOluKMTQ7pI8HZYl6IMooABNUZ4zCBkIoVM9xJSy64JOldc61tfI8U+qyb6eMUYAwSkDcQmUGJTSKj4SsighAwFaeQGGGTarUHqpYXmaMMzxG4MEC5ZdiBXTyl1Oo415oZjwrgje4LrqUChT4DOa03Qn1wRMJ4QdxoxFKuuLAnBRHdF3GiQR75yFTGQJSpoHz1kwWfGACOKBnB0DoLYAA7CrFWIEuLYsyI1EQ1cHnjgaQgiFN0chs0kDIOAWAdJcD0OEHIlJRBzxMMrPOuBWwUHrNwTeyB2QHGlJ3b25BBIBBeFgYeZc0GCoyLi8Y+L3iEpZCS28rA9wvigFSxEWxKWNPaYyp8BRpJuLZRygAHMQXl-LTEo2FbHXaeTbosQlUivKMqnRytkIqgYyqQxMGkFMOcXB9pkMoPWDERqjhdDNdkPOEBS1MAgPASgLI7UMz2XiA5tFBLSAkoAglXgWTsHos62yucah1AaKVTonFFhjEAUCd46AUjCuXY6x8zC0RRnPGuP8Kt0AaH5bgxYYAnpEHANAeAtAwBiAAI6WEAjdFkFAmrrJZXsG6D6FBvIpEjMUCgWZ4AUFGOwO5jlDSvR5IAA)