# Day 2B - Real State Space Dynamics

## Objective

Simulate an inverted pendulum using state-space equations.

## State Variables

x1 = Angle (theta)

x2 = Angular Velocity (omega)

## State Equations

d(theta)/dt = omega

d(omega)/dt = (g/L) * sin(theta)

## Parameters

Gravity = 9.81 m/s²

Pendulum Length = 1 m

Time Step = 0.01 s

Simulation Time = 10 s

## Results

The angle increased continuously and exceeded 2000 degrees.

Angular velocity also increased over time.

## Observations

The system is unstable.

Gravity pushes the inverted pendulum away from equilibrium.

Without a controller the pendulum falls and cannot balance itself.

## Learning Outcome

State-space models can represent the dynamics of robotic systems using a set of state variables and differential equations.