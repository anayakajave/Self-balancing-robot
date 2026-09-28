import numpy as np
import matplotlib.pyplot as plt
import os

# ====================================
# INITIAL STATE
# ====================================

x = 2.0
x_dot = 0.0

theta = np.radians(10)
theta_dot = 0.0

# ====================================
# STATE FEEDBACK GAINS
# ====================================

k1 = 2
k2 = 6
k3 = 50
k4 = 15

dt = 0.01
T = 10

time_history = []
theta_history = []

# ====================================
# SIMULATION
# ====================================

for t in np.arange(0, T, dt):

    u = -(
        k1*x +
        k2*x_dot +
        k3*theta +
        k4*theta_dot
    )

    x_ddot = u

    # More damped linear model
    theta_ddot = -2*theta + u

    x_dot += x_ddot * dt
    x += x_dot * dt

    theta_dot += theta_ddot * dt
    theta += theta_dot * dt

    time_history.append(t)
    theta_history.append(np.degrees(theta))

# ====================================
# SAVE IMAGE
# ====================================

os.makedirs("images/day6", exist_ok=True)

plt.figure(figsize=(10,5))
plt.plot(time_history, theta_history, linewidth=2)

plt.title("State Feedback Controller (Tuned)")
plt.xlabel("Time (s)")
plt.ylabel("Angle (deg)")
plt.grid(True)

plt.savefig(
    "images/day6/state_feedback_controller_final.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("Saved: images/day6/state_feedback_controller_final.png")