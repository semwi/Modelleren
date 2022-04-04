# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 13:07:52 2022

@author: Sem
"""

# import the necessary modules
import numpy as np
import matplotlib.pyplot as plt
from cycler import cycler


plt.ioff()    # this stops the graphs from overwriting each other

# allows us to compute factorials 
import math

def approx_e(x,n):
    """Genereert de ne orde Taylorpolynoom van e^x rond x=0"""
    # intialize the array of  yvals
    yvals = np.zeros([n,len(x)])

    for k in range(n):
        # special case for 0th order
        if k == 0:
            yvals[k,:] = np.ones(len(x))
      
        # otherwise nth order is n-1th order plus new term
        else:
            new_term = x**k / math.factorial(k)
            yvals[k,:] = yvals[k-1,:] + new_term
    return yvals

# max number of terms we want to expand to
nterms = 5

# range of x and y values to look at
xvals = np.linspace(-2,2,200)
yvals = approx_e(xvals,nterms)

fig = plt.figure()
ax = plt.axes()
plt.grid()


cc = cycler(color=list('bkrgcmy'))

plt.rc('lines', linewidth=1, linestyle = '--')
plt.rc('axes', prop_cycle=cc)

# loop through number of terms and plot
for n in range(nterms):
    label = r"$P_{n}(x)$"
    plt.plot(xvals,yvals[n,:], label=label, linewidth=1)
    
# plot the real function  
plt.plot(xvals, np.exp(xvals), label="$e^x$", linewidth=2.0, linestyle='solid')
plt.xlabel("x")
plt.ylabel("y")
plt.xlim([-2,2]) 
plt.ylim([-1,6]) # set y-axis to make it easier to see
plt.legend()
plt.show()