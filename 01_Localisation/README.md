# Localisation summary
Localisation is robot locating itself in an environment.

First it senses the environment and calculates probability of its location in the environment.

Then it moves as commanded and updates its probability.

Mainly created 2 commands sense and move.

## Sense
Sense multiplies pHit when measurement and the environment are equal and pMiss when they are different.
pHit means that it measures green and the robot is on green.
And the it divides all probability by its sum to normalise it and make total equal to 1 as probability can not be greater than 1. 

## Move
Move function updates the probaility(proability of robot's location in the environment in each point) after the robot has moved. Here, the code is written for when the robot moves right. 
Robot movements are inexact so it can either overshoot or undershoot and their probaility are also take into account.

## Localise
This function gives the location of the robot after multiple movement through the environment in 2D space.

## Probability

0 <= P(x) <= 1

### Total Probabilty Theorem

Given n mutually exclusive events A_1, ..., A_n whose probabilities sum to unity, then

 P(B) = P(B|A_1) * P(A_1) + ... + P(B|A_n) * P(A_n) 

### Baye's Rule

 P(A_i|A) = (P(A_i) * P(A|A_i)) / Σ P(A_j) * P(A|A_j)) 