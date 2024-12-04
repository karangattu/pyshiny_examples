import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from shiny import App, ui, render, reactive

# Generate synthetic data
np.random.seed(123)

# Disease prevalence data
diseases = ['Diabetes', 'Hypertension', 'Heart Disease', 'Asthma', 'Arthritis']
regions = ['North', 'South', 'East', 'West', 'Central']
prevalence_data = pd.DataFrame({
    'Disease': np.repeat(diseases, len(regions)),
    'Region': regions * len(diseases),
    'Prevalence_Rate': np.random.uniform(5, 25, len(diseases) * len(regions))
})

# Treatment efficacy data
treatments = ['Drug A', 'Drug B', 'Drug C', 'Drug D']
diseases_treated = ['Diabetes', 'Hypertension', 'Heart Disease']
efficacy_data = pd.DataFrame({
    'Treatment': np.repeat(treatments, len(diseases_treated)),
    'Disease': diseases_treated * len(treatments),
    'Efficacy_Rate': np.random.uniform(60, 95, len(treatments) * len(diseases_treated)),
    'Sample_Size': np.random.randint(100, 1000, len(treatments) * len(diseases_treated))
})

# Adverse events data
adverse_events = ['Nausea', 'Headache', 'Dizziness', 'Fatigue', 'Rash']
adverse_data = pd.DataFrame({
    'Treatment': np.repeat(treatments, len(adverse_events)),
    'Adverse_Event': adverse_events * len(treatments),
    'Frequency': np.random.uniform(1, 15, len(treatments) * len(adverse_events))
})

# Define the UI
app_ui = ui.page_fluid(
    ui.panel_title("Clinical Data Explorer"),
    
    ui.layout_sidebar(
        ui.sidebar(
            ui.h4("Filters and Controls"),
            ui.input_select(
                "viz_type",
                "Select Visualization",
                choices=["Disease Prevalence", "Treatment Efficacy", "Adverse Events"]
            ),
            ui.panel_conditional(
                "input.viz_type === 'Disease Prevalence'",
                ui.input_selectize(
                    "selected_regions",
                    "Select Regions",
                    choices=regions,
                    multiple=True,
                    selected=regions[0]
                )
            ),
            ui.panel_conditional(
                "input.viz_type === 'Treatment Efficacy'",
                ui.input_selectize(
                    "selected_diseases",
                    "Select Diseases",
                    choices=diseases_treated,
                    multiple=True,
                    selected=diseases_treated[0]
                )
            ),
            ui.panel_conditional(
                "input.viz_type === 'Adverse Events'",
                ui.input_selectize(
                    "selected_treatments",
                    "Select Treatments",
                    choices=treatments,
                    multiple=True,
                    selected=treatments[0]
                )
            )
        ),
        ui.output_plot("main_plot"),
        ui.output_table("data_table")
    )
)

def server(input, output, session):
    
    @render.plot
    def main_plot():
        plt.figure(figsize=(12, 6))
        
        if input.viz_type() == "Disease Prevalence":
            filtered_data = prevalence_data[
                prevalence_data['Region'].isin(input.selected_regions())
            ]
            
            plt.figure(figsize=(12, 6))
            bars = plt.bar(
                range(len(filtered_data)), 
                filtered_data['Prevalence_Rate'],
                color='skyblue'
            )
            plt.xlabel('Disease - Region')
            plt.ylabel('Prevalence Rate (%)')
            plt.title('Disease Prevalence by Region')
            plt.xticks(
                range(len(filtered_data)),
                [f"{d}\n{r}" for d, r in zip(filtered_data['Disease'], filtered_data['Region'])],
                rotation=45,
                ha='right'
            )
            
        elif input.viz_type() == "Treatment Efficacy":
            filtered_data = efficacy_data[
                efficacy_data['Disease'].isin(input.selected_diseases())
            ]
            
            plt.figure(figsize=(12, 6))
            bars = plt.bar(
                range(len(filtered_data)), 
                filtered_data['Efficacy_Rate'],
                color='lightgreen'
            )
            plt.xlabel('Treatment - Disease')
            plt.ylabel('Efficacy Rate (%)')
            plt.title('Treatment Efficacy by Disease')
            plt.xticks(
                range(len(filtered_data)),
                [f"{t}\n{d}" for t, d in zip(filtered_data['Treatment'], filtered_data['Disease'])],
                rotation=45,
                ha='right'
            )
            
        else:  # Adverse Events
            filtered_data = adverse_data[
                adverse_data['Treatment'].isin(input.selected_treatments())
            ]
            
            plt.figure(figsize=(12, 6))
            bars = plt.bar(
                range(len(filtered_data)), 
                filtered_data['Frequency'],
                color='salmon'
            )
            plt.xlabel('Treatment - Adverse Event')
            plt.ylabel('Frequency (%)')
            plt.title('Adverse Events by Treatment')
            plt.xticks(
                range(len(filtered_data)),
                [f"{t}\n{ae}" for t, ae in zip(filtered_data['Treatment'], filtered_data['Adverse_Event'])],
                rotation=45,
                ha='right'
            )
            
        plt.tight_layout()
        return plt.gcf()

    @render.table
    def data_table():
        if input.viz_type() == "Disease Prevalence":
            return prevalence_data[
                prevalence_data['Region'].isin(input.selected_regions())
            ].round(2)
        elif input.viz_type() == "Treatment Efficacy":
            return efficacy_data[
                efficacy_data['Disease'].isin(input.selected_diseases())
            ].round(2)
        else:
            return adverse_data[
                adverse_data['Treatment'].isin(input.selected_treatments())
            ].round(2)

app = App(app_ui, server)