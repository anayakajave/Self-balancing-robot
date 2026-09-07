import numpy as np
import matplotlib.pyplot as plt

# -------------------------
# Parameters
# -------------------------

g = 9.81
L = 1.0

# -------------------------
# Initial Conditions
# -------------------------

theta = np.radians(10)   # 10 degrees
omega = 0.0

# -------------------------
# Simulation Settings
# -------------------------

dt = 0.01
T = 10

time = np.arange(0, T, dt)

theta_history = []
omega_history = []

# -------------------------
# Simulation Loop
# -------------------------

for t in time:

    theta_dot = omega

    omega_dot = -(g / L) * np.sin(theta)

    theta = theta + theta_dot * dt
    omega = omega + omega_dot * dt

    theta_history.append(np.degrees(theta))
    omega_history.append(omega)

# -------------------------
# Plot Angle
# -------------------------

plt.figure(figsize=(8,5))
plt.plot(time, theta_history)

plt.xlabel("Time (s)")
plt.ylabel("Angle (deg)")
plt.title("State Space Pendulum - Angle")

plt.grid(True)
plt.show()