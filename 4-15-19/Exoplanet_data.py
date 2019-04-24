# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 08:17:09 2019

@author: eric_
"""

import numpy as np
import matplotlib.pyplot as plt

#################################################################
#           files and variables
#################################################################
file_in = 'exoplanet_transit.csv'

r_s = 80*1e3 #km
Np = 3

#####################################################################
#               load data
#####################################################################
mData = np.loadtxt(file_in, delimiter = ", ", skiprows = 1).T #transpose of data matrix
N = len(mData[0])
lenPer = int(float(N)/Np)
#compute difference between subsequent samples
aDiff = mData[1][1::] - mData[1][0:-1]



#####################################################################
#               compute depth of transit
#####################################################################
aDepth = np.zeros(lenPer)
for i in range(Np):
    #create index vector
    aID = np.arange(lenPer) + lenPer*i
    selMin = aDiff[aID] == aDiff[aID].min()
    selMax = aDiff[aID] == aDiff[aID].max()
    
    iID_min = aID[selMin][0]
    iID_max = aID[selMax][0]
    
    #compute mean depth of transit (for each period)
    
    aDepth[i] = 1 - mData[1, iID_min:iID_max].mean()
    
#computer size of planet
aR_p = np.sqrt( aDepth)*r_s
print("Radius = ", aR_p)


######################################################################
#               plotting
######################################################################
plt.figure(1)
plt.subplot(211)
plt.plot(mData[0], mData[1], 'ko', ms = 1)
plt.subplot(212)
plt.plot(mData[0][0:-1], 'ro', ms = 10)
plt.xlabel("Transit Time [hr]")
plt.ylabel("Brightness")
plt.show()



