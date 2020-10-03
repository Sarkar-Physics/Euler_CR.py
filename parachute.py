# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 12:44:54 2020

@author: iamsa
"""

import matplotlib.pyplot as plt

vp=[]
tp=[]

t=0
v=0.0
b=0.25
m=50.0
v2=0
t2=0
tf=20
while(t<=tf):
    prev_v=v
    h=0.1
    v=v+h*(9.8-(b/m)*v**2)
    t=t+h
    new_v=v
    vp.append(v)
    tp.append(t)
    if(new_v-prev_v<=0.001):
         h=0.001
         v2=new_v
         t2=t
         break

print("Terminal velocity(m/s):",v2,"is attained at time(sec):",t2)
while(t2<=tf):
    h=0.001
    b=500
    v2=v2+h*(9.8-(b/m)*v2**2)
    t2=t2+h
    new_v=v
    vp.append(v2)
    tp.append(t2)
    

plt.plot(tp,vp)
plt.title("Dropping from parachute")
plt.xlabel('time(sec)')
plt.ylabel('velocity(m/s)')
plt.grid()
plt.show()    
    
    