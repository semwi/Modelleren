# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 11:42:15 2022

@author: Sem
"""

import numpy as np

# Willekeurige eindige rij
an = [1,4,3,-9,0,0.25]

# door n steeds groter te maken kun je de oneindige rij simuleren. Het blijft in de computer wiskundig altijd eindig.
def bn(n, r=2, b0=1):
    """Genereert een eindige rij b(k) van n+1 termen met b(k)=b0*r^k"""
    x = np.array([b0],dtype=int)
    for i in range(1,n):
        new_x = r*x[i-1]
        x=np.append(x,new_x)
    return x

def bn_2(n, r=2, b0=1):
    x = [b0]
    for i in range(1, n):
        new_x = r*x[i-1]
        x.append(new_x)
    return x
    

print(bn(10))
print(bn_2(10))