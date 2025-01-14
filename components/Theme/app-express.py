from shiny import reactive
from shiny.express import input, ui, render

# Configure page options with a custom theme
ui.page_opts(
    title="Theme Demo",
    fillable=True,
    theme=ui.Theme()
    .add_defaults(
        font_family="'Arial', sans-serif",
        primary="#007bff",
        secondary="#6c757d",
        success="#28a745",
        info="#17a2b8",
        warning="#ffc107",
        danger="#dc3545",
    )
    .add_rules(
        """
        body { 
            line-height: 1.6;
        }
        h1, h2, h3 { 
            color: var(--bs-primary);
            margin-bottom: 1rem;
        }
        .custom-text {
            color: var(--bs-info);
            font-weight: bold;
            padding: 1rem;
            border-radius: 4px;
            background-color: rgba(var(--bs-info-rgb), 0.1);
        }
        .themed-link {
            color: var(--bs-primary);
            text-decoration: none;
            padding: 0.5rem 1rem;
            border: 1px solid var(--bs-primary);
            border-radius: 4px;
            display: inline-block;
            margin: 1rem 0;
        }
        .themed-link:hover {
            background-color: var(--bs-primary);
            color: white;
            transition: all 0.3s ease;
        }
        """
    ),
)

with ui.layout_sidebar():
    with ui.sidebar():
        ui.h3("Sidebar Controls")
        ui.input_text("name", "Enter your name", "User")
        ui.input_slider("size", "Text size", 12, 32, 16)
        ui.input_select(
            "color",
            "Select color theme",
            {
                "primary": "Primary",
                "success": "Success",
                "warning": "Warning",
                "danger": "Danger",
            },
        )

    with ui.card():
        ui.h1("Theme Demonstration")
        ui.p("This text demonstrates the base styling.", class_="custom-text")
        ui.a("Hover over me to see theme colors", href="#", class_="themed-link")
        ui.hr()

        @render.ui
        def dynamic_content():
            return ui.div(
                f"Hello, {input.name()}!",
                style=f"color: var(--bs-{input.color()}); font-size: {input.size()}px;",
            )


with ui.card():
    ui.h2("Additional Theme Examples")

    with ui.layout_column_wrap():
        with ui.value_box(
            showcase=ui.HTML(
                '<i class="fa-solid fa-palette" style="font-size: 2rem;"></i>'
            ),
            theme="primary",
        ):
            "Theme Colors"
            "Customizable palette"
            "Using Bootstrap variables"

        with ui.value_box(
            showcase=ui.HTML(
                '<i class="fa-solid fa-font" style="font-size: 2rem;"></i>'
            ),
            theme="success",
        ):
            "Typography"
            "Custom fonts & sizes"
            "Consistent styling"

# Add Font Awesome for icons
ui.head_content(
    ui.tags.link(
        rel="stylesheet",
        href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css",
    )
)
