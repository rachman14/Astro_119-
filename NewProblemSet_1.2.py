# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 19:46:24 2019

@author: eric_
"""
import math
def summation(n):
    total = 0.
    for i in range(n+1):
        term = 8./((4.*i+1.)*(4.*i+3.))
        total = total + term
    print(total)
    return total
error = summation(10) - math.pi
print("Error: ", error)