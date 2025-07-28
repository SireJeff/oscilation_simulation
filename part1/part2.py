import numpy as np
import matplotlib.pyplot as plt

# Define system parameters
m1 = 1.0    # Mass of first pendulum (kg)
m2 = 1.0    # Mass of second pendulum (kg)
kappa = 0.5 # Spring constant (N/m)
ell = 1.0   # Length of pendulums (m)
g = 9.81    # Acceleration due to gravity (m/s^2)

# Define the equations of motion
def derivatives(t, y):
    theta1, omega1, theta2, omega2 = y
    dtheta1_dt = omega1
    domega1_dt = -(g / ell) * theta1 - (kappa / m1) * (theta1 - theta2)
    dtheta2_dt = omega2
    domega2_dt = -(g / ell) * theta2 - (kappa / m2) * (theta2 - theta1)
    return np.array([dtheta1_dt, domega1_dt, dtheta2_dt, domega2_dt])

# Runge-Kutta 4th Order Method
def runge_kutta_4(y0, t0, tf, h):
    num_steps = int((tf - t0) / h)
    t = np.linspace(t0, tf, num_steps + 1)
    y = np.zeros((num_steps + 1, len(y0)))
    y[0] = y0
    for i in range(num_steps):
        ti = t[i]
        yi = y[i]
        k1 = derivatives(ti, yi)
        k2 = derivatives(ti + h/2, yi + h/2 * k1)
        k3 = derivatives(ti + h/2, yi + h/2 * k2)
        k4 = derivatives(ti + h, yi + h * k3)
        y[i+1] = yi + (h/6)*(k1 + 2*k2 + 2*k3 + k4)
    return t, y

# Initial conditions: [theta1, omega1, theta2, omega2]
y0 = [0.1, 0.0, 0.1, 0.0]  # Small initial angles in radians

# Time parameters
t0 = 0.0    # Start time (s)
tf = 20.0   # End time (s)
h = 0.01    # Time step (s)

# Perform the integration
t, y = runge_kutta_4(y0, t0, tf, h)

# Extract angular displacements
theta1 = y[:, 0]
theta2 = y[:, 2]

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(t, theta1, label=r'$\theta_1$')
plt.plot(t, theta2, label=r'$\theta_2$')
plt.title('Dynamics of Two Coupled Oscillators using RK4')
plt.xlabel('Time (s)')
plt.ylabel('Angular Displacement (rad)')
plt.legend()
plt.grid(True)
plt.show()
