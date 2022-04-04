# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 17:08:20 2022

@author: Sem
"""

import numpy as np
import math


# noteer de gegevens
graden_tegen_klok = 30
graden_met_klok = 15

t_x = 3
t_y = 2

v = np.array([[3,2]])

# maak matrixes voor transformatie
verplaatsen = np.array([[1, 0, t_x],[0, 1, t_y], [0,0,1]])
rot_tegen_klok = np.array([[math.cos((graden_tegen_klok*math.pi)/180),
                            -1*math.sin((graden_tegen_klok*math.pi)/180)],
                           [math.sin((graden_tegen_klok*math.pi)/180),
                            math.cos((graden_tegen_klok*math.pi)/180)]])

rot_met_klok = np.array([[math.cos((graden_met_klok*math.pi)/180),
                            math.sin((graden_met_klok*math.pi)/180)],
                           [-1*math.sin((graden_met_klok*math.pi)/180),
                            math.cos((graden_met_klok*math.pi)/180)]])

y_spiegel = np.array([[-1, 0],[0, 1]])

# v transformaties

v_1 = np.dot(v, rot_tegen_klok)
print(v_1)
v_2 = np.dot(v_1.reshape((2,1)), verplaatsen.reshape((2,2)))
v_3 = np.dot(v_2, y_spiegel)
v_trafo = np.dot(v_3, rot_met_klok)
