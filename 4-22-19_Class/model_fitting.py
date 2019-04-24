# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 08:57:26 2019
Model fitting of Least Squares

pre-made model on canvas called opt_utils.py
use function called lin_LS
@author: eric_
"""
import numpy as np
import matplotlib.pyplot as plt
import opt_utils
np.random.seed(12345)

#===========================================================
#               function definition
#===========================================================

#===========================================================
#               parameters, files
#===========================================================
xmin, xmax = 0, 5
N = 20 #number of observations
f_a = 5.0
f_b = -2.4
f_sigma = .5 #width of Gaussian

#===========================================================
#               synthetic data
#===========================================================
a_x = np.linspace(xmin, xmax, N)
a_y = f_b * a_x + f_a + np.random.randn(N)*f_sigma

#===========================================================
#           lin. LS. and plot
#===========================================================
dLS = opt_utils.lin_LS(a_x, a_y)

plt.figure(1)
plt.title(str(dLS['R2']))
ax1 = plt.subplot(211)
ax1.plot(a_x, a_y, 'ko', ms = 5, mew = 1.5, mfc = 'none', label = 'Obs.')
ax1.plot(a_x, dLS['Y_hat'], 'r-', label = 'Model')
ax1.legend(loc = 'upper right')
plt.show()










