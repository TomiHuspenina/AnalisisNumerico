import math
from tabulate import tabulate
print("metodo simpson ejercicio 3")
print(" ")

a=0
b=(3*math.pi)/20
n=8
h=(b-a)/n
funcion=[]
x=[]
matriz=[]

i=0
while i <= n:
    x.append(i*h+a)
    funcion.append(math.sin(5*x[i]+1))
    i+=1

i=0
while i<=n:
    fila = list()
    fila.append(i)
    fila.append(x[i])
    fila.append(funcion[i])
    matriz.append(fila)
    i+=1

print(tabulate(matriz, headers=["i", "x", "funcion"]))

fpar=0
fimpar=0

i=1
while i<=n-1:
    fimpar=fimpar+funcion[i]
    i+=2
i=2
while i<=n-2:
    fpar=fpar+funcion[i]
    i+=2

print(" ")
print(f"funcion impar: {fimpar}")
print(f"funcion par: {fpar}")

Is=(b-a)*(funcion[0]+4*fimpar+2*fpar+funcion[n])/(3*n)
print(f"valor de Is: {Is}")

Vreal = 0.3047
Error=abs(Vreal-Is)
print(f"Error real cometido: {Error}")
