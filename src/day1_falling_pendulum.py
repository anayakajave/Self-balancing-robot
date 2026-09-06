import numpy as np
import matplotlib.pyplot as plt

dt = 0.01
total_time = 5

theta = 0.1
omega = 0

g = 9.81
L = 0.5

time_data = []
theta_data = []

for t in np.arange(0, total_time, dt):

    alpha = (g / L) * np.sin(theta)

    omega = omega + alpha * dt

    theta = theta + omega * dt

    time_data.append(t)
    theta_data.append(theta)

plt.plot(time_data, theta_data)

plt.title("Falling Inverted Pendulum")

plt.xlabel("Time (seconds)")
plt.ylabel("Angle (radians)")

plt.grid(True)

plt.show()