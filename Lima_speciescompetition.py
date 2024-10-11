# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 02:26:52 2024

@author: dell
"""

import numpy as np
import matplotlib.pyplot as plt

# Parameters
r1 = 1.5      # Growth rate of species 1
r2 = 1.25     # Growth rate of species 2
S1 = 0.4      # Diminishing rate due to species 2
S2 = 0.4      # Diminishing rate due to species 1

# Initial populations
x0 = 10   # Initial population of species 1
y0 = 10    # Initial population of species 2

# Time steps
n_steps = 10

# Arrays to store populations over time
x = np.zeros(n_steps)
y = np.zeros(n_steps)

# Initial conditions
x[0] = x0
y[0] = y0

# Difference equations for species 1 and 2
for n in range(n_steps - 1):
    x[n+1] = r1 * x[n] - S1 * y[n] 
    y[n+1] = r2 * y[n] - S2 * x[n] 

# Plotting the population of species over time(steps)
plt.figure(figsize=(10, 6))
plt.plot(x, label="Species 1 (x)", color="blue")
plt.plot(y, label="Species 2 (y)", color="green")
plt.axhline(y=0, color='blue', linestyle='--', label="Steady-state x*")
plt.axhline(y=0, color='green', linestyle='--', label="Steady-state y*")
plt.title("Linear Competition Model without Immigration and Migration")
plt.xlabel("Time steps")
plt.ylabel("Population size")
plt.legend()
plt.grid(True)
plt.show()

print(x)
print(y)

