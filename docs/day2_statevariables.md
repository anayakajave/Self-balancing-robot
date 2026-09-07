# Day 2.1 - State Variables

## Objective

Understand what state variables are and why they are important in a self-balancing robot.

---

## What is a State Variable?

A state variable is the minimum information required to completely describe the current condition of a system and predict its future behavior.

---

## State Variables of an Inverted Pendulum

For a pendulum:

x₁ = θ = Angle

x₂ = ω = Angular Velocity

Together:

State = [θ, ω]

---

## Why Angle Alone Is Not Enough

Example:

Pendulum A:
Angle = 20°
Velocity = 0

Pendulum B:
Angle = 20°
Velocity = -50°/s

Both pendulums have the same angle but different future behavior.

Therefore angle alone cannot completely describe the system.

---

## Connection to Self-Balancing Robots

A balancing robot continuously estimates:

- Angle (θ)
- Angular Velocity (ω)

These values are used by the controller to decide how the motors should move.

---

## Key Learning

State variables provide a mathematical way to describe the condition of a dynamic system.

For an inverted pendulum, angle and angular velocity are sufficient to describe the system state.