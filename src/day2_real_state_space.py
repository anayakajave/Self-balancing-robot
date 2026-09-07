import numpy as np
import matplotlib.pyplot as plt

g = 9.81
L = 1.0

dt = 0.01
T = 10

theta = np.radians(10)
omega = 0

theta_history = []
omega_history = []
time_history = []

t = 0

while t < T:

    theta_dot = omega

    omega_dot = (g / L) * np.sin(theta)

    theta = theta + theta_dot * dt
    omega = omega + omega_dot * dt

    theta_history.append(np.degrees(theta))
    omega_history.append(omega)
    time_history.append(t)

    t += dt

plt.figure(figsize=(10,6))

plt.subplot(2,1,1)
plt.plot(time_history, theta_history)
plt.title("Real State Space Dynamics")
plt.ylabel("Angle (deg)")
plt.grid()

plt.subplot(2,1,2)
plt.plot(time_history, omega_history)
plt.ylabel("Angular Velocity")
plt.xlabel("Time (s)")
plt.grid()

plt.tight_layout()

plt.savefig("images/day2/real_state_space.png")

plt.show()