# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 13:09:20 2020

@author: iamsa
"""


import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def f(x,y):
    return x+y

y0=1.0
x=np.linspace(0,1,10)

y=odeint(f,y0,x)
print(y[(len(y)-1)])
#len(y)-1 means value of y[9] in the array  