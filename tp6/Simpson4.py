import math

print("metodo simpson ejercicio 4")
print(" ")

a=0
b=4
n=10
h=(b-a)/n
funcion=[]
x=[]

i=0
while i <= n:
    x.append(i*h+a)
    funcion.append(x[i]*math.exp(x[i]*2))
    print(f"funcion {i} para {x[i]}: {funcion[i]}")
    i+=1

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
Is=(b-a)*(funcion[0]+4*fimpar+2*fimpar+funcion[n])/(3*n)
print(f"valor de Is: {Is}")

Vreal = 5216.92647
Error=abs(Vreal-Is)
print(f"Error real cometido: {Error}")
print(" ")