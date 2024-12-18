from shiny import reactive
from shiny.express import ui, input, render

# Synthetic data for the example
travel_destinations = {
    "Europe": [
        {
            "city": "Paris",
            "country": "France",
            "rating": 9.5,
            "description": "The city of love and lights, known for its iconic Eiffel Tower and rich cultural heritage.",
        },
        {
            "city": "Rome",
            "country": "Italy",
            "rating": 9.3,
            "description": "Ancient history meets modern life, home to the Colosseum and Vatican City.",
        },
        {
            "city": "Barcelona",
            "country": "Spain",
            "rating": 9.0,
            "description": "Vibrant city with stunning Gaudi architecture and beautiful Mediterranean beaches.",
        },
    ],
    "Asia": [
        {
            "city": "Tokyo",
            "country": "Japan",
            "rating": 9.2,
            "description": "A fascinating blend of ultra-modern and traditional, with cutting-edge technology and ancient temples.",
        },
        {
            "city": "Seoul",
            "country": "South Korea",
            "rating": 8.8,
            "description": "Dynamic metropolis known for K-pop, technology, and delicious cuisine.",
        },
        {
            "city": "Bali",
            "country": "Indonesia",
            "rating": 9.4,
            "description": "Tropical paradise with beautiful beaches, lush landscapes, and rich cultural experiences.",
        },
    ],
    "Americas": [
        {
            "city": "New York",
            "country": "USA",
            "rating": 9.1,
            "description": "The city that never sleeps, home to iconic skyscrapers and diverse cultural experiences.",
        },
        {
            "city": "Rio de Janeiro",
            "country": "Brazil",
            "rating": 8.9,
            "description": "Famous for its carnival, beautiful beaches, and the Christ the Redeemer statue.",
        },
        {
            "city": "Vancouver",
            "country": "Canada",
            "rating": 9.0,
            "description": "Scenic city nestled between mountains and ocean, known for its natural beauty and multiculturalism.",
        },
    ],
}

# Page options with title
ui.page_opts(title="Travel Destinations Markdown Demo")

# Sidebar for region selection
with ui.sidebar():
    ui.input_select(
        "region", "Select Travel Region", choices=list(travel_destinations.keys())
    )

# Main content area with markdown and dynamic content
ui.markdown(
    """
# Travel Destination Explorer 🌍✈️

Explore amazing travel destinations from around the world! 
Select a region from the sidebar to see top-rated cities.

## How to Use
- Choose a region from the dropdown menu
- Discover fascinating destinations with their ratings and descriptions
"""
)


# Render destinations based on selected region
@render.ui
def destination_details():
    region = input.region()
    destinations = travel_destinations[region]

    # Use markdown to format the destination details
    markdown_content = f"## Top Destinations in {region}\n\n"

    for dest in destinations:
        markdown_content += f"""
### {dest['city']}, {dest['country']} (Rating: {dest['rating']}/10)

{dest['description']}

---
"""

    return ui.markdown(markdown_content)
