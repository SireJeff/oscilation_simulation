import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Define system parameters
m1 = 1.0    # Mass of first pendulum (kg)
m2 = 1.0    # Mass of second pendulum (kg)
kappa = 0.5 # Spring constant (N/m)
ell = 1.0   # Length of pendulums (m)
g = 9.81    # Acceleration due to gravity (m/s^2)

# Equations of motion
def equations(t, y):
    theta1, omega1, theta2, omega2 = y
    dtheta1_dt = omega1
    domega1_dt = -(g / ell) * theta1 - (kappa / m1) * (theta1 - theta2)
    dtheta2_dt = omega2
    domega2_dt = -(g / ell) * theta2 - (kappa / m2) * (theta2 - theta1)
    return [dtheta1_dt, domega1_dt, dtheta2_dt, domega2_dt]

# Initial conditions: [theta1, omega1, theta2, omega2]
y0 = [0.1, 0, 0.1, 0]  # Small initial angles in radians

# Time span for the simulation
t_span = (0, 20)  # seconds
t_eval = np.linspace(t_span[0], t_span[1], 1000)

# Solve the ODE
solution = solve_ivp(equations, t_span, y0, t_eval=t_eval, method='RK45')

# Extract solutions
theta1 = solution.y[0]
theta2 = solution.y[2]

# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(solution.t, theta1, label=r'$\theta_1$')
plt.plot(solution.t, theta2, label=r'$\theta_2$')
plt.title('Dynamics of Two Coupled Oscillators')
plt.xlabel('Time (s)')
plt.ylabel('Angular Displacement (rad)')
plt.legend()
plt.grid(True)
plt.show()
