# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 11:42:08 2022

@author: Sem
"""

import numpy as np

A = np.array([[2,-1,3],[1,1,-1],[5,-3,1]])
A_inv = np.linalg.inv(A)
A_det = np.linalg.det(A)
print(A)
print(A_det)
print(A_inv)