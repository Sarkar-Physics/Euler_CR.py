
"""An object of mass m kg is released from rest from a height
h metre and falls under gravity. Formulate the model and 
nd velocity variation
with time for a period of 5 sec using Euler algorithm. Take time step
as #t = 0:5:
"""

# freefall due to gravity #
import numpy as np
import matplotlib.pyplot as plt

def f(v,t):
    dvdt=g
    return dvdt

g=float(input("Enter the value of g(m/s^2):"))
v_0=float(input("Enter initial velocity(m/s):"))
t_0=float(input("Enter initial time(sec):"))
t_f=float(input("Enter required time(sec):"))
h=float(input("Enter your step:"))
N=int((t_f-t_0)/h)
plot_v=[]
plot_t=[]
v=v_0
t=t_0

for i in range(N):
    plot_v.append(v)
    plot_t.append(t)
    v=v+h*f(v,t)
    t=t+h
 
plt.plot(plot_t,plot_v,marker='.',label='euler')
plt.title("Free fall due to gravity")
plt.xlabel("Time(sec)")
plt.ylabel("Velocity(m/s)")
plt.legend(loc='best') 
plt.grid()
plt.show()  