# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 14:45:59 2022

@author: Sem
"""

import matplotlib.pyplot as plt
import numpy as np


def sinc(x): 
    '''Functie volgens voorschrift, zowel input (x) als output (sinc) zijn numpy arrays'''
    return list(map(lambda a: 1 if a ==0 else np.sin(a)/a, x))
plt.plot(np.linspace(-10,10,973), sinc(np.linspace(-10,10,973)))

#plt.plot(np.linspace((np.pi)*-1,np.pi,973), sinc(np.linspace((np.pi)*-1,np.pi,973)))

#plt.plot(np.linspace(1000,1000000000,23), sinc(np.linspace(1000,1000000000,23)))
#plt.xscale('log')

plt.show()