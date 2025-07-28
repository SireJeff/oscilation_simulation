import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define system parameters
m = 1.0      # Mass of each oscillator (kg)
K1 = 10.0    # Spring constant for adjacent connections (N/m)
K2 = 5.0     # Spring constant for next-nearest connections (N/m)
K3 = 2.0     # Spring constant for opposite connections (N/m)
N = 6        # Number of oscillators

# Stiffness Matrix K (from Task 2)
K = np.array([
    [32, -10, -5, -2, -5, -10],
    [-10, 32, -10, -5, -2, -5],
    [-5, -10, 32, -10, -5, -2],
    [-2, -5, -10, 32, -10, -5],
    [-5, -2, -5, -10, 32, -10],
    [-10, -5, -2, -5, -10, 32]
])

# Eigenvalues and Eigenvectors (from Task 2)
eigenvalues = np.array([0.00, 29.00, 29.00, 44.00, 45.00, 45.00])
eigenvectors = np.array([
    [-0.40824829, -0.57543483, -0.04699037,  0.40824829, -0.04344317,  0.57571349],
    [-0.40824829, -0.24702256, -0.52183636, -0.40824829, -0.47686092, -0.32547964],
    [-0.40824829,  0.32841227, -0.47484599,  0.40824829,  0.52030409, -0.25023386],
    [-0.40824829,  0.57543483,  0.04699037, -0.40824829, -0.04344317,  0.57571349],
    [-0.40824829,  0.24702256,  0.52183636,  0.40824829, -0.47686092, -0.32547964],
    [-0.40824829, -0.32841227,  0.47484599, -0.40824829,  0.52030409, -0.25023386]
])

# Calculate angular frequencies
omega = np.sqrt(eigenvalues)
# Handle zero frequency (Mode 1) to avoid division by zero
omega[omega == 0] = 0.0

# Define time parameters
t_max = 10              # Maximum time (s)
dt = 0.05               # Time step (s)
t = np.arange(0, t_max, dt)  # Time array

# Define amplitude scaling factor
A = 1.0  # Maximum displacement amplitude

# Define oscillator positions in a circle
radius = 5.0  # Radius of the circle
angles = np.linspace(0, 2 * np.pi, N, endpoint=False)  # Angles for each oscillator
x_eq = radius * np.cos(angles)  # Equilibrium x positions
y_eq = radius * np.sin(angles)  # Equilibrium y positions

# Set up the figure with 2x3 subplots
fig, axes = plt.subplots(2, 3, figsize=(18, 10))
plt.tight_layout(pad=4.0)

# Initialize oscillator markers and spring lines for each subplot
oscillators = []
springs = []
mode_texts = []
for ax in axes.flatten():
    # Plot equilibrium circle
    ax.set_xlim(-radius*1.5, radius*1.5)
    ax.set_ylim(-radius*1.5, radius*1.5)
    ax.set_aspect('equal')
    ax.grid(True)
    # Initialize oscillator markers
    osc, = ax.plot([], [], 'o', color='blue', markersize=8)
    oscillators.append(osc)
    # Initialize spring lines
    spring_lines = []
    for _ in range(N):
        line, = ax.plot([], [], '-', color='black', linewidth=1)
        spring_lines.append(line)
    springs.append(spring_lines)
    # Initialize mode information text
    text = ax.text(0.05, 0.95, '', transform=ax.transAxes, fontsize=12,
                  verticalalignment='top')
    mode_texts.append(text)

# Function to initialize the background of the animation
def init():
    for osc in oscillators:
        osc.set_data([], [])
    for spring_set in springs:
        for spring in spring_set:
            spring.set_data([], [])
    for text in mode_texts:
        text.set_text('')
    return oscillators + [spring for spring_set in springs for spring in spring_set] + mode_texts

# Animation function to update all subplots
def animate(frame):
    for mode in range(N):
        current_omega = omega[mode]
        current_eigenvector = eigenvectors[:, mode]
        
        # Compute displacement for current time frame
        if current_omega == 0:
            displacement = np.zeros(N)
        else:
            displacement = A * np.cos(current_omega * frame * dt)
        
        # Update oscillator positions
        x = x_eq + current_eigenvector * displacement
        y = y_eq + current_eigenvector * displacement
        
        # Update oscillators
        oscillators[mode].set_data(x, y)
        
        # Update springs (connect to immediate neighbors)
        for i in range(N):
            j = (i + 1) % N  # Next oscillator index
            springs[mode][i].set_data([x[i], x[j]], [y[i], y[j]])
        
        # Update mode information text
        mode_texts[mode].set_text(f'Mode {mode + 1}\nω = {current_omega:.2f} rad/s')
    
    return oscillators + [spring for spring_set in springs for spring in spring_set] + mode_texts

# Create the animation
ani = FuncAnimation(fig, animate, frames=len(t), init_func=init,
                    blit=True, interval=50, repeat=True)

plt.show()
