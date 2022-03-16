# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 13:53:12 2022

@author: Sem
"""

from scipy import optimize

def f(x):
    return (x**2 - 1)

# 4*pi*N*(((m)/(2*pi*k*T)**(3/2))*(v**2)*(exp**((m*(v**2))/(2*k*T)))
x = optimize.bisect(f, 0, 2)

print(x)