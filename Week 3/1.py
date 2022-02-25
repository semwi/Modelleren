# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 11:34:13 2022

@author: Sem
"""

import numpy as np

A = np.array([[-1,-1],[-8,-7]])
B = np.array([[1,2],[1,4]])
C = np.array([[1,1],[1,1]])

print(np.linalg.det(A))
print(np.linalg.det(B))
print(np.linalg.det(C))