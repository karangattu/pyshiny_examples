## Build a Robust Shiny for Python Application (Express Mode)

**Goal:** Create a high-quality, interactive Shiny for Python application using the *Express* mode. The application should be robust, handle data correctly, follow best practices, and be easy to maintain.

**Key Concepts (for the LLM):**

*   **Shiny for Python (Express Mode):**  A simplified way to build Shiny apps in Python.  It uses a more concise syntax compared to the traditional `app_ui`/`server` structure.  It's designed for rapid prototyping and simpler applications.
*   **Reactivity:** The core of Shiny. User input changes automatically trigger updates in the UI (outputs).
*   **Pandas DataFrames:** The standard for tabular data in Python.  Shiny works best with DataFrames.
*   **`reactive.Value`:** A special variable that holds a value and automatically triggers updates when changed.
*   **`@reactive.effect`:**  A decorator. The function runs whenever a reactive value it depends on changes.  *Crucially, it should only update `reactive.Value` objects, NOT directly modify the UI.*
*   **`@render.ui`, `@render.table`, `@render.plot`, `@render.data_frame`:** Decorators that define how to display output.  In Express mode, these are often placed directly within the UI layout.
*    **`shiny.express`:** This module contains the key functions for Express mode (`input`, `ui`, `render`).
*    **`shinywidgets`**: Used for creating interactive `plotly` graphs.

**Guidelines (Structured for Clarity):**

1.  **Data Handling (Tables):**

    *   **MANDATORY:** Use Pandas DataFrames for *all* data displayed in tables (`@render.table` or `@render.data_frame`).
    *   **Initialize Early:** Create DataFrames at the start, even if they're initially empty. Avoid using Python lists and converting later.
    *   **Synthetic Data:** Generate realistic synthetic data *within* the application. The data should reflect the user's request.  Do *not* load external files.
    * **DataFrame Creation**
        *   Use the dictionary method.
        *   Ensure all columns have the same length. Use `len()` to verify.
        *   Build column by column.
        *   Use explicit lengths with NumPy or random data.
        *   Use list comprehensions/loops for synchronized data.
        *   (Debugging Tip: Print array lengths before DataFrame creation.)

2.  **Reactive UI Updates (Express Mode Specifics):**

    *   **`@reactive.effect` for Logic:** Use `@reactive.effect` to *update* `reactive.Value` objects (or reactive calculations) in response to input changes.  *Never* put UI update code inside `@reactive.effect`.
    *   **`@render...` for Display:**  In Express mode, `@render.ui`, `@render.table`, `@render.plot`, etc., are often placed *directly* within the UI layout where you want the output to appear.  This is different from the traditional Shiny structure.
    *  **Shiny Update Functions:** For existing UI elements, utilize Shiny-provided update functions within a render block or from a `reactive.Effect`, but avoid directly calling UI functions within the effect.
    *   **Example (Express Mode):**
        ```python
        from shiny import reactive
        from shiny.express import input, ui, render
        import pandas as pd

        # Dataframe creation (example - adjust as needed)
        data = pd.DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6]})

        with ui.card(): # card added for structure
            ui.input_slider("n", "Multiplier", 1, 10, 2)

            @render.table  # Directly inside the UI layout
            def result_table():
                df = data.copy()
                df['col1'] = df['col1'] * input.n()  # Use input.n()
                return df
        ```

3.  **Global vs. Reactive:**

    *   **Minimize Globals:** Use globals *only* for data that *never* changes.
    *   **Reactive for Dynamic Data:** Use `reactive.Value`, `reactive.Calc`, etc., for anything that needs to change.

4.  **Error Prevention:**

    *   **DataFrame Check:** Always ensure data for tables is a DataFrame.
    *   **UI Update Check:** Verify UI updates use `@render...` decorators appropriately.
    *   **Event Handling:** Check that event handlers (e.g., `@reactive.event`) update reactive values correctly.

5.  **Shiny for Python API:**

    *   **Official Documentation:** Use *only* functions and components from the official Shiny for Python documentation.
    *   **No Undocumented Features:** Avoid undocumented or experimental features.
    *   **Certainty:** Only use components you are *absolutely sure* about.
    *   **No Third-Party Extensions:** Avoid them unless specifically requested.

6.  **User Input Validation (Dates):**

    *   **Date Handling:** Convert `input.date_range()` (which returns `datetime.date` objects) to `datetime64[ns]` (Pandas Timestamp) *before* comparisons with DataFrame columns.

        ```python
        # Correct date handling:
        start_date = pd.to_datetime(input.date_range()[0])
        end_date = pd.to_datetime(input.date_range()[1])
        filtered_df = df[(df['date'] >= start_date) & (df['date'] <= end_date)]
        ```

7. **Output Placement:**
    * **Beside Input Components:** Ensure that each `output_text` component is placed directly beside its corresponding `input` component. Do not club all the outputs at the bottom of the app.
    * **Consistent Layout:** Maintain a consistent layout where each input and its related output are visually grouped together.

**Technical Constraints and Best Practices (Express Mode):**

*   **Library Adherence:**
    *   Do *not* translate R Shiny code directly.
    *   IDs (for components and `@reactive.event`) must be letters, numbers, and underscores *only*.  No hyphens (e.g., `task_modal_save`, not `task_modal-save`).
    *   Use only official Shiny for Python library functions.
    *   Validate code against the current function reference.

*   **Data Handling:**
    *   Generate synthetic data internally, matching user requirements.
    *   `input.date_range()` returns `datetime.date` objects. Convert to `datetime64[ns]` for DataFrame comparisons (as shown above).
    *   `@render.table` *requires* a Pandas DataFrame.  Lists or dictionaries will cause errors.
    *  **DataGrid:**
        * `@render.DataGrid` takes dataframes.
        *  Use the correct selection modes, such as rows, none, region, row, cell, col, or cols.
        *  Example: `render.DataGrid(df, selection_mode="row")`

*   **Styling:** Use "px" units for `max_height_mobile`, `height`, and `width` (e.g., `height="300px"`).

*   **Visualizations:**
    *   **Basic:** Use `matplotlib` (remember `import matplotlib.pyplot as plt`).
    *   **Advanced/Interactive:** Use `plotly`.  *Import `render_widget` from `shinywidgets`*:
        ```python
        from shinywidgets import render_widget
        from shiny.express import ui

        with ui.card(): # card added for structure
            @render_widget
            def my_plotly_plot():
                # ... Plotly figure creation ...
        ```
    *   **Font Awesome Icons:**
        *   Include Font Awesome CSS:
            ```python
            ui.head_content(
                ui.HTML('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.2/css/all.min.css">')
            )
            ```
        *   Use `fa-solid` icons (e.g., `<i class="fa-solid fa-chart-simple"></i>`).
    *   **Placeholder Images:** Use `https://picsum.photos/200/300`.

*   **Mandatory IDs:**  *Always* include an `id` argument when creating UI components (e.g., `ui.input_text("text_input", "Enter text:", id="my_text_input")`).

*    **Express Mode Imports:** Use the following import structure:
    ```python
    from shiny import reactive
    from shiny.express import input, ui, render
    ```
* **`@render...` Placement (Express):**  Place `@render.ui`, `@render.plot`, etc., *directly* within the UI layout where the output should appear.

*   **HTML Tags:** Use `ui.tags` (e.g., `ui.tags.div("Hello")`).

**Prohibited Practices (Things to Avoid):**

*   Do *not* use `ui.input_switch`. Use `ui.input_dark_mode` instead.
*   Do *not* load data from external files.
*   Do *not* use `@output` above rendering functions.
*   Do *not* use `ui.panel_sidebar` or `ui.panel_main`. Use `ui.sidebar` instead.
*   Do *not* include `app = App(app_ui, server=None)` or `app_ui = ui.page_opts...` in Express mode.  Shiny Express handles app creation automatically.
*   Do *not* use `ui.icon` for icons. Use `ui.tags.i` with Font Awesome classes.

**Deliverable:**

*   A single, complete, runnable Python file (Shiny Express app) in a python code block.
*   Comments explaining complex logic.
*   A list of required packages (e.g., `shiny`, `pandas`, `matplotlib`, `plotly`, `shinywidgets`).
*  A brief technical description of the app.
*  Instructions for installing dependencies and running the app.

### Use the first positional argument as the id (Recommended)

Examples of Incorrect Code
```python
# ❌ WRONG - id specified twice
ui.input_checkbox("full_screen", "Enable Full Screen", value=False, id="fs_check")
ui.input_slider("height", "Height (px)", min=100, max=800, value=300, id="height_slider")
```

Correct Approach
```python
# ✅ CORRECT - first argument becomes the id
ui.input_checkbox("full_screen", "Enable Full Screen", value=False)
ui.input_slider("height", "Height (px)", min=100, max=800, value=300)
```
Some high quality examples are shown below
* Reactive plot in sidebar

```python
import seaborn as sns

# Import data from shared.py
from shared import df
from shiny.express import input, render, ui

ui.page_opts(title="Hello sidebar!")

with ui.sidebar():
    ui.input_select("var", "Select variable", choices=["bill_length_mm", "body_mass_g"])
    ui.input_switch("species", "Group by species", value=True)
    ui.input_switch("show_rug", "Show Rug", value=True)


@render.plot
def hist():
    hue = "species" if input.species() else None
    sns.kdeplot(df, x=input.var(), hue=hue)
    if input.show_rug():
        sns.rugplot(df, x=input.var(), hue=hue, color="black", alpha=0.25)
```


* Navigating multiple panels

```python
import seaborn as sns

# Import data from shared.py
from shared import df
from shiny.express import input, render, ui

ui.page_opts(title="Shiny navigation components")

ui.nav_spacer()  # Push the navbar items to the right

footer = ui.input_select(
    "var", "Select variable", choices=["bill_length_mm", "body_mass_g"]
)

with ui.nav_panel("Page 1"):
    with ui.navset_card_underline(title="Penguins data", footer=footer):
        with ui.nav_panel("Plot"):

            @render.plot
            def hist():
                p = sns.histplot(
                    df, x=input.var(), facecolor="#007bc2", edgecolor="white"
                )
                return p.set(xlabel=None)

        with ui.nav_panel("Table"):

            @render.data_frame
            def data():
                return df[["species", "island", input.var()]]


with ui.nav_panel("Page 2"):
    "This is the second 'page'."
```

* Restaurant tips dashboard

```python
import faicons as fa
import plotly.express as px

# Load data and compute static values
from shared import app_dir, tips
from shiny import reactive, render
from shiny.express import input, ui
from shinywidgets import render_plotly

bill_rng = (min(tips.total_bill), max(tips.total_bill))

# Add page title and sidebar
ui.page_opts(title="Restaurant tipping", fillable=True)

with ui.sidebar(open="desktop"):
    ui.input_slider(
        "total_bill",
        "Bill amount",
        min=bill_rng[0],
        max=bill_rng[1],
        value=bill_rng,
        pre="$",
    )
    ui.input_checkbox_group(
        "time",
        "Food service",
        ["Lunch", "Dinner"],
        selected=["Lunch", "Dinner"],
        inline=True,
    )
    ui.input_action_button("reset", "Reset filter")

# Add main content
ICONS = {
    "user": fa.icon_svg("user", "regular"),
    "wallet": fa.icon_svg("wallet"),
    "currency-dollar": fa.icon_svg("dollar-sign"),
    "ellipsis": fa.icon_svg("ellipsis"),
}

with ui.layout_columns(fill=False):
    with ui.value_box(showcase=ICONS["user"]):
        "Total tippers"

        @render.express
        def total_tippers():
            tips_data().shape[0]

    with ui.value_box(showcase=ICONS["wallet"]):
        "Average tip"

        @render.express
        def average_tip():
            d = tips_data()
            if d.shape[0] > 0:
                perc = d.tip / d.total_bill
                f"{perc.mean():.1%}"

    with ui.value_box(showcase=ICONS["currency-dollar"]):
        "Average bill"

        @render.express
        def average_bill():
            d = tips_data()
            if d.shape[0] > 0:
                bill = d.total_bill.mean()
                f"${bill:.2f}"


with ui.layout_columns(col_widths=[6, 6, 12]):
    with ui.card(full_screen=True):
        ui.card_header("Tips data")

        @render.data_frame
        def table():
            return render.DataGrid(tips_data())

    with ui.card(full_screen=True):
        with ui.card_header(class_="d-flex justify-content-between align-items-center"):
            "Total bill vs tip"
            with ui.popover(title="Add a color variable", placement="top"):
                ICONS["ellipsis"]
                ui.input_radio_buttons(
                    "scatter_color",
                    None,
                    ["none", "sex", "smoker", "day", "time"],
                    inline=True,
                )

        @render_plotly
        def scatterplot():
            color = input.scatter_color()
            return px.scatter(
                tips_data(),
                x="total_bill",
                y="tip",
                color=None if color == "none" else color,
                trendline="lowess",
            )

    with ui.card(full_screen=True):
        with ui.card_header(class_="d-flex justify-content-between align-items-center"):
            "Tip percentages"
            with ui.popover(title="Add a color variable"):
                ICONS["ellipsis"]
                ui.input_radio_buttons(
                    "tip_perc_y",
                    "Split by:",
                    ["sex", "smoker", "day", "time"],
                    selected="day",
                    inline=True,
                )

        @render_plotly
        def tip_perc():
            from ridgeplot import ridgeplot

            dat = tips_data()
            dat["percent"] = dat.tip / dat.total_bill
            yvar = input.tip_perc_y()
            uvals = dat[yvar].unique()

            samples = [[dat.percent[dat[yvar] == val]] for val in uvals]

            plt = ridgeplot(
                samples=samples,
                labels=uvals,
                bandwidth=0.01,
                colorscale="viridis",
                colormode="row-index",
            )

            plt.update_layout(
                legend=dict(
                    orientation="h", yanchor="bottom", y=1.02, xanchor="center", x=0.5
                )
            )

            return plt


ui.include_css(app_dir / "styles.css")

# --------------------------------------------------------
# Reactive calculations and effects
# --------------------------------------------------------


@reactive.calc
def tips_data():
    bill = input.total_bill()
    idx1 = tips.total_bill.between(bill[0], bill[1])
    idx2 = tips.time.isin(input.time())
    return tips[idx1 & idx2]


@reactive.effect
@reactive.event(input.reset)
def _():
    ui.update_slider("total_bill", value=bill_rng)
    ui.update_checkbox_group("time", selected=["Lunch", "Dinner"])
```

* Location distance calculator

```python
import ipyleaflet as L
from faicons import icon_svg
from geopy.distance import geodesic, great_circle
from shared import BASEMAPS, CITIES
from shiny import reactive
from shiny.express import input, render, ui
from shinywidgets import render_widget

city_names = sorted(list(CITIES.keys()))

ui.page_opts(title="Location Distance Calculator", fillable=True)
{"class": "bslib-page-dashboard"}

with ui.sidebar():
    ui.input_selectize("loc1", "Location 1", choices=city_names, selected="New York")
    ui.input_selectize("loc2", "Location 2", choices=city_names, selected="London")
    ui.input_selectize(
        "basemap",
        "Choose a basemap",
        choices=list(BASEMAPS.keys()),
        selected="WorldImagery",
    )
    ui.input_dark_mode(mode="dark")

with ui.layout_column_wrap(fill=False):
    with ui.value_box(showcase=icon_svg("globe"), theme="gradient-blue-indigo"):
        "Great Circle Distance"

        @render.text
        def great_circle_dist():
            circle = great_circle(loc1xy(), loc2xy())
            return f"{circle.kilometers.__round__(1)} km"

    with ui.value_box(showcase=icon_svg("ruler"), theme="gradient-blue-indigo"):
        "Geodisic Distance"

        @render.text
        def geo_dist():
            dist = geodesic(loc1xy(), loc2xy())
            return f"{dist.kilometers.__round__(1)} km"

    with ui.value_box(showcase=icon_svg("mountain"), theme="gradient-blue-indigo"):
        "Altitude Difference"

        @render.text
        def altitude():
            try:
                return f'{loc1()["altitude"] - loc2()["altitude"]} m'
            except TypeError:
                return "N/A (altitude lookup failed)"


with ui.card():
    ui.card_header("Map (drag the markers to change locations)")

    @render_widget
    def map():
        return L.Map(zoom=4, center=(0, 0))


# Reactive values to store location information
loc1 = reactive.value()
loc2 = reactive.value()


# Update the reactive values when the selectize inputs change
@reactive.effect
def _():
    loc1.set(CITIES.get(input.loc1(), loc_str_to_coords(input.loc1())))
    loc2.set(CITIES.get(input.loc2(), loc_str_to_coords(input.loc2())))


# When a marker is moved, the input value gets updated to "lat, lon",
# so we decode that into a dict (and also look up the altitude)
def loc_str_to_coords(x: str) -> dict:
    latlon = x.split(", ")
    if len(latlon) != 2:
        return {}

    lat = float(latlon[0])
    lon = float(latlon[1])

    try:
        import requests

        query = f"https://api.open-elevation.com/api/v1/lookup?locations={lat},{lon}"
        r = requests.get(query).json()
        altitude = r["results"][0]["elevation"]
    except Exception:
        altitude = None

    return {"latitude": lat, "longitude": lon, "altitude": altitude}


# Convenient way to get the lat/lons as a tuple
@reactive.calc
def loc1xy():
    return loc1()["latitude"], loc1()["longitude"]


@reactive.calc
def loc2xy():
    return loc2()["latitude"], loc2()["longitude"]


# Add marker for first location
@reactive.effect
def _():
    update_marker(map.widget, loc1xy(), on_move1, "loc1")


# Add marker for second location
@reactive.effect
def _():
    update_marker(map.widget, loc2xy(), on_move2, "loc2")


# Add line and fit bounds when either marker is moved
@reactive.effect
def _():
    update_line(map.widget, loc1xy(), loc2xy())


# If new bounds fall outside of the current view, fit the bounds
@reactive.effect
def _():
    l1 = loc1xy()
    l2 = loc2xy()

    lat_rng = [min(l1[0], l2[0]), max(l1[0], l2[0])]
    lon_rng = [min(l1[1], l2[1]), max(l1[1], l2[1])]
    new_bounds = [
        [lat_rng[0], lon_rng[0]],
        [lat_rng[1], lon_rng[1]],
    ]

    b = map.widget.bounds
    if len(b) == 0:
        map.widget.fit_bounds(new_bounds)
    elif (
        lat_rng[0] < b[0][0]
        or lat_rng[1] > b[1][0]
        or lon_rng[0] < b[0][1]
        or lon_rng[1] > b[1][1]
    ):
        map.widget.fit_bounds(new_bounds)


# Update the basemap
@reactive.effect
def _():
    update_basemap(map.widget, input.basemap())


# ---------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------


def update_marker(map: L.Map, loc: tuple, on_move: object, name: str):
    remove_layer(map, name)
    m = L.Marker(location=loc, draggable=True, name=name)
    m.on_move(on_move)
    map.add_layer(m)


def update_line(map: L.Map, loc1: tuple, loc2: tuple):
    remove_layer(map, "line")
    map.add_layer(
        L.Polyline(locations=[loc1, loc2], color="blue", weight=2, name="line")
    )


def update_basemap(map: L.Map, basemap: str):
    for layer in map.layers:
        if isinstance(layer, L.TileLayer):
            map.remove_layer(layer)
    map.add_layer(L.basemap_to_tiles(BASEMAPS[input.basemap()]))


def remove_layer(map: L.Map, name: str):
    for layer in map.layers:
        if layer.name == name:
            map.remove_layer(layer)


def on_move1(**kwargs):
    return on_move("loc1", **kwargs)


def on_move2(**kwargs):
    return on_move("loc2", **kwargs)


# When the markers are moved, update the selectize inputs to include the new
# location (which results in the locations() reactive value getting updated,
# which invalidates any downstream reactivity that depends on it)
def on_move(id, **kwargs):
    loc = kwargs["location"]
    loc_str = f"{loc[0]}, {loc[1]}"
    choices = city_names + [loc_str]
    ui.update_selectize(id, selected=loc_str, choices=choices)

```
