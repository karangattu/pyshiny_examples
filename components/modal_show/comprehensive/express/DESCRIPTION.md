This app demonstrates all the parameters of modal_show:

1. `modal`: The modal object to show, created with different configurations:
   - Different sizes ('s', 'm', 'l')
   - With and without fade animations
   - With and without easy_close functionality
   - Various footer configurations
   - Different content types (text, tables, icons)

2. `session`: The session parameter is handled implicitly by Shiny Express mode

Key features of the app:

1. Uses Shiny Express mode for cleaner syntax
2. Demonstrates all modal parameters:
   - size
   - easy_close
   - fade
   - footer
   - title
   - content variations

3. Includes:
   - Font Awesome icons for visual appeal
   - Sample data using pandas
   - Different modal closing behaviors
   - Custom styling for buttons and content
   - Responsive layout with sidebar

4. Shows various modal use cases:
   - Data display
   - Confirmation dialogs
   - Success messages
   - Custom interactions

To run this app:

1. Install required packages:
```bash
pip install shiny pandas numpy
```

2. Save the code in a file (e.g., `app.py`)

3. Run with:
```bash
shiny run app.py
```

The app provides a comprehensive demonstration of modal_show's capabilities while maintaining clean, organized code structure in Shiny Express mode.
## Preview the app on [Shinylive](https://shinylive.io/py/app/#h=0&code=NobwRAdghgtgpmAXAAjFADugdOgnmAGlQGMB7CAFzkqVQDMAnUmZAZwAsBLCXZTmdKQYVkDOFGIVOANzgAdCI2ZsuPLHAAe6Ma1Z8BQkd3QBXCkROciYiABM4DBf0HDk6KHah6vb204OuECYCvD4Q6AoKAMTIAMqw6AA2cMi2UBRQCrZ0yAC8vlgAIulQAGIMsHAAFCAKyPXIAORpVI0o6LZYLXAA+hUQAObVrBnCuY0ATAAMEwAsALRTAIyLS41E6A6cpLasuUtTAJQEdQ2N0lCJJnBtyOFY-bbMDx62EFUHx6f1jcTpcAMhLhbvdHs9iOxSJxiNVgI0AILrJoAISRjQAwo0ALpET4KAC+h0iQU4OCgQx6pHQFFYVSkFGSuTkYAAsjtLshCnAYKRmUQ6JxEokoAAjRkAFQY1yJEGiyHhtlsyFK5BE8IA7nBWMwUnQhHwyBBWApLFh2OJbD1DVRKFVvshTQAJcUsgAyVUaAB5EtwANaiOCJJlgEa4ZIcOBwCjM5DsMR0YPsCgUdCsRAAenTxDeACtWFhiIlSCZssKxAXmOmoDmoBp0z6Rax03rKPMoJrtfB0wA2LBTPtZ3RVoVYGDcAu6ZkAPkaMplCnVnAo7AdpOFuGLFB6rE49hFUAYVUOiHti+Xq6wO73B6PJ4gDQfF+MZh6Eik5B6IrMFHIdpDkPVbdnGSPlkGZWIALiYCUjZNJElAwsvFYHpgxgEV5gAZmZGVHwaU1ny3N9tggT9v1-ZkOFIQCyyGUDwMg10DyGZBYMuBDhV0FDmTQzDsPtB98PCF8iI-L9k3I-8qO3GBLngwgwLACCqLiGShRY9k5KIRDONQ9CsLAHDcKfITCMkYjSPE94KIAno9VIKhHHk+jlNYxJkDPFcVXshx2KQriwB4-TDNwwTTFM98SLEn8rMkwCIFIWyoHsOjFMg1z3KXSEzGVJL5Hk7TkN03iDP4vDSQI18zNEsiYsowDxFYXArSLVg8qIZz1WQABRLxeHRFqYI03ydO4vS+NlCAAAExCI2R1DoOg4EkBRpvEMy5rgWRbQIy8bJ3ARkhlewcjqoCDt6Hk4Nve0WHyU1LsuO17yM5lxS4PROG8ZB9x3YhkAetyPNSOA6CgExEhEVrk24AZjUIUr6npRlwOg9S4L5BHkAaprC1IVrclKS5WpOZ7cLshzcgAOXIeRSeQYKLwB7cAKqGB5ymmb1rgebFuWjm1qkDatooKodtOmi4COkGVCkiWegB666duxmNKeoyL03MKegyMVqmZOWdZAgySfVpG4GDRiGGY9KgeKDIMbph8dwAL3NxpEnWTHseavHzcJxJicx8mHFye6NIs6K-3633xofBmw7g5mqNZ9nVtm7mQd56N+fT9RhdFkzdqk1hVMSKWTr20v5dV48bryFWrsx00MlhrBOCqAr-NB+ZtR9JVu4hJb-W72YNGQKgNAoHuTGIGFJ2NpvSRb-N2FmP8AHlNgqCK4hnufWDocGAEJhsK7ip6Ck2jLN4NYlLtG2Phx2Ghdt3WE95-6m93H8f9wPP+QMHBgodSRMyihJdeABpWODR46gPDnVFOxI05cx5ktbOKDBYZ3zmLGyQDy4y0AkA6uV1a5K3rgnR6mNXrvX+hpWMPhiAmBGMoIB30apwyvrhG+zIbaZWVKQbyjkuGPiAbkYAmMBLwMTuAmK6IPAwk0sgTuwYRQUAgD3Ja5A0gMFwNhER6tKGJAjhJeIshT7+TURo7Q-ADx6JKgArE9o4GjgQSzNmyDOZYLQXzTBMhsHUBFrgqS8VEr2AIadUJoN7AkMemQh8ysjFqxemAN6n06FwWQBgTYB4PpGgyJQRIvAPKbkAblLJEBbERQdqbJcyMwDUxyvYB+mkg65QJkTOABiGhiKMSYuRA0YH1BcUzRBHiJp+I2gtdBK0vH+LzoEguYUi71V6j7VqESbLfwGrExIisEkUOkVQgBzJ+rQn9JuK8KR9TaC1HoLqsR0Tj1IMoga49aEAxqdfOp5tmQ9UasgaOrUWlfNwts32uRJTXGcfaPpYz2YxAAErUHsAwceopkiAP1BLDJbF+Z2AcFgQ2tNjrIANhi6o8SGhiAoCYBg95sjEhiCyKA3BlGqkCVkmaGVzzcBGFKKqRoFz8NNH8Bgth9llQLAeS05pcqHl4fQrkPJ5SYCGYzA8vonjqhisyPVdM0neEwMDHk+Tt5alSJwaZNgRAA3ZYoTgAw6XpGImme09oABUyAPUetiKjVyPqUDIi8NCXFgN+HHTBhDNgUYpCDGNHTL1PrLbWw0oGuIAEvotCgOi3WfB7w5pxZ8xN3rfX3wDR6lA6JmDuEkGGnlK5WB7zuf9O55JaYPiTR6vh54vIOXTeiZhP4WBsNkQmztpbGmE2aRWlAPasoiGiSkDwVTiKetLf8vqbzZ2Ao8N9FIP84BKhFLwQs5yYbIEubua5aLbm6AvQ89E7q6ZnOIP6ZcKQx35veSkK5+40U-hjSkWwVrFo2vrRQXAmx8zurAHqgyYB8REHANAeAtAwBiAAI6WDEPASg+YKCT3kmAa0gT0MKBkimIsDJOAigUEEEICh3CeATZIhoiGsRAA)
