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

y = 2
x = 0

for i in range(n):

    fila = [i, x, y]
    matriz.append(fila)
    y = y + f(x, y)*h
    x += h

print(tabulate(matriz, headers=["i", "x", "y"]))