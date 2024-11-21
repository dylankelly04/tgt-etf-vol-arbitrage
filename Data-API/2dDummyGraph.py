import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import datetime
import random

# Initialize dummy data storage
times = []
implied_vols = []

# Function to generate dummy data
def generate_dummy_data():
    current_time = datetime.datetime.now()
    # Generate a random implied volatility value between 0.15 and 0.30
    iv = round(random.uniform(0.15, 0.30), 4)
    return current_time, iv

# Update graph function
def update(frame):
    # Generate new dummy data
    current_time, iv = generate_dummy_data()
    
    # Append new data
    times.append(current_time)
    implied_vols.append(iv)
    
    # Limit the number of points to display for better performance
    if len(times) > 100:
        times.pop(0)
        implied_vols.pop(0)
    
    # Clear and redraw the graph
    ax.clear()
    ax.plot(times, implied_vols, label="Implied Volatility", marker="o")
    ax.set_title("Live Dummy Implied Volatility")
    ax.set_xlabel("Time")
    ax.set_ylabel("Implied Volatility")
    ax.legend(loc="upper left")
    plt.xticks(rotation=45)
    plt.tight_layout()

# Create the figure and axes
fig, ax = plt.subplots()

# Create the animation
ani = FuncAnimation(fig, update, interval=15000)  # Update every second

# Show the live graph
plt.show()
