import numpy as np
import pandas as pd
from datetime import datetime, timedelta
from shiny import App, Inputs, Outputs, Session, reactive, render, ui

# Generate sample data
np.random.seed(42)
raw_materials = pd.DataFrame({
    'material': ['Hops', 'Barley', 'Yeast', 'Grapes'],
    'current_inventory': np.random.randint(100, 1000, 4),
    'min_inventory': np.random.randint(50, 300, 4),
    'lead_time': np.random.randint(7, 30, 4)
})

work_in_progress = pd.DataFrame({
    'product': ['IPA', 'Chardonnay', 'Stout', 'Cabernet'],
    'current_qty': np.random.randint(100, 1000, 4),
    'target_qty': np.random.randint(500, 2000, 4),
    'completion_date': [datetime.now() + timedelta(days=np.random.randint(7, 30)) for _ in range(4)]
})

finished_goods = pd.DataFrame({
    'product': ['IPA', 'Chardonnay', 'Stout', 'Cabernet'],
    'current_qty': np.random.randint(100, 1000, 4),
    'target_qty': np.random.randint(500, 2000, 4),
    'last_shipment': [datetime.now() - timedelta(days=np.random.randint(7, 30)) for _ in range(4)]
})

app_ui = ui.page_fluid(
    ui.panel_title("Inventory Management Dashboard"),
    ui.layout_column_wrap(
        ui.value_box(
            "Raw Materials",
            str(raw_materials['current_inventory'].sum()),
            f"Min Inventory: {raw_materials['min_inventory'].sum()}",
            showcase=ui.tags.i(class_="fa-solid fa-boxes-stacked", style="font-size: 2rem;"),
            theme="bg-gradient-orange-red",
            full_screen=True,
        ),
        ui.value_box(
            "Work in Progress",
            str(work_in_progress['current_qty'].sum()),
            f"Target Qty: {work_in_progress['target_qty'].sum()}",
            showcase=ui.tags.i(class_="fa-solid fa-cubes", style="font-size: 2rem;"),
            theme="bg-gradient-purple-pink",
            full_screen=True,
        ),
        ui.value_box(
            "Finished Goods",
            str(finished_goods['current_qty'].sum()),
            f"Target Qty: {finished_goods['target_qty'].sum()}",
            showcase=ui.tags.i(class_="fa-solid fa-box-open", style="font-size: 2rem;"),
            theme="bg-gradient-green-teal",
            full_screen=True,
        ),
        width=1/3,
    ),
    ui.layout_column_wrap(
        ui.card(
            ui.card_header("Raw Materials"),
            ui.output_data_frame("raw_materials_table"),
        ),
        ui.card(
            ui.card_header("Work in Progress"),
            ui.output_data_frame("wip_table"),
        ),
        ui.card(
            ui.card_header("Finished Goods"),
            ui.output_data_frame("finished_goods_table"),
        ),
        width=2/3,
    )
)

def server(input: Inputs, output: Outputs, session: Session):
    @render.data_frame
    def raw_materials_table():
        return raw_materials

    @render.data_frame
    def wip_table():
        return work_in_progress

    @render.data_frame
    def finished_goods_table():
        return finished_goods

app = App(app_ui, server)