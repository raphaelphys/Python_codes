# -*- coding: utf-8 -*-
"""
Created on Fri May 15 21:13:56 2015

@author: Razib
"""
import numpy as np
import matplotlib.pyplot as plt

#Creating a function for the circle
#The idea is to take a point from a 
#psedorandom number generator and check
#whether it falls within the circle
def circle(x,y):
    if (x**2 + y**2) <=1:
        bullseye = 1
    else: bullseye = 0
    return bullseye
    
def main(nIter=10**8):
    bEye=0
    for n in range(nIter):
        x = np.random.uniform(0,1)
        y = np.random.uniform(0,1)
        bEye +=circle(x,y)
    PPi=4*(bEye/nIter)
    #print(PPi)
    return PPi

piBucket=[]
for x in range(100):
    piBucket.append(main())
    
print(np.average(piBucket))
plt.hist(piBucket)
plt.show()