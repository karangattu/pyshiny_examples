This app demonstrates:

1. All parameters of `update_select`:
   - `id`: Identifies which select input to update
   - `label`: Updates the label text
   - `choices`: Updates the available choices
   - `selected`: Updates the selected value

2. The app includes:
   - A select input with initial grouped choices
   - An action button to trigger the update
   - A text display showing the current selection
   - A reactive effect that updates the select input when the button is clicked

3. Key features:
   - Uses express mode syntax
   - Uses static data generated within the app
   - Minimal design focusing on `update_select` functionality
   - Demonstrates grouped choices in both initial and updated states
   - Shows how the label, choices, and selection can all be updated simultaneously

To run this app:
1. Save the code to a file (e.g., `app.py`)
2. Install required packages: `pip install shiny`
3. Run with: `shiny run app.py`

The app will show a select input with grouped state choices. Clicking the "Update" button will:
1. Change the label to include the click count
2. Replace the choices with a new set of states
3. Change the selection to "Texas"
4. The current selection will be displayed below the input
## Preview the app on [Shinylive](https://shinylive.io/py/app/#h=0&code=NobwRAdghgtgpmAXAAjFADugdOgnmAGlQGMB7CAFzkqVQDMAnUmZAZwAsBLCXZTmdKQYVkDOFGIVOANzgAdCI2ZsuPLHAAe6Ma1Z8BQkd3QBXCkROciYiABM4DBQoDEyAJIROUqABtktqAooNjgKE3QFViCqPQBeZBAFZGTkOTAAUSgo5ABhUiyKNJREsAA5AE0i1LK4AHdkcqEAazSiNNKAKSr2uuQOh1Y4XFbqnIAVbrA8iAg4SU5iMzSAXwIklLSAdThsvIKqks2AQUnNrNUAcwpyEbSAeQAlSbuxC5vCUZPaNJzfTjohJ4oCs1hAUtUALKcWy1HaFWglCGlSZQmY7UhBW5gTZuU6cVhkCCsbhYtxfFBpNykWrAsDLBT0iAuZAABSgFzgITCEQglhw7LgAH1SOgKKwABRSCg+OCxNIAVXQASoyAAynAZZJkAAROAwUgjOicHw+KAAIxlsTGDBMcAAlE4ILUvOxkHzTbhSGZBcT7GaoAxxXbEOtks6KK6+b64P7A8HQ+C3ZwsMZvRIpORBWazNcIOK0uFlfIPgqlYFOerNSIPKZ4URiKbdIK5WAYGaALQAZjSDrBieSCfBrjG7E5gyrfAgteQsIA5CbkGbOYXAtwLoOUnzUxQfRq5hR833++C0lFy60N-2fuxSKRBshgmeqCHCJfE8QbwsdrEnztQcfE3Hfc4FsFsKjSN9ewTcNI2TYgA1sIMQyPRM+XghhbEFUcoHsQMfhMBgbBESt904d5ewAt8AAEbFwrAqA0QoUPBew6GQRZCOoHcgPmcgkLfcExDCBgwTofDOMoEIqzIiBim3LBfyDekwEdACaOoOiGKYgDWLdMsqEFMgTEofjmOPISCNE9oTDbBxkFINiVxiOSpzMLAnLgJSIKZCBXHSOg6H3ZBrn8PVyCiBhyz0otdyrBR1PTGQ4HUAL93isREtkdRZBM+SPN7XTBVModkEVItgtHKSgu3GcXWQWZ6g-Ugvz0KA7Cq3ifPBPkPNi-dDwA6EW1-C8zOSU0lx8WIxLAMry1sNVogrPdOuQcUch8BYmmQZwQDy-TPLtZYHVfMb2M-Yhv0SM6TzAVUvQjBwwVVJbWAOATjzSAAxAAZSYvp8IRoVpf8AM+sAxgADUmMZNCyUawfBo4AC1JiOBhOAAL3IWkPuSRkANWN8eKoUC0ih7zwTtOkAF0gA)
