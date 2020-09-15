# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 13:01:10 2020

@author: iamsa
"""


import numpy as np
import matplotlib.pyplot as plt

def f(x,y):
    return x+y

a=0.0
b=1.0
y=1.0
x=a
h=0.01
N=(b-a)/h

for i in range(int(N)):
    y=y+h*f(x,y)
    x=x+h
    
print(y)    
