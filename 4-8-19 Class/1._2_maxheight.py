# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file."""
import numpy as np
import matplotlib.pyplot as plt
v0 = 5 #m/s initial velocity
g = 9.81 #m/s^2 acceleration due to gravity
n = 2000 #time steps
a_t = np.linspace(0, 1, n) #time arrray
y = v0*(a_t) - 0.5*g*(a_t)**2 #kinematic equation

#find max height in while loop
i = 1
while y[i] > y[i-1]:
        largest_height = y[i]
        i += 1

print("max height : ", round(largest_height, 3), "meters")
plt.plot(a_t, y)
plt.show()