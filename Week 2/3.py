# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 11:18:31 2022

@author: Sem
"""

import numpy as np

C = np.array([[3,2],[4,5]])

print('C*C: ', C*C) # is dit correct als je C*D als matrix vermenigvuldiging wilt uitrekenen?

print(np.linalg.det(C))