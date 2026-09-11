import numpy as np
import matplotlib.pyplot as plt

# =====================================
# PARAMETERS
# =====================================

g = 9.81
L = 1.0

Kp = 15

dt = 0.01
T = 10

# =====================================
# INITIAL CONDITIONS
# =====================================

theta = np.radians(10)
omega = 0

# =====================================
# STORAGE
# =====================================

theta_history = []
time_history = []

# =====================================
# SIMULATION LOOP
# =====================================

t = 0

while t < T:

    # Error

    error = -theta

    # P Controller

    u = Kp * error

    # State Equations

    theta_dot = omega

    omega_dot = (g / L) * np.sin(theta) + u

    # Euler Integration

    theta = theta + theta_dot * dt
    omega = omega + omega_dot * dt

    # Save Data

    theta_history.append(np.degrees(theta))
    time_history.append(t)

    t += dt

# =====================================
# PLOT
# =====================================

plt.figure(figsize=(10,5))

plt.plot(time_history, theta_history)

plt.title("P Controller Response")
plt.xlabel("Time (s)")
plt.ylabel("Angle (deg)")

plt.grid(True)

plt.savefig(
    "images/day3/p_controller_response.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()