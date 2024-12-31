from shiny import reactive
from shiny.express import input, ui, render
import pandas as pd

# Sample data generation
df = pd.DataFrame(
    {
        "name": ["John", "Jane", "Bob", "Alice"],
        "age": [25, 30, 35, 28],
        "city": ["New York", "London", "Paris", "Tokyo"],
    }
)

# Set page options
ui.page_opts(title="TagList Demo", fillable=True)

with ui.sidebar():
    ui.input_selectize(
        "person", "Select Person", choices=df["name"].tolist(), multiple=True
    )
    ui.input_action_button("update_btn", "Update Display")
    ui.hr()
    ui.markdown("### About TagList")
    ui.markdown(
        """
    TagList is a container for HTML elements that allows:
    - Multiple elements to be grouped
    - Dynamic updates
    - Nested structures
    """
    )

# Main content area using TagList features
with ui.card():
    ui.card_header("Basic TagList Example")

    @render.ui
    def basic_list():
        return ui.TagList(
            ui.h3("Header in TagList"),
            ui.p("This is a paragraph in TagList"),
            ui.div(ui.strong("Bold text"), " and normal text"),
        )

with ui.card():
    ui.card_header("Dynamic TagList with Data")

    @render.ui
    @reactive.event(input.update_btn)
    def dynamic_list():
        if not input.person():
            return ui.TagList(ui.p("Please select a person", class_="text-muted"))

        selected_data = df[df["name"].isin(input.person())]

        elements = [ui.h4("Selected People:")]

        for _, row in selected_data.iterrows():
            elements.append(
                ui.div(
                    ui.tags.b(f"Name: {row['name']}"),
                    ui.br(),
                    f"Age: {row['age']}, City: {row['city']}",
                    class_="border p-2 mb-2",
                )
            )

        return ui.TagList(*elements)

with ui.card():
    ui.card_header("Nested TagList Example")

    @render.ui
    def nested_list():
        inner_list = ui.TagList(
            ui.tags.li("First nested item"), ui.tags.li("Second nested item")
        )

        outer_list = ui.TagList(
            ui.h4("Nested Structure"), ui.tags.ul(inner_list), ui.p("Footer text")
        )

        return outer_list

with ui.card():
    ui.card_header("TagList with Dependencies")

    @render.ui
    def dependent_list():
        # Create a TagList with conditional elements
        elements = []

        if input.person():
            elements.extend(
                [
                    ui.div(
                        f"You have selected {len(input.person())} people",
                        class_="alert alert-info",
                    ),
                    ui.p(f"Selected names: {', '.join(input.person())}"),
                ]
            )
        else:
            elements.append(
                ui.div("No selections made", class_="alert alert-warning")
            )

        return ui.TagList(*elements)
