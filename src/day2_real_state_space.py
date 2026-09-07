import numpy as np
import matplotlib.pyplot as plt

# =====================================
# SYSTEM PARAMETERS
# =====================================

g = 9.81      # Gravity (m/s^2)
L = 1.0       # Pendulum length (m)

# =====================================
# SIMULATION SETTINGS
# =====================================

dt = 0.01     # Time step
T = 10        # Total simulation time

# =====================================
# INITIAL CONDITIONS
# =====================================

theta = np.radians(10)   # Initial angle = 10 degrees
omega = 0.0              # Initial angular velocity

# =====================================
# DATA STORAGE
# =====================================

theta_history = []
omega_history = []
time_history = []

# =====================================
# SIMULATION LOOP
# =====================================

t = 0

while t < T:

    # State equations

    theta_dot = omega

    omega_dot = (g / L) * np.sin(theta)

    # Euler Integration

    theta = theta + theta_dot * dt
    omega = omega + omega_dot * dt

    # Store data

    theta_history.append(np.degrees(theta))
    omega_history.append(omega)
    time_history.append(t)

    t += dt

# =====================================
# STATE VARIABLES PLOT
# =====================================

plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.plot(time_history, theta_history)
plt.title("Real State Space Dynamics")
plt.ylabel("Angle (deg)")
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(time_history, omega_history)
plt.ylabel("Angular Velocity (rad/s)")
plt.xlabel("Time (s)")
plt.grid(True)

plt.tight_layout()

plt.savefig(
    "images/day2/real_state_space.png",
    dpi=300,
    bbox_inches="tight"
)
plt.savefig(
    "images/day2/phase_portrait.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()

# =====================================
# PHASE PORTRAIT
# =====================================

plt.figure(figsize=(8, 6))

plt.plot(theta_history, omega_history)

plt.title("Phase Portrait")
plt.xlabel("Angle (deg)")
plt.ylabel("Angular Velocity (rad/s)")
plt.grid(True)

plt.savefig(
    "images/day2/phase_portrait.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()