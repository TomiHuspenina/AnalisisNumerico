import math
from tabulate import tabulate

a = 0
b = 4
h = 0.1
i = 0
matriz = []
n = int((b - a) / h) + 1

def f(x, y):
    return math.exp(0.8 * x) - 0.50 * y

y=2
y0=y
x=0
xaux=0
y0axu=y0
yaux=y
s=h/2

for i in range(0, n):
    fila = [i, x, y0, y]
    matriz.append(fila)
    y0aux=y0
    y0=y+f(x,y)*h
    xaux=x 
    x=xaux+h
    yaux=y
    y=yaux+(f(xaux,yaux)+f(x,y0))*s

print(tabulate(matriz, headers=["i", "x", "euler", "heun"]))