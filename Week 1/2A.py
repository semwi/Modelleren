# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 14:45:10 2022

@author: Sem
"""

import numpy as np


def sinc(x): 
    '''Functie volgens voorschrift, zowel input (x) als output (sinc) zijn numpy arrays'''
    return list(map(lambda a: 1 if a ==0 else np.sin(a)/a, x))