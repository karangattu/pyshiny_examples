from datetime import datetime, timedelta
import pandas as pd
import numpy as np
from shiny import App, ui, render, reactive
import random

# Generate mock data
opportunities = pd.DataFrame({
    "id": range(1, 21),
    "title": [
        "Food Bank Helper", "Animal Shelter Assistant", "Library Reading Buddy",
        "Park Cleanup Volunteer", "Senior Center Assistant", "Youth Mentor",
        "Community Garden Helper", "Homeless Shelter Aid", "Museum Guide",
        "School Tutor", "Beach Cleanup", "Food Pantry Worker",
        "Wildlife Conservation", "Hospital Helper", "Literacy Program",
        "Soup Kitchen", "Children's Sports Coach", "Elderly Companion",
        "Environmental Educator", "Art Gallery Guide"
    ],
    "organization": [
        "City Food Bank", "Happy Paws Shelter", "Public Library",
        "Parks Department", "Golden Years Center", "Youth First",
        "Green Thumb Society", "Hope Shelter", "City Museum",
        "Education First", "Ocean Friends", "Community Pantry",
        "Wildlife Trust", "General Hospital", "Reading Partners",
        "Helping Hands", "Youth Sports League", "Elder Care",
        "Nature Center", "Art Society"
    ],
    "location": np.random.choice([
        "Downtown", "North Side", "South Side", "West End", "East Side",
        "Central", "Riverside", "Parkview", "Hillside", "Lake Area"
    ], 20),
    "hours_per_week": np.random.randint(2, 21, 20),
    "duration_weeks": np.random.randint(4, 25, 20),
    "skills_needed": [
        "Communication", "Animal Care", "Reading",
        "Physical Labor", "Patience", "Mentoring",
        "Gardening", "Social Skills", "Public Speaking",
        "Teaching", "Physical Labor", "Organization",
        "Nature Knowledge", "Healthcare", "Teaching",
        "Food Service", "Coaching", "Companionship",
        "Environmental", "Art Knowledge"
    ],
    "start_date": [
        datetime.now() + timedelta(days=x) for x in range(0, 60, 3)
    ],
    "spots_available": np.random.randint(1, 11, 20)
})

# Create the UI
app_ui = ui.page_fluid(
    ui.panel_title("Volunteer Opportunities Tracker"),
    
    ui.layout_sidebar(
        ui.sidebar(
            ui.h4("Search & Filter"),
            ui.input_text("search", "Search by keyword", placeholder="Enter keywords..."),
            ui.input_select(
                "location", "Location",
                choices=["All"] + list(opportunities["location"].unique())
            ),
            ui.input_slider(
                "hours", "Hours per week",
                min=min(opportunities["hours_per_week"]),
                max=max(opportunities["hours_per_week"]),
                value=[min(opportunities["hours_per_week"]), max(opportunities["hours_per_week"])]
            ),
            ui.input_select(
                "sort_by", "Sort by",
                choices={
                    "start_date": "Start Date",
                    "hours_per_week": "Hours per Week",
                    "spots_available": "Spots Available"
                }
            ),
            ui.input_switch("show_available", "Show only available positions", value=True)
        ),
        
        ui.navset_tab(
            ui.nav_panel(
                "Available Opportunities",
                ui.output_data_frame("opportunities_table")
            ),
            ui.nav_panel(
                "My Applications",
                ui.output_data_frame("applications_table")
            )
        )
    )
)

def server(input, output, session):
    # Store applications in a reactive value
    applications = reactive.Value([])
    
    @reactive.calc
    def filtered_opportunities():
        df = opportunities.copy()
        
        # Apply search filter
        if input.search():
            search_term = input.search().lower()
            mask = (
                df["title"].str.lower().str.contains(search_term) |
                df["organization"].str.lower().str.contains(search_term) |
                df["skills_needed"].str.lower().str.contains(search_term)
            )
            df = df[mask]
        
        # Apply location filter
        if input.location() != "All":
            df = df[df["location"] == input.location()]
        
        # Apply hours filter
        df = df[
            (df["hours_per_week"] >= input.hours()[0]) &
            (df["hours_per_week"] <= input.hours()[1])
        ]
        
        # Apply availability filter
        if input.show_available():
            df = df[df["spots_available"] > 0]
        
        # Apply sorting
        df = df.sort_values(input.sort_by())
        
        return df

    @render.data_frame
    def opportunities_table():
        df = filtered_opportunities()
        df = df[[
            "title", "organization", "location", "hours_per_week",
            "start_date", "spots_available", "skills_needed"
        ]]
        return render.DataGrid(
            df,
            row_selection_mode="single",
            height="600px",
            filters=True
        )

    @render.data_frame
    def applications_table():
        apps = pd.DataFrame(applications.get())
        if len(apps) == 0:
            return render.DataGrid(
                pd.DataFrame(columns=[
                    "Title", "Organization", "Status", "Applied Date"
                ])
            )
        return render.DataGrid(apps)

    @reactive.effect
    @reactive.event(input.opportunities_table_selected)
    def _():
        selected_idx = input.opportunities_table_selected()
        if not selected_idx:
            return
        
        selected_opp = filtered_opportunities().iloc[selected_idx[0]]
        
        # Show confirmation dialog
        m = ui.modal(
            "Would you like to apply for this position?",
            title=f"Apply to {selected_opp['title']}",
            easy_close=True,
            footer=ui.row(
                ui.column(6, ui.input_action_button("confirm_apply", "Apply", class_="btn-primary")),
                ui.column(6, ui.modal_button("Cancel"))
            )
        )
        ui.modal_show(m)

    @reactive.effect
    @reactive.event(input.confirm_apply)
    def _():
        selected_idx = input.opportunities_table_selected()
        if not selected_idx:
            return
        
        selected_opp = filtered_opportunities().iloc[selected_idx[0]]
        
        # Add to applications
        current_apps = applications.get()
        new_app = {
            "Title": selected_opp["title"],
            "Organization": selected_opp["organization"],
            "Status": "Pending",
            "Applied Date": datetime.now().strftime("%Y-%m-%d")
        }
        current_apps.append(new_app)
        applications.set(current_apps)
        
        # Show success message
        ui.notification_show("Application submitted successfully!", type="message")
        ui.modal_remove()

app = App(app_ui, server)