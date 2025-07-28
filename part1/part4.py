import numpy as np
import matplotlib.pyplot as plt

# System parameters
length = 1.0  # Length of the pendulums (m)
spring_constant = 0.5  # Spring constant (N/m)
gravity = 9.81  # Gravitational acceleration (m/s^2)
amplitude = 0.1  # Amplitude of oscillation (rad)
time_end = 10  # Duration of simulation (s)
dt = 0.01  # Time step (s)
d = 4.0  # Separation distance between pendulums (m)

# Time array
time_steps = int(time_end / dt)
time = np.linspace(0, time_end, time_steps)

# Calculate normal mode frequencies
omega_plus = np.sqrt(gravity / length + spring_constant / 1.0)  # In-phase mode frequency
omega_minus = np.sqrt(gravity / length)  # Out-of-phase mode frequency

# Calculate angles for both modes
theta1_plus = amplitude * np.cos(omega_plus * time)  # In-phase mode
theta2_plus = amplitude * np.cos(omega_plus * time)

theta1_minus = amplitude * np.cos(omega_minus * time)  # Out-of-phase mode
theta2_minus = -amplitude * np.cos(omega_minus * time)

# Plotting In-Phase Mode
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(time, theta1_plus, label='Mass 1')
plt.plot(time, theta2_plus, label='Mass 2')
plt.title(f'In-Phase Mode (ω = {omega_plus:.2f} rad/s)')
plt.xlabel('Time (s)')
plt.ylabel('Angular Displacement (rad)')
plt.legend()
plt.grid(True)

# Plotting Out-of-Phase Mode
plt.subplot(1, 2, 2)
plt.plot(time, theta1_minus, label='Mass 1')
plt.plot(time, theta2_minus, label='Mass 2')
plt.title(f'Out-of-Phase Mode (ω = {omega_minus:.2f} rad/s)')
plt.xlabel('Time (s)')
plt.ylabel('Angular Displacement (rad)')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

# Print the angular frequencies
print(f'In-Phase Mode Angular Frequency: {omega_plus:.2f} rad/s')
print(f'Out-of-Phase Mode Angular Frequency: {omega_minus:.2f} rad/s')
