# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 11:55:11 2022

@author: Sem
"""

import numpy as np
import matplotlib.pyplot as plt
import rijen

nterms = 10

# Hier definieer je het domein. Gebruik hier niet linspace, want het domein van een functie 
# van een rij wordt gegeven door de natuurlijke getallen 0,1,2,3,... niet ertussen!
nlist = np.arange(1,nterms+1)

fig = plt.figure()
ax = plt.axes()

plt.grid()


plt.plot(nlist, rijen.bn(nterms), 'o', color='red');
plt.plot([1,4,3,-9,0,0.25], 'x', color='blue');

plt.xlabel('n')
plt.ylabel('$a_n$')

plt.legend(['Oneindige rij', 'Eindige rij'])
plt.suptitle('Eindige en oneindige rijen')
plt.show()
