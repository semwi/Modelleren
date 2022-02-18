# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 16:44:47 2022

@author: Sem
"""
# Vul deze code aan voor opgave 3

import numpy as np
import matplotlib.pyplot as plt

def random(a=-1,b=1,size=None):
    ''' Geeft een random getal terug in het interval [a,b)
    
        argumenten:
            a: linker grens interval (inclusief)
            b: rechter grens interval (exclusief)
            size: vorm van ndarray, bij None een enkele float
            
        teruggave:
            enkele float of ndarray met random getallen.
    '''
    return (b-a)*np.random.random(size)+a

def v(t):
    offset = 1+random()
    helling = random()*3
    y = offset+t*(helling+random()/10) + random(size=len(t))/2
    return y

print(v(2))
# tijdstip waarop gemeten is
t = np.linspace(0,4,210)

# theoretische offset
offset = 1+random()
# theoretische helling
helling = random()*3

# gemeten snelheid
v = offset+t*(helling+random()/10) + random(size=len(t))/2

# error in snelheid
v_err = random(a=min(v),b=max(v),size=len(t))/5

## Hier komt de rest van je code 

plt.plot(v(t),t)
plt.show()