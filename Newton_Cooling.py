
# NEWTON'S LAW OF COOLING USING EULER METHOD #
import numpy as np
import matplotlib.pyplot as plt

plot_t=[]
plot_y=[]
y_analy=[]

def euler(f,y0,a,b,h):
    t,y=a,y0
    while t<=b:
        plot_t.append(t)
        plot_y.append(y)
        t=t+h
        y=y+h*f(y,t)
T_a=float(input("Enter the ambiant Temperature(°C):")) #T_a=20.0
T_0=float(input("Enter initial temperature(°C):"))     #t_0=100.0
x_0=int(input("Enter initial time(sec):"))             #x_0=0
x_f=int(input("Enter required time(sec):"))            #x_f=50

        
def cooling(temp,time):
    return -0.07*(temp-T_a)
euler(cooling,T_0,x_0,x_f,1)

for i in range(0,x_f,1):
    y_analy.append(T_a+(T_0-T_a)*np.exp(-0.07*i))
    
plt.plot(plot_t,plot_y,marker='.',label='euler')
plt.plot(y_analy,'r--',label='exact')
plt.title('Newton Law of Cooling')
plt.xlabel('Time(sec)')
plt.ylabel('Temperature(°C)')
plt.grid()
plt.legend(loc='best')
plt.show()
    
