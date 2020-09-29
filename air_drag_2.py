# freefall when drag force is proportional to v^2 with initial velocity 0 #

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import math

plot_t=[]
plot_v=[]

def euler(f,v0,t0,tf,h):
    t,v=t0,v0
    while t<=tf:
        plot_t.append(t)
        plot_v.append(v)
        t=t+h
        v=v+h*f(v,t)
 
b=float(input("Enter the drag coefficient(kg/m):"))
m=float(input("Enter the mass of the object(kg):"))
g=float(input("Enter the value of g(m/s^2):"))
v0=float(input("Enter initial velocity(m/s):"))
t0=float(input("Enter initial time(sec):"))
tf=float(input("Enter final time(sec):"))   
h=0.001  
def f(v,t):
    g=9.8
    dvdt=g-(b/m)*v**2
    return dvdt

euler(f,v0,t0,tf,h)
#using odient
#t=np.linspace(0,tf)
#y=odeint(f,v0,t)
###

#for analytical part
v_analy=[]
time=[]
v_t=math.sqrt((m*g)/b)
T=math.sqrt(m/(g*b))
#v_t=44.27
#T=4.51
v=v0
i=t0
h=0.1
while i<=tf:
    v_analy.append(v)
    time.append(i)
    v=v_t*np.tanh(i/T)
    i=i+h


#graph plotting
    
plt.plot(plot_t,plot_v,'r--',label="velocity plot in air ressistive medium")
plt.plot(time,v_analy,label="exact")
plt.title("Free Fall considering air drag proportional to v^2")
plt.xlabel('time(sec)')
plt.ylabel('velocity(m/s)')
plt.legend()
plt.grid()
plt.show()
