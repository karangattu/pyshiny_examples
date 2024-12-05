import datetime
import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from shiny import App, render, ui, reactive

# Synthetic Data Generation
def generate_volunteer_data():
    organizations = [
        "Red Cross", "Local Food Bank", "Animal Shelter", 
        "Community Garden", "Senior Center", "Youth Mentorship Program", 
        "Environmental Conservation Group", "Homeless Shelter", 
        "Local Hospital", "Community Clean-up Initiative"
    ]
    
    categories = [
        "Community Service", "Healthcare", "Animal Welfare", 
        "Environmental", "Education", "Senior Support", 
        "Youth Development", "Emergency Response"
    ]
    
    locations = [
        "Downtown", "Westside", "Eastside", "Northend", "Southend", 
        "Suburban Area", "Urban Center", "Rural Community"
    ]
    
    data = []
    for i in range(50):
        start_date = pd.Timestamp.now() + pd.Timedelta(days=random.randint(0, 180))
        end_date = start_date + pd.Timedelta(days=random.randint(1, 30))
        
        data.append({
            "opportunity_id": f"VOL{i+1:03d}",
            "organization": random.choice(organizations),
            "title": f"Volunteer {random.choice(['Project', 'Initiative', 'Program'])} {i+1}",
            "category": random.choice(categories),
            "location": random.choice(locations),
            "start_date": start_date,
            "end_date": end_date,
            "hours_needed": random.randint(2, 40),
            "skills_required": random.sample(["Communication", "Physical Labor", "Technical Skills", 
                                              "Teaching", "Emotional Support", "Administrative"], 
                                             random.randint(1, 3)),
            "spots_available": random.randint(1, 20)
        })
    
    return pd.DataFrame(data)

# Generate volunteer data
volunteer_df = generate_volunteer_data()

# Shiny App
app_ui = ui.page_fluid(
    ui.head_content(
        ui.HTML('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.1/css/all.min.css">')
    ),
    ui.panel_title("Volunteer Opportunity Tracker"),
    ui.layout_sidebar(
        ui.sidebar(
            ui.input_selectize("category", "Select Category", 
                               choices=["All"] + list(volunteer_df["category"].unique()), 
                               multiple=False),
            ui.input_selectize("location", "Select Location", 
                               choices=["All"] + list(volunteer_df["location"].unique()), 
                               multiple=False),
            ui.input_date_range("date_range", "Date Range"),
            ui.input_action_button("apply_filters", "Apply Filters", class_="btn-primary"),
        ),
        ui.layout_columns(
            ui.card(
                ui.card_header("Available Opportunities"),
                ui.output_data_frame("opportunities_table"),
                full_screen=True
            ),
            ui.card(
                ui.card_header("Opportunities by Category"),
                ui.output_plot("category_plot"),
                full_screen=True
            )
        )
    )
)

def server(input, output, session):
    @reactive.calc
    def filtered_opportunities():
        df = volunteer_df.copy()
        
        # Date Range Filter
        if input.date_range()[0] and input.date_range()[1]:
            start_date = datetime.datetime.combine(input.date_range()[0], datetime.datetime.min.time())
            end_date = datetime.datetime.combine(input.date_range()[1], datetime.datetime.max.time())
            df = df[(df['start_date'] >= start_date) & (df['end_date'] <= end_date)]
        
        # Category Filter
        if input.category() != "All":
            df = df[df['category'] == input.category()]
        
        # Location Filter
        if input.location() != "All":
            df = df[df['location'] == input.location()]
        
        return df

    @render.data_frame
    def opportunities_table():
        df = filtered_opportunities()
        return render.DataGrid(
            df[['opportunity_id', 'organization', 'title', 'category', 'location', 'start_date', 'end_date', 'hours_needed', 'spots_available']],
            selection_mode="rows"
        )

    @render.plot
    def category_plot():
        df = filtered_opportunities()
        category_counts = df['category'].value_counts()
        
        plt.figure(figsize=(10, 6))
        category_counts.plot(kind='bar', color='skyblue', edgecolor='black')
        plt.title('Volunteer Opportunities by Category')
        plt.xlabel('Category')
        plt.ylabel('Number of Opportunities')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        
        return plt.gcf()

app = App(app_ui, server)