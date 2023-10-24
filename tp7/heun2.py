import math
from tabulate import tabulate

a = 0
b = 4
h = 0.5
i = 0
matriz = []
n = int((b - a) / h) + 1

def f(x, y):
    return 2*x**3+12*x**2-20*x+8.5

y = 1
x = 0
heun=y
yaux=0
xaux=0
s=h/2

for i in range(0, n):

    fila = [i, x, y, heun]
    matriz.append(fila)
    yaux=y
    xaux=x
    y = y + f(x, y)*h
    x += h
    heun=yaux+(f(xaux, yaux)+f(x,y))*s

print(tabulate(matriz, headers=["i", "x", "euler", "heun"]))