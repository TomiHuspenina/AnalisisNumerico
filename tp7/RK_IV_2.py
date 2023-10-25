import math
from tabulate import tabulate

a=0
b=4
h=0.5
n=int((a+b)/h)+1
i=0
matriz=[]

def f(x, y):
    return 2*x**3+12*x**2-20*x+8.5

k1=0
k2=0
k3=0
k4=0
x=0
y=1
yaux=y

for i in range(0,n):
    k1=f(x,y)
    k2=f(x+(h/2),y+(h*k1/2))
    k3=f(x+h*0.5,y+h*k2*0.5)
    k4=f(x+h,y+h*k3)

    fila=[i,x,y,k1,k2, k3, k4]
    matriz.append(fila)

    y=y+((1/6)*(k1+2*k2+2*k3+k4))*h
    x+=h

print(tabulate(matriz,headers=["i","x","y","k1","k2","k3","k4"]))