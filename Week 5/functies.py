# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 12:39:18 2022

@author: Sem
"""

import numpy as np

def rekenkundig(n, v=10, a0=4):
    """Retourneert 1e n termen van rekenkundige rij met beginwaarde 
    a0 en richtingscoëfficient v"""    
    x = np.array([a0],dtype=int)
    for i in range(1,n):
        new_x = v+x[i-1]
        x=np.append(x,new_x)
    return x
def meetkundig(n, b=2, r=0.5):
    """Genereert een eindige rij b(k) van n+1 termen met b(k)=b0*r^k"""
    x = np.array([b],dtype=int)
    for i in range(1,n):
        new_x = r*x[i-1]
        x=np.append(x,new_x)
    return x