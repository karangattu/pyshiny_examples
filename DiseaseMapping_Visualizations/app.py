import numpy as np
import pandas as pd
import plotly.express as px
from shinywidgets import output_widget, render_widget
from shiny import App, ui, render, reactive

# Generate synthetic data
np.random.seed(42)

# Generate data for 50 states
states = [
    "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA",
    "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
    "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
    "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
    "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"
]

# Create synthetic dataset
df = pd.DataFrame({
    'state': states,
    'cases': np.random.randint(1000, 50000, size=50),
    'vaccinated': np.random.uniform(30, 95, size=50),
    'outbreak_severity': np.random.choice(['Low', 'Medium', 'High'], size=50),
    'disease_type': np.random.choice(['COVID-19', 'Influenza', 'Measles'], size=50)
})

app_ui = ui.page_fluid(
    ui.panel_title("Disease Outbreak and Vaccination Tracker"),
    
    ui.layout_sidebar(
        ui.sidebar(
            ui.h4("Filters"),
            ui.input_select(
                "disease",
                "Select Disease",
                choices=["All"] + list(df['disease_type'].unique())
            ),
            ui.input_slider(
                "vax_range",
                "Vaccination Rate Range (%)",
                min=30,
                max=95,
                value=[30, 95]
            ),
            ui.input_radio_buttons(
                "severity",
                "Outbreak Severity",
                choices=["All"] + list(df['outbreak_severity'].unique())
            ),
            width=250
        ),
        
        ui.layout_column_wrap(
            ui.value_box(
                "Total Cases",
                ui.output_text("total_cases"),
                theme="danger",
            ),
            ui.value_box(
                "Average Vaccination Rate",
                ui.output_text("avg_vax"),
                theme="success",
            ),
            ui.value_box(
                "States with High Severity",
                ui.output_text("high_severity"),
                theme="warning",
            ),
            width=1/3
        ),
        
        ui.card(
            ui.card_header("Cases by State"),
            output_widget("cases_map")
        ),
        
        ui.card(
            ui.card_header("Vaccination Rates by State"),
            output_widget("vax_map")
        ),
    )
)

def server(input, output, session):
    
    @reactive.calc
    def filtered_data():
        df_filtered = df.copy()
        
        if input.disease() != "All":
            df_filtered = df_filtered[df_filtered['disease_type'] == input.disease()]
            
        df_filtered = df_filtered[
            (df_filtered['vaccinated'] >= input.vax_range()[0]) &
            (df_filtered['vaccinated'] <= input.vax_range()[1])
        ]
        
        if input.severity() != "All":
            df_filtered = df_filtered[df_filtered['outbreak_severity'] == input.severity()]
            
        return df_filtered

    @render.text
    def total_cases():
        return f"{filtered_data()['cases'].sum():,}"

    @render.text
    def avg_vax():
        return f"{filtered_data()['vaccinated'].mean():.1f}%"

    @render.text
    def high_severity():
        return str(len(filtered_data()[filtered_data()['outbreak_severity'] == 'High']))

    @render_widget
    def cases_map():
        df_viz = filtered_data()
        fig = px.choropleth(
            df_viz,
            locations='state',
            locationmode="USA-states",
            color='cases',
            scope="usa",
            color_continuous_scale="Reds",
            title="Disease Cases by State",
            hover_data=['disease_type', 'outbreak_severity']
        )
        fig.update_layout(
            title_x=0.5,
            geo=dict(scope='usa'),
            width=800,
            height=500
        )
        return fig

    @render_widget
    def vax_map():
        df_viz = filtered_data()
        fig = px.choropleth(
            df_viz,
            locations='state',
            locationmode="USA-states",
            color='vaccinated',
            scope="usa",
            color_continuous_scale="Greens",
            title="Vaccination Rates by State (%)",
            hover_data=['disease_type', 'outbreak_severity']
        )
        fig.update_layout(
            title_x=0.5,
            geo=dict(scope='usa'),
            width=800,
            height=500
        )
        return fig

app = App(app_ui, server)