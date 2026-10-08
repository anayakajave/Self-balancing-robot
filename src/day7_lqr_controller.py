import numpy as np
import matplotlib.pyplot as plt
import os
from scipy.linalg import solve_continuous_are

# ====================================
# SIMPLE ROBOT MODEL
# ====================================

A = np.array([
    [0, 1, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 1],
    [0, 0, -1, 0]
])

B = np.array([
    [0],
    [1],
    [0],
    [1]
])

# ====================================
# LQR WEIGHTS
# ====================================

Q = np.diag([1, 1, 100, 10])

R = np.array([[0.1]])

# ====================================
# COMPUTE LQR GAIN
# ====================================

P = solve_continuous_are(A, B, Q, R)

K = np.linalg.inv(R) @ B.T @ P

print("LQR Gain K:")
print(K)

# ====================================
# INITIAL STATE
# ====================================

X = np.array([
    [2.0],                 # position
    [0.0],                 # velocity
    [np.radians(10)],      # angle
    [0.0]                  # angular velocity
])

dt = 0.01
T = 10

time_history = []
theta_history = []

# ====================================
# SIMULATION
# ====================================

for t in np.arange(0, T, dt):

    u = -K @ X

    X_dot = A @ X + B @ u

    X = X + X_dot * dt

    time_history.append(t)
    theta_history.append(np.degrees(X[2, 0]))

# ====================================
# SAVE GRAPH
# ====================================

os.makedirs("images/day7", exist_ok=True)

plt.figure(figsize=(10, 5))
plt.plot(time_history, theta_history, linewidth=2)

plt.title("LQR Controller Response")
plt.xlabel("Time (s)")
plt.ylabel("Angle (deg)")
plt.grid(True)

plt.savefig(
    "images/day7/lqr_controller.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("\nSaved:")
print("images/day7/lqr_controller.png")