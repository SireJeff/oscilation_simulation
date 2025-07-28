from vpython import *
import numpy as np

# System parameters
length = 1.0  # Length of the pendulums (m)
spring_constant = 0.5  # Spring constant (N/m)
gravity = 9.81  # Gravitational acceleration (m/s^2)
dt = 0.01  # Time step (s)
time_end = 10  # Duration of simulation (s)

# Normal mode frequencies
omega_plus = np.sqrt(gravity / length + spring_constant / 1.0)  # In-phase mode frequency
omega_minus = np.sqrt(gravity / length)  # Out-of-phase mode frequency

# Initial conditions for the angles (small displacements)
amplitude = 0.1  # Amplitude of oscillation (rad)
time_steps = int(time_end / dt)
time = np.linspace(0, time_end, time_steps)

# Calculate angles for both modes
theta1_plus = amplitude * np.cos(omega_plus * time)  # In-phase mode
theta2_plus = amplitude * np.cos(omega_plus * time)

theta1_minus = amplitude * np.cos(omega_minus * time)  # Out-of-phase mode
theta2_minus = -amplitude * np.cos(omega_minus * time)

# Helper function to calculate pendulum positions
def get_positions(theta1, theta2):
    x1 = -2 + length * np.sin(theta1)
    y1 = -length * np.cos(theta1)
    x2 = 2 + length * np.sin(theta2)
    y2 = -length * np.cos(theta2)
    return x1, y1, x2, y2

# Initial positions
x1_plus, y1_plus, x2_plus, y2_plus = get_positions(theta1_plus[0], theta2_plus[0])
x1_minus, y1_minus, x2_minus, y2_minus = get_positions(theta1_minus[0], theta2_minus[0])

# VPython visualization setup for in-phase mode
scene1 = canvas(title="In-Phase Mode", width=600, height=400, align="left")
scene1.range = 3

# VPython visualization setup for out-of-phase mode
scene2 = canvas(title="Out-of-Phase Mode", width=600, height=400, align="right")
scene2.range = 3

# In-phase mode elements
anchor1_plus = sphere(canvas=scene1, pos=vector(-2, 0, 0), radius=0.05, color=color.red)
anchor2_plus = sphere(canvas=scene1, pos=vector(2, 0, 0), radius=0.05, color=color.red)
mass1_plus = sphere(canvas=scene1, pos=vector(x1_plus, y1_plus, 0), radius=0.1, color=color.blue)
mass2_plus = sphere(canvas=scene1, pos=vector(x2_plus, y2_plus, 0), radius=0.1, color=color.blue)
spring_plus = helix(canvas=scene1, pos=mass1_plus.pos, axis=mass2_plus.pos - mass1_plus.pos, radius=0.05, coils=10, color=color.cyan)
rod1_plus = cylinder(canvas=scene1, pos=anchor1_plus.pos, axis=mass1_plus.pos - anchor1_plus.pos, radius=0.02, color=color.gray(0.7))
rod2_plus = cylinder(canvas=scene1, pos=anchor2_plus.pos, axis=mass2_plus.pos - anchor2_plus.pos, radius=0.02, color=color.gray(0.7))

# Out-of-phase mode elements
anchor1_minus = sphere(canvas=scene2, pos=vector(-2, 0, 0), radius=0.05, color=color.red)
anchor2_minus = sphere(canvas=scene2, pos=vector(2, 0, 0), radius=0.05, color=color.red)
mass1_minus = sphere(canvas=scene2, pos=vector(x1_minus, y1_minus, 0), radius=0.1, color=color.green)
mass2_minus = sphere(canvas=scene2, pos=vector(x2_minus, y2_minus, 0), radius=0.1, color=color.green)
spring_minus = helix(canvas=scene2, pos=mass1_minus.pos, axis=mass2_minus.pos - mass1_minus.pos, radius=0.05, coils=10, color=color.orange)
rod1_minus = cylinder(canvas=scene2, pos=anchor1_minus.pos, axis=mass1_minus.pos - anchor1_minus.pos, radius=0.02, color=color.gray(0.7))
rod2_minus = cylinder(canvas=scene2, pos=anchor2_minus.pos, axis=mass2_minus.pos - anchor2_minus.pos, radius=0.02, color=color.gray(0.7))

# Animation loop
for step in range(time_steps):
    rate(100)  # Frame rate

    # Update in-phase mode
    x1_plus, y1_plus, x2_plus, y2_plus = get_positions(theta1_plus[step], theta2_plus[step])
    mass1_plus.pos = vector(x1_plus, y1_plus, 0)
    mass2_plus.pos = vector(x2_plus, y2_plus, 0)
    spring_plus.pos = mass1_plus.pos
    spring_plus.axis = mass2_plus.pos - mass1_plus.pos
    rod1_plus.axis = mass1_plus.pos - anchor1_plus.pos
    rod2_plus.axis = mass2_plus.pos - anchor2_plus.pos

    # Update out-of-phase mode
    x1_minus, y1_minus, x2_minus, y2_minus = get_positions(theta1_minus[step], theta2_minus[step])
    mass1_minus.pos = vector(x1_minus, y1_minus, 0)
    mass2_minus.pos = vector(x2_minus, y2_minus, 0)
    spring_minus.pos = mass1_minus.pos
    spring_minus.axis = mass2_minus.pos - mass1_minus.pos
    rod1_minus.axis = mass1_minus.pos - anchor1_minus.pos
    rod2_minus.axis = mass2_minus.pos - anchor2_minus.pos
