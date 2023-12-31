import math
from tabulate import tabulate
print("ejercicio 4 metodo de los trapecios")

n=10
a=0
b=4
h=(b-a)/n
i=0
x=[]
funcion=[]
devSeg=[]
matriz1=[]
matriz2=[]
sumaDevS=0
suma=0
Itotal=0
pri=(b-a)/(2*n)

while i <= n:
    x.append(i*h+a)
    funcion.append(x[i]*math.exp(x[i]*2))
    devSeg.append(4*math.exp(2*x[i])+4*x[i]*math.exp(2*x[i]))
    i+=1

i=1
while i <= n:
   sumaDevS+=devSeg[i]
   i+=1


i=0
while i<len(x):
    fila1 = list()
    fila1.append(i)
    fila1.append(x[i])
    fila1.append(funcion[i])
    matriz1.append(fila1)
    i+=1

print(tabulate(matriz1, headers=["i", "x", "funcion"]))

i=1
while i<len(x):
    fila2 = list()
    fila2.append(i)
    fila2.append(x[i])
    fila2.append(devSeg[i])
    matriz2.append(fila2)
    i+=1

print(tabulate(matriz2, headers=["i", "x", "Derivada2"]))

print(" ")
print(f"suma derivada segunda: {sumaDevS}")
print(" ")

fn=sumaDevS/n

print(f"f'': {fn}")

i=1
while i <= n-1:
    suma+=funcion[i]
    i+=1

print(" ")
print(f"suma de 1 a n-1: {suma}")

print(" ")
It=(pri)*(funcion[0]+2*suma+funcion[n])
print(f"It: {It}")

Vreal = 5216.92647
print(f"valor real: {Vreal}")

print(" ")
Et=-(((b-a)**3)/(12*n*n))*fn
print(f"Et: {Et}")

print(" ")

Error=abs(Vreal-It)
print(f"error cometido: {Error}")