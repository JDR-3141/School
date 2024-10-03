import tkinter as tk
from tkinter import ttk
import pandas as pd
import matplotlib.pyplot as plt

# Data for the colleges
data = {
    "College": [
        "Brasenose", "Christ Church", "Magdalen", 
        "St. John's", "Queen's", "Wadham"
    ],
    "Stereotypes": [
        "Friendly, community-focused", "Prestigious, traditional",
        "Elite but welcoming", "Rigorous but friendly", 
        "Traditional yet friendly", "Progressive, inclusive"
    ],
    "Music Facilities": [
        "Practice rooms, choir, jazz society", 
        "Well-known choir, music rooms", 
        "Choir, practice rooms, jazz opportunities", 
        "Good facilities, jazz opportunities", 
        "Practice rooms, choir, jazz society", 
        "Good facilities, jazz society"
    ],
    "Distance to Andrew Wiles (miles)": [
        1.2, 1.2, 1.0, 1.0, 1.0, 1.0
    ],
    "Distance to Radcliffe Camera (miles)": [
        0.5, 0.5, 0.6, 0.6, 0.5, 0.5
    ],
    "Accommodation Cost (per week)": [
        "£115-£170", "£140-£210", "£130-£200", 
        "£140-£200", "£115-£180", "£120-£200"
    ],
    "Food Cost (per meal)": [
        "£4-£6", "£6-£10", "£6-£9", 
        "£5-£8", "£4-£7", "£4-£8"
    ],
    "Accommodation Guarantee": [
        "Yes", "Yes", "Yes", "Yes", "Yes", "Yes"
    ],
    "Other Info": [
        "Active social life", 
        "Strong academic environment", 
        "Beautiful grounds, deer park", 
        "Strong support for initiatives", 
        "Good balance of activities", 
        "Active focus on diversity"
    ]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Function to display tables and graphs
def display_data():
    # Displaying DataFrame as a table
    print("College Information:")
    print(df)

    # Creating a bar chart for Accommodation Costs
    plt.figure(figsize=(10, 6))
    df['Accommodation Cost (per week)'].str.extract('(\d+)-(\d+)').astype(float).mean(axis=1).plot(kind='bar', color='skyblue')
    plt.title('Average Accommodation Cost per Week')
    plt.xlabel('Colleges')
    plt.ylabel('Average Cost (£)')
    plt.xticks(range(len(df)), df['College'], rotation=45)
    plt.tight_layout()
    plt.show()

    # Creating a bar chart for Food Costs
    food_costs = df['Food Cost (per meal)'].str.extract('(\d+)-(\d+)').astype(float).mean(axis=1)
    plt.figure(figsize=(10, 6))
    food_costs.plot(kind='bar', color='lightgreen')
    plt.title('Average Food Cost per Meal')
    plt.xlabel('Colleges')
    plt.ylabel('Average Cost (£)')
    plt.xticks(range(len(df)), df['College'], rotation=45)
    plt.tight_layout()
    plt.show()

# Function to create a Tkinter canvas with a simple map of Oxford
def create_map():
    root = tk.Tk()
    root.title("Oxford College Map")
    canvas = tk.Canvas(root, width=800, height=600, bg="lightblue")
    canvas.pack()

    # Locations for the colleges and key places
    locations = {
        "Brasenose": (100, 300),
        "Christ Church": (150, 250),
        "Magdalen": (200, 200),
        "St. John's": (250, 250),
        "Queen's": (300, 300),
        "Wadham": (350, 350),
        "Andrew Wiles": (400, 400),
        "Radcliffe Camera": (200, 100),
    }

    # Draw dots and labels for each college
    for college, (x, y) in locations.items():
        canvas.create_oval(x, y, x + 10, y + 10, fill="blue")
        canvas.create_text(x + 15, y, text=college, anchor=tk.W)

    # Draw dots for Andrew Wiles and Radcliffe Camera
    canvas.create_oval(400, 400, 410, 410, fill="red")
    canvas.create_text(415, 400, text="Andrew Wiles", anchor=tk.W)
    
    canvas.create_oval(200, 100, 210, 110, fill="red")
    canvas.create_text(215, 100, text="Radcliffe Camera", anchor=tk.W)

    root.mainloop()

# Call functions to display data and create map
display_data()
create_map()
