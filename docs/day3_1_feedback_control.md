# Day 3.1 - Feedback Control

## Objective

Understand how a self-balancing robot uses feedback to maintain balance.

## Open Loop System

An open-loop system does not measure its output.

Example:

Push Robot
↓
Robot Falls
↓
No Correction

## Closed Loop System

A closed-loop system continuously measures its output and applies corrections.

Example:

Push Robot
↓
Measure Angle
↓
Calculate Error
↓
Move Wheels
↓
Correct Tilt

## Error Equation

Error = Desired - Actual

For a balancing robot:

e = 0 - θ

where:

θ = current robot angle

## Why Feedback Is Important

Feedback allows the robot to continuously reduce error and maintain balance even when disturbances occur.

## Key Learning

A self-balancing robot is a closed-loop control system.