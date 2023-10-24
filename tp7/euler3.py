import math
from tabulate import tabulate

a = 0
b = 2
h = 0.01
i = 0
matriz = []
n = int((b - a) / h) + 1

def f(x, y):
    return y*x**2-y

y = 1
x = 0

for i in range(n):

    fila = [i, x, y]
    matriz.append(fila)
    y = y + f(x, y)*h
    x += h

print(tabulate(matriz, headers=["i", "x", "y"]))