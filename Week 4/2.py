# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 16:29:53 2022

@author: Sem
"""

import numpy as np
import math

degree = 30

# maak matrixes 

v = np.array([[3,2]])

w = v

Rot_tegen_klok = np.array([[math.cos((degree*math.pi)/180),
                            -1*math.sin((degree*math.pi)/180)],
                           [math.sin((degree*math.pi)/180),
                            math.cos((degree*math.pi)/180)]])

x_spiegel = np.array([[1,0],[0,-1]])

# v transformaties

v_1 = np.dot(v, Rot_tegen_klok)

v_trafo = np.dot(v_1, x_spiegel)

# w transformaties

w_1 = np.dot(w, x_spiegel)

w_trafo = np.dot(w_1, Rot_tegen_klok)

