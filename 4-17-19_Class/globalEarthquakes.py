# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 08:54:19 2019
Animation of global eartquake locations from 2000 to 2019
    -plotted annually
@author: eric_
"""
import numpy as np
import matplotlib.pyplot as plt
#from mpl_toolkits.basemap import Basemap as Basemap
#=========================================
#           file and parameters
#=========================================
file_eq = 'globalEqs.txt'

#=========================================
#           load data
#=========================================
aYr = np.genfromtxt(file_eq, skip_header = 1, 
                    usecols = (0), delimiter = "-", dtype = int) #time vector
print(np.unique(aYr))
mLoc = np.genfromtxt(file_eq, skip_header = 1, delimiter = ",", usecols = (2, 1), 
                     dtype = float).T




#========================================
#           plot eq data using basemap
#========================================
for it in np.unique(aYr):
    sel_eq = it == aYr
    print("no. of eqs. in ", it, sel_eq.sum())
    plt.figure(1)
    plt.title(str(it))
    m = Basemap()
    
    a_X, a_Y = m(mLoc[0], mLoc[1])
    
    plt.plot(a_X, a_Y)
    
    plt.pause(.5)