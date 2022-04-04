# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 12:16:42 2022

@author: Sem
"""

import numpy as np

import matplotlib.pyplot as plt

nterms = 10

# an = a_{n-1} + v -> v = 10, a_0 = 4
# ak = vk + a_0 -> v = 10, a_0 = 4
# bn = rb_{n-1} -> r_0 = 0.2, b_0 = 1
# bk = a_0 r^k -> r_0 = 0.2, b_0 = 1

# rekenkundige reeks alles +20
# meetkundige reeks verkleint 25 keer zo snel

def rekenkundig(n, v=10, a0=4):
    """Retourneert 1e n termen van rekenkundige rij met beginwaarde 
    a0 en richtingscoëfficient v"""    
    x = np.array([a0],dtype=int)
    for i in range(1,n):
        new_x = v+x[i-1]
        x=np.append(x,new_x)
    return x
def meetkundig(n, b=1, r=0.2):
    """Genereert een eindige rij b(k) van n+1 termen met b(k)=b0*r^k"""
    x = np.array([b],dtype=int)
    for i in range(1,n):
        new_x = r*x[i-1]
        x=np.append(x,new_x)
    return x


print(rekenkundig(10))
print(meetkundig(10))

nlist = np.arange(1,nterms+1)

fig = plt.figure()
ax = plt.axes()

plt.grid()


plt.plot(nlist, rekenkundig(nterms), 'o', color='red');
plt.plot(nlist, meetkundig(nterms), 'x', color='blue');

plt.xlabel('n')
plt.ylabel('$a_n$')

plt.legend(['a', 'b'])
plt.suptitle('Eindige en oneindige rijen')
plt.show()