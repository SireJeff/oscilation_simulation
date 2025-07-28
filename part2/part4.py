import numpy as np
import matplotlib.pyplot as plt

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
dt = 0.01               # Time step (s)
t = np.arange(0, t_max, dt)  # Time array

# Define amplitude scaling factor
A = 1.0  # Maximum displacement amplitude

# Create figure and subplots
fig, axes = plt.subplots(2, 3, figsize=(18, 10))
fig.suptitle('Oscillation Patterns of Normal Modes', fontsize=16)
plt.subplots_adjust(wspace=0.3, hspace=0.4)

# Iterate over each mode and plot oscillation patterns
for mode in range(N):
    ax = axes.flatten()[mode]
    current_omega = omega[mode]
    current_eigenvector = eigenvectors[:, mode]
    
    # Calculate displacement for each oscillator over time
    # x_j(t) = A * v_ji * cos(omega_i * t)
    if current_omega == 0:
        displacement = np.zeros_like(t)
    else:
        displacement = A * np.cos(current_omega * t)
    
    # Calculate displacement for each oscillator
    oscillators_displacement = current_eigenvector[:, np.newaxis] * displacement
    
    # Plot oscillation patterns for each oscillator
    for osc in range(N):
        ax.plot(t, oscillators_displacement[osc], label=f'Oscillator {osc + 1}')
    
    # Set plot title and labels
    ax.set_title(f'Mode {mode + 1}: ω = {current_omega:.2f} rad/s', fontsize=14)
    ax.set_xlabel('Time (s)', fontsize=12)
    ax.set_ylabel('Displacement (units)', fontsize=12)
    ax.legend(loc='upper right', fontsize=8)
    ax.grid(True)

# Display the plots
plt.show()
