import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

from shiny import App, reactive, render, ui

# Synthetic Data Generation
def generate_medical_data():
    """Generate synthetic medical dataset for disease and treatment analysis."""
    np.random.seed(42)
    
    # Diseases
    diseases = [
        "Hypertension", 
        "Diabetes Type 2", 
        "Heart Disease", 
        "Rheumatoid Arthritis", 
        "Asthma"
    ]
    
    # Treatments
    treatments = {
        "Hypertension": ["ACE Inhibitors", "Beta Blockers", "Diuretics"],
        "Diabetes Type 2": ["Metformin", "Insulin", "Sulfonylureas"],
        "Heart Disease": ["Statins", "Blood Thinners", "Beta Blockers"],
        "Rheumatoid Arthritis": ["Methotrexate", "Biologics", "Corticosteroids"],
        "Asthma": ["Inhaled Corticosteroids", "Bronchodilators", "Leukotriene Modifiers"]
    }
    
    # Adverse Events
    adverse_events = {
        "ACE Inhibitors": ["Dry Cough", "Dizziness", "Hyperkalemia"],
        "Beta Blockers": ["Fatigue", "Cold Extremities", "Depression"],
        "Metformin": ["Diarrhea", "Nausea", "Vitamin B12 Deficiency"],
        "Insulin": ["Weight Gain", "Hypoglycemia", "Injection Site Reaction"],
        "Statins": ["Muscle Pain", "Liver Damage", "Memory Issues"]
    }
    
    # Generate patient data
    n_patients = 1000
    data = []
    
    for _ in range(n_patients):
        disease = np.random.choice(diseases)
        treatment = np.random.choice(treatments[disease])
        adverse_event = np.random.choice(adverse_events.get(treatment, ["None"]))
        
        treatment_efficacy = np.random.uniform(0.5, 0.95)
        age = np.random.randint(18, 80)
        
        data.append({
            "Disease": disease,
            "Treatment": treatment,
            "Adverse_Event": adverse_event,
            "Treatment_Efficacy": treatment_efficacy,
            "Patient_Age": age
        })
    
    return pd.DataFrame(data)

# Global dataset
medical_df = generate_medical_data()

# Shiny App
app_ui = ui.page_fluid(
    ui.panel_title("Medical Treatment & Adverse Event Explorer"),
    ui.layout_sidebar(
        ui.sidebar(
            ui.input_select(
                "disease_select", 
                "Select Disease", 
                choices=medical_df['Disease'].unique().tolist()
            ),
            ui.input_checkbox_group(
                "treatment_select", 
                "Select Treatments", 
                choices=medical_df['Treatment'].unique().tolist()
            ),
            ui.input_slider(
                "age_range", 
                "Patient Age Range", 
                min=18, 
                max=80, 
                value=[30, 60]
            ),
            ui.input_dark_mode(id="dark_mode")
        ),
        ui.layout_columns(
            ui.card(
                ui.card_header("Treatment Efficacy Distribution"),
                ui.output_plot("treatment_efficacy_plot")
            ),
            ui.card(
                ui.card_header("Adverse Event Frequency"),
                ui.output_plot("adverse_events_plot")
            )
        ),
        ui.layout_columns(
            ui.card(
                ui.card_header("Disease Prevalence"),
                ui.output_plot("disease_prevalence_plot")
            ),
            ui.card(
                ui.card_header("Detailed Analysis"),
                ui.output_table("detailed_table")
            )
        )
    )
)

def server(input, output, session):
    @reactive.calc
    def filtered_data():
        df = medical_df.copy()
        
        # Filter by disease
        df = df[df['Disease'] == input.disease_select()]
        
        # Filter by treatments
        if input.treatment_select():
            df = df[df['Treatment'].isin(input.treatment_select())]
        
        # Filter by age range
        df = df[
            (df['Patient_Age'] >= input.age_range()[0]) & 
            (df['Patient_Age'] <= input.age_range()[1])
        ]
        
        return df

    @render.plot
    def treatment_efficacy_plot():
        df = filtered_data()
        plt.figure(figsize=(10, 6))
        df.boxplot(column='Treatment_Efficacy', by='Treatment')
        plt.title(f"Treatment Efficacy for {input.disease_select()}")
        plt.ylabel("Efficacy Score")
        plt.xticks(rotation=45)
        return plt.gcf()

    @render.plot
    def adverse_events_plot():
        df = filtered_data()
        adverse_counts = df['Adverse_Event'].value_counts()
        plt.figure(figsize=(10, 6))
        adverse_counts.plot(kind='bar')
        plt.title(f"Adverse Events for {input.disease_select()}")
        plt.xlabel("Adverse Event")
        plt.ylabel("Frequency")
        plt.xticks(rotation=45)
        return plt.gcf()

    @render.plot
    def disease_prevalence_plot():
        plt.figure(figsize=(10, 6))
        medical_df['Disease'].value_counts().plot(kind='pie', autopct='%1.1f%%')
        plt.title("Disease Prevalence")
        return plt.gcf()

    @render.table
    def detailed_table():
        df = filtered_data()
        summary = df.groupby('Treatment').agg({
            'Treatment_Efficacy': ['mean', 'std'],
            'Patient_Age': ['mean', 'min', 'max']
        }).reset_index()
        summary.columns = ['Treatment', 'Avg Efficacy', 'Efficacy Std Dev', 'Avg Age', 'Min Age', 'Max Age']
        return summary

app = App(app_ui, server)