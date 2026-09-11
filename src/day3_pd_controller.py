import numpy as np
import matplotlib.pyplot as plt

# ====================================
# PARAMETERS
# ====================================

g = 9.81
L = 0.2

dt = 0.01
total_time = 10

# Controller gains
Kp = 20
Kd = 5

# Initial conditions
theta = np.radians(10)   # 10 degrees
omega = 0.0

# ====================================
# DATA STORAGE
# ====================================

time_history = []
theta_history = []

# ====================================
# SIMULATION LOOP
# ====================================

for t in np.arange(0, total_time, dt):

    error = -theta

    # PD Controller
    control = Kp * error - Kd * omega

    # Pendulum dynamics
    alpha = -(g / L) * np.sin(theta) + control

    omega = omega + alpha * dt
    theta = theta + omega * dt

    time_history.append(t)
    theta_history.append(np.degrees(theta))

# ====================================
# PLOT
# ====================================

plt.figure(figsize=(10, 5))
plt.plot(time_history, theta_history)

plt.title("PD Controller Response")
plt.xlabel("Time (s)")
plt.ylabel("Angle (deg)")
plt.grid(True)

plt.savefig(
    "images/day3/pd_controller_response.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()