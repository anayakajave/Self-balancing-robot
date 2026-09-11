# Day 3.2 - Proportional Control

## Objective

Understand how a proportional controller generates corrective action.

## Control Law

u = Kp × e

where:

u = controller output

Kp = proportional gain

e = error

## Physical Meaning

Small error → Small correction

Large error → Large correction

## Effect of Kp

Low Kp:
- Slow response
- Weak correction

High Kp:
- Fast response
- Strong correction

Very High Kp:
- Overshoot
- Oscillations
- Instability

## Connection to Self-Balancing Robot

The controller output eventually becomes a motor command that moves the wheels to reduce tilt.

## Key Learning

A proportional controller generates correction proportional to the current error.