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

for i in range(n):

    fila = [i, x, y]
    matriz.append(fila)
    y = y + f(x, y)*h
    x += h

print(tabulate(matriz, headers=["i", "x", "y"]))