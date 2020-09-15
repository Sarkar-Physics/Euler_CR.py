
import numpy as np
import matplotlib.pyplot as plt

def f(x,y):
    return (V-y/C)/R

#R=10000.0
#C=1*10E-6 #(0.00001)
#V=5.0
R=float(input("Enter R:"))
C=float(input("Enter C:"))
V=float(input("Enter V:"))
#a=0
#b=1
a=float(input("Enter initial time(in sec):"))
b=float(input("Enter required time(in sec):"))
y=float(input("Enter initial value:"))
x=a
h=0.001

N=int((b-a)/h)
#t=np.linspace(a,b,N)
xp=np.zeros(N) #creates a array of size N with all elements zero
yp=np.zeros(N) # #creates a array of size N with all elements zero
 
for i in range(N):
    y=y+h*f(x,y)
    xp[i]=x
    yp[i]=y/C
    x=x+h

exactp=np.zeros(N)
t=np.linspace(a,b,N)
for i in range(N): 
    exactp[i]=V*(1-np.exp(-(1/(R*C)*i/N)))
       
exact=V*(1-np.exp(-(1/(R*C)*b)))
print("The value of V:",y/C)
print("The exact value at that time :",exact)
plt.plot(xp,yp,label='Euler')
plt.plot(t,exactp,label="Exact")
plt.legend()#label
plt.grid()
plt.xlabel('time(sec)')
plt.ylabel('Vcap(Volt)')
plt.title('Charging of capacitor(Euler Method)') 
plt.show()   

