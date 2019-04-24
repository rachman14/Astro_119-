# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 08:07:56 2019
Compute temporal earthquake rate change for KTB fluid injection experiment

@author: eric_
"""

import numpy as np
import matplotlib.pyplot as plt

#===========================================================
#               define functions
#===========================================================
def comp_rate(a_t, k):
    """
    -compute rate change for time vector a_t
    :input
        a_t - time vector
        k - sample window - controls smoothness
    :output a_bin, a_rate
    """
    aS = np.arange(0, a_t.shape[0]-k, 1)
    a_bin = np.zeros(aS.shape[0])
    a_rate = np.zeros(aS.shape[0])
    iS = 0
    for s_step in aS:
        i1, i2 = s_step, s_step+k
        a_rate[iS] = k/(a_t[i2] - a_t[i1])
        a_bin[iS] = 0.5*(a_t[i1] + a_t[i2])
        iS += 1
    return a_bin, a_rate

#========================================================================
#                   parameters and files
#========================================================================
file_in = 'KTB_inject.txt'
file_eq = 'KTB_mag.txt'

#sample window
k_win = 10

t0 = float() #starting time for plotting
aT_eq = np.array([]) #timing of the earthquakes
aT_Mag = np.array([])

aT_inj = np.array([])
aV = np.array([])

#----------------------------------------------------
#                   load data and computation rates
#===================================================



mData = np.loadtxt(file_eq).T
aT_eq = mData[0]
aMag = mData[1]

mData = np.loadtxt(file_in).T
aT_inj = mData[3]
aV = mData[4]





sel = aV > 0 #gets rid of the zeros
aV = aV[sel]
aT_inj = aT_inj[sel]

### compute eq rates
a_tbin, a_rate = comp_rate(aT_eq, k_win)

### test plot of magnitudes
plt.figure()
ax1 = plt.subplot(211)
ax1.plot(aT_eq, aV, 'b-')
ax2 = plt.subplot(212)
ax2.plot(a_tbin, a_rate, 'ko')
ax2.set_xlim(ax1.get_xlim())
plt.show()




