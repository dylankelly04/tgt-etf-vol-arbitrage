import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Initialize figure and 3D axis
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Function to generate dummy data
def generate_dummy_data():
    time = np.linspace(0.1, 2.5, 30)  # Time to expiration
    strike = np.linspace(50, 150, 30)  # Strike prices
    time, strike = np.meshgrid(time, strike)
    iv = np.exp(-time) * np.sin(strike / 50) + np.random.uniform(0.3, 0.5)  # Dummy IV
    return time, strike, iv

# Update function for animation
def update(frame):
    global ax
    ax.clear()  # Clear the previous frame
    
    # Generate dummy data for API 1
    time1, strike1, iv1 = generate_dummy_data()
    # Generate dummy data for API 2
    time2, strike2, iv2 = generate_dummy_data()
    
    # Plot API 1 data
    ax.plot_surface(strike1, time1, iv1, cmap="viridis", alpha=0.7, edgecolor='k', label="API 1")
    # Plot API 2 data
    ax.plot_surface(strike2, time2, iv2, cmap="plasma", alpha=0.7, edgecolor='k', label="API 2")
    
    # Customize plot
    ax.set_title("Combined Implied Volatility Surface (Live Update)")
    ax.set_xlabel("Strike Price")
    ax.set_ylabel("Time to Expiration")
    ax.set_zlabel("Implied Volatility")
    plt.tight_layout()

# Set up the animation
ani = FuncAnimation(fig, update, interval=1000)  # Update every 15 seconds

# Show the graph
plt.show()
