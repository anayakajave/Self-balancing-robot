import numpy as np
import matplotlib.pyplot as plt
import os

# ====================================
# SIMULATION SETTINGS
# ====================================

dt = 0.01
T = 10

time = np.arange(0, T, dt)

# ====================================
# TRUE ANGLE
# ====================================

true_angle = 15 * np.sin(0.8 * time)

# ====================================
# ACCELEROMETER (NOISY)
# ====================================

np.random.seed(42)

acc_angle = (
    true_angle
    + np.random.normal(0, 2, len(time))
)

# ====================================
# GYROSCOPE (DRIFTING)
# ====================================

gyro_rate = np.gradient(true_angle, dt)

drift = 0.2  # deg/s bias

gyro_angle = np.zeros(len(time))

for i in range(1, len(time)):
    gyro_angle[i] = (
        gyro_angle[i - 1]
        + (gyro_rate[i] + drift) * dt
    )

# ====================================
# COMPLEMENTARY FILTER
# ====================================

fused_angle = np.zeros(len(time))

alpha = 0.98

for i in range(1, len(time)):

    prediction = (
        fused_angle[i - 1]
        + (gyro_rate[i] + drift) * dt
    )

    fused_angle[i] = (
        alpha * prediction
        + (1 - alpha) * acc_angle[i]
    )

# ====================================
# CREATE FOLDER
# ====================================

os.makedirs(
    "images/day9",
    exist_ok=True
)

# ====================================
# GRAPH
# ====================================

plt.figure(figsize=(12, 6))

plt.plot(
    time,
    true_angle,
    linewidth=3,
    label="True Angle"
)

plt.plot(
    time,
    acc_angle,
    alpha=0.5,
    label="Accelerometer (Noisy)"
)

plt.plot(
    time,
    gyro_angle,
    linewidth=2,
    label="Gyroscope (Drifting)"
)

plt.plot(
    time,
    fused_angle,
    linewidth=3,
    label="Sensor Fusion"
)

plt.title("MPU6050 Sensor Fusion")
plt.xlabel("Time (s)")
plt.ylabel("Angle (deg)")
plt.grid(True)
plt.legend()

# ====================================
# SAVE IMAGE
# ====================================

plt.savefig(
    "images/day9/sensor_fusion.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("\nSaved:")
print("images/day9/sensor_fusion.png")