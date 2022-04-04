# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 12:00:03 2022

@author: Sem
"""

import numpy as np
import matplotlib.pyplot as plt

def meetkundig(n,b=2,r=0.5):
    """functie die de eerste n termen van de rij a_k=br^k retourneert. 
    Hierin zijn b = 2 en r=0.5 optionele argumenten."""
    """Genereert een eindige rij b(k) van n+1 termen met b(k)=b0*r^k"""
    x = np.array([b],dtype=int)
    for i in range(1,n):
        new_x = r*x[i-1]
        x=np.append(x,new_x)
    return x

print(meetkundig(10))

nterms = 10

# Hier definieer je het domein. Gebruik hier niet linspace, want het domein van een functie 
# van een rij wordt gegeven door de natuurlijke getallen 0,1,2,3,... niet ertussen!
nlist = np.arange(1,nterms+1)

fig = plt.figure()
ax = plt.axes()

plt.grid()


plt.plot(nlist, meetkundig(nterms), 'o', color='red');
plt.xlabel('n')
plt.ylabel('$a_n$')

plt.legend(['Oneindige rij', 'Eindige rij'])
plt.suptitle('Eindige en oneindige rijen')
plt.show()
