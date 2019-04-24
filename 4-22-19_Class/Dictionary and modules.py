# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 08:11:22 2019

@author: eric_
"""
import numpy as np
Dictionary = {'my_pi':np.pi, 
              'my_array' : np.arange(10)}

print(Dictionary['my_pi'])
print(Dictionary) 
for i in Dictionary:
    print(type(Dictionary[i]))
    
    
#importing my own modules
puzzle = _import_('4-17-19_Class.3_4_KTB_rates-1')
