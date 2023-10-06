import math

print("ejercicio 1 metodo de los trapecios")

n=10
a=0
b=math.pi
i=0
x=[]
funcion=[]
suma=0
Itotal=0
pri=(b-a)/(2*n)
print(f"pri: {pri}")
print(" ")

while i <= n:
    
    x.append((i*(b-a))/n)
    print(f"valor de x {i}: {x[i]}")
    funcion.append(8+5*math.cos(x[i]))
    print(f"funcion {i}: {funcion[i]}")
    i+=1

i=1
while i<=n-1:
    suma+=funcion[i]
    i+=1

print(f"suma: {suma}")

Itotal=(pri)*(funcion[0]+2*suma+funcion[n])

print(f"expresion final: {Itotal}")