# freefall when drag force is proportional to velocity #

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def f1(v,t):
    g=9.8
    dvdt=g-a*v
    return dvdt
"""
def f2(v,t):
    g=9.8
    dvdt=g-0.0005*v
    return dvdt
def f3(v,t):
    g=9.8
    dvdt=g-3*v
    return dvdt
"""
a=float(input("Enter the constant:"))
g=float(input("Enter the value of g(m/s^2):"))
v0=float(input("Enter initial velocity(m/s):"))
tf=float(input("Enter final time(sec):"))
t=np.linspace(0,tf)
y1=odeint(f1,v0,t)
#y2=odeint(f2,v0,t)
#y3=odeint(f3,v0,t)

plt.plot(t,y1,label="velocity plot in air ressistive medium for a=1")
#plt.plot(t,y2,label="velocity plot in air ressistive medium for a=2")
#plt.plot(t,y3,label="velocity plot in air ressistive medium for a=3")
plt.title("Free Fall considering air drag proportional to v")
plt.xlabel('time(sec)')
plt.ylabel('velocity(m/s)')
plt.legend()
plt.grid()
plt.show()

'''
y=0
a=0
b=5
x=a
h=0.1
N=int((b-a)/h)
yp=np.zeros(N)
for i in range(N):
    y=y + h*f(x,y)
    x=x+h
    yp[i]=y
'''   

