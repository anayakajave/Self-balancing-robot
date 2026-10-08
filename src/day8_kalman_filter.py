import numpy as np
import matplotlib.pyplot as plt
import os

# ====================================
# SIMULATION SETTINGS
# ====================================

dt = 0.1
T = 10

# ====================================
# TRUE ANGLE
# ====================================

time = np.arange(0, T, dt)

true_angle = 10 * np.sin(0.5 * time)

# ====================================
# NOISY SENSOR
# ====================================

np.random.seed(42)

sensor_angle = true_angle + np.random.normal(
    0,
    2,
    len(time)
)

# ====================================
# SIMPLE KALMAN FILTER
# ====================================

estimate = 0

P = 1
Q = 0.01
R = 4

kalman_history = []

for measurement in sensor_angle:

    # Prediction

    P = P + Q

    # Kalman Gain

    K = P / (P + R)

    # Correction

    estimate = estimate + K * (
        measurement - estimate
    )

    P = (1 - K) * P

    kalman_history.append(estimate)

# ====================================
# SAVE IMAGE
# ====================================

os.makedirs(
    "images/day8",
    exist_ok=True
)

plt.figure(figsize=(12,6))

plt.plot(
    time,
    true_angle,
    label="True Angle",
    linewidth=3
)

plt.plot(
    time,
    sensor_angle,
    label="Noisy Sensor",
    alpha=0.6
)

plt.plot(
    time,
    kalman_history,
    label="Kalman Estimate",
    linewidth=3
)

plt.title("Kalman Filter Angle Estimation")
plt.xlabel("Time (s)")
plt.ylabel("Angle (deg)")
plt.grid(True)
plt.legend()

plt.savefig(
    "images/day8/kalman_filter.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("Saved:")
print("images/day8/kalman_filter.png")