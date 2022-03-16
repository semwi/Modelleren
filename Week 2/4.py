# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 12:38:22 2022

@author: Sem
"""

import numpy as np

x1 = [4]

a2 = np.array([[2, 3], [4, 9]])
b2 = np.array([6, 15])

a3 = np.array([[2, 1, 4, 1], [3, 4, -1, -1],[1,-4,1,5],[2,-2,1,3]])
b3 = np.array([-4, 3, 9, 7])

x2 = np.linalg.solve(a2, b2)
x3 = np.linalg.solve(a3, b3)


print("x2 is: ", x2)
print("x2 is: ", x3)