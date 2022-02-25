# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 11:34:13 2022

@author: Sem
"""

import numpy as np

A = np.array([[-1,-1],[-8,-7]])
B = np.array([[1,2],[1,4]])
C = np.array([[1,1],[1,1]])

A_inv = np.linalg.inv(A)
B_inv = np.linalg.inv(B)
C_inv = C

print(A_inv)
print(B_inv)
print(C)
