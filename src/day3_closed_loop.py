import numpy as np
import matplotlib.pyplot as plt

# ==========================
# PARAMETERS
# ==========================

g = 9.81
L = 1.0

Kp = 20

dt = 0.01
T = 10

# ==========================
# INITIAL CONDITIONS
# ==========================

theta = np.radians(10)
omega = 0

# ==========================
# STORAGE
# ==========================

time_history = []
theta_history = []

# ==========================
# SIMULATION LOOP
# ==========================

for t in np.arange(0, T, dt):

    control = -Kp * theta

    alpha = (g / L) * np.sin(theta) + control

    omega = omega + alpha * dt
    theta = theta + omega * dt

    time_history.append(t)
    theta_history.append(np.degrees(theta))

# ==========================
# PLOT
# ==========================

plt.figure(figsize=(10,5))

plt.plot(time_history, theta_history)

plt.title("Closed Loop Pendulum")
plt.xlabel("Time (s)")
plt.ylabel("Angle (deg)")
plt.grid(True)

plt.savefig(
    "images/day3/closed_loop_response.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()