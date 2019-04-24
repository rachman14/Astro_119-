# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 09:11:04 2019

@author: eric_
"""
import numpy as np

##############################################
#               create ex data
##############################################
file_out = 'dataI0_ex.txt'
N = 10
aX = np.arange(N)
aY = aX**2
print(aY)


###############################################
#               methods to load and save data
###############################################
np.savetxt(file_out, np.array([aX, aY]).T, comments = 'X  X^2')


#read file line by line
with open(file_out, 'r') as file_obj:
    for line in file_obj:
        lStr = line.split(' ')
        print(lStr)