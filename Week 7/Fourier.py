# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 14:56:27 2022

@author: Sem
"""

import sympy as sp
sp.init_printing(use_latex='mathjax') # voor mooie text weergave 
from IPython.display import display # voor mooie text weergave
import matplotlib.pyplot as plt
from TN_code.fourier import fourier_coeff as fc
from sympy import Symbol
t = Symbol('t')
    
f = fc.Heaviside(t+1) - fc.Heaviside(t-1)
T = 4 
N = 50
reeks, a, b = fc.fourreeks(f,T,N)
p=sp.plotting.plot(fc.periodiek(f,T,10), reeks, (t,0,10))
fc.plot_color(p)

plt.subplot(T, fc.fourreeks(f,4,2))

print('De reeksontwikkeling is (tot %d even en oneven termen):' %(N))
display(reeks)