# Day 2 - State Space Simulation

## Objective

Implement a state-space representation of an inverted pendulum.

## State Variables

θ = Angle

ω = Angular Velocity

## State Equations

θ' = ω

ω' = -(g/L)sin(θ)

## Files

src/day2_state_space.py

## Observation

The pendulum motion was simulated using two state variables and Euler integration.