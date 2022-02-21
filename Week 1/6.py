# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 16:54:27 2022

@author: Sem
"""

from sympy import *
x, y, z = symbols('x y z')
init_printing(use_unicode=True)

F = atan(2*x) +  exp(x/3)
dF = diff(F, x)
print(diff(dF, x))

A = (6*x)*sqrt(16+(x**2))
print(integrate(A, (x,0,3)))

B = x*cos(2*x)
print(integrate(B))

C = x/(sqrt(1+2*x))
print(integrate(C))

# kan nergens de rest vinden