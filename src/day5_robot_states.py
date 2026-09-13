import numpy as np
import matplotlib.pyplot as plt

# ==========================
# Initial Robot State
# ==========================

x = 0.0
x_dot = 0.5

theta = np.radians(10)
theta_dot = 0.0

dt = 0.01
T = 10

# ==========================
# Storage
# ==========================

time_history = []

x_history = []
xdot_history = []

theta_history = []
thetadot_history = []

# ==========================
# Simulation
# ==========================

for t in np.arange(0, T, dt):

    # Simple demonstration dynamics

    x = x + x_dot * dt

    theta = theta + theta_dot * dt

    # Gravity effect

    theta_dot = theta_dot + np.sin(theta) * dt

    # Save data

    time_history.append(t)

    x_history.append(x)
    xdot_history.append(x_dot)

    theta_history.append(np.degrees(theta))
    thetadot_history.append(theta_dot)

# ==========================
# Plot
# ==========================

plt.figure(figsize=(10,8))

plt.subplot(2,2,1)
plt.plot(time_history, x_history)
plt.title("Position x")
plt.grid()

plt.subplot(2,2,2)
plt.plot(time_history, xdot_history)
plt.title("Velocity x_dot")
plt.grid()

plt.subplot(2,2,3)
plt.plot(time_history, theta_history)
plt.title("Angle theta")
plt.grid()

plt.subplot(2,2,4)
plt.plot(time_history, thetadot_history)
plt.title("Angular Velocity theta_dot")
plt.grid()

plt.tight_layout()

import os
os.makedirs("images/day5", exist_ok=True)

plt.savefig(
    "images/day5/four_state_robot.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()