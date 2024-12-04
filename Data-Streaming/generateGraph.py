import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
from generateGraphData import generate_component_data1
import scipy.interpolate as interp

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
    
    # generate data
    time1, strike1, iv1, iv2 = generate_component_data1()

    smh_t, smh_s = np.meshgrid(np.linspace(np.min(time1), np.max(time1), len(time1)),\
                               np.linspace(np.min(strike1), np.max(strike1), len(time1)))
    smh_iv = interp.griddata((time1, strike1),iv1, (smh_t, smh_s), method='linear')
    component_iv = interp.griddata((time1, strike1),iv2, (smh_t, smh_s), method='linear')

        
    # Plot all data
    ax.plot_surface(smh_s, smh_t, smh_iv, cmap="viridis", alpha=0.7, edgecolor='k', label="SMH")
    # Plot API 2 data
    ax.plot_surface(smh_s, smh_t, component_iv, cmap="plasma", alpha=0.7, edgecolor='k', label="components")
    
    # Customize plot
    ax.set_title("Combined Implied Volatility Surface")
    ax.set_xlabel("Strike Price")
    ax.set_ylabel("Days to Expiration")
    ax.set_zlabel("Implied Volatility")
    plt.tight_layout()

# Set up the animation
ani = FuncAnimation(fig, update, interval=5*60000)  # Update every 5 minute

# Show the graph
plt.show()
