import math
from tabulate import tabulate

a=0
b=2
h=0.1
n=int((a+b)/h)+1
i=0
matriz=[]

def f(x, y):
    return 2*y-6

k1=0
k2=0
x=0
y=1

for i in range(0,n):
    k1=f(x,y)
    k2=f(x+h,y+h*k1)

    fila=[i,x,y,k1,k2]
    matriz.append(fila)

    y=y+((k1/2)+(k2/2))*h
    x+=h

print(tabulate(matriz,headers=["i","x","y","k1","k2"]))