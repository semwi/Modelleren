# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 12:37:50 2022

@author: Sem
"""

import numpy as np
import functies as f

#print(f.rekenkundig(10))
#print(f.meetkundig(10))

C = np.array([1,0.5,0.25,0.125],dtype=int)

def rij_partiele_sommen(array1):
    a = array1
    x = np.array([])
    for i in range((len(array1))):
        s_i = (1-a[i]**i)/(i-a[i])*a[0]
        x = np.append(x, s_i)
    return x

print(C)
print(rij_partiele_sommen(C))