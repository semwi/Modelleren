# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 11:50:51 2022

@author: Sem
"""

import numpy as np

A = np.random.random((15000,15000))
A_inv = np.linalg.inv(A)
print(A_inv)