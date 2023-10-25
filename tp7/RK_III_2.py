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
x=0
y=1

for i in range(0,n):
    k1=f(x,y)
    k2=f(x+(0.5*h),y+(h*k1*0.5))
    k3=f(x+h,(y-(h*k1)+(2*h*k2)))

    fila=[i,x,y,k1,k2, k3]
    matriz.append(fila)

    y=y+((1/6)*(k1+4*k2+k3))*h
    x+=h

print(tabulate(matriz,headers=["i","x","y","k1","k2","k3"]))