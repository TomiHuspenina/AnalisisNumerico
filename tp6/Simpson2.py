import math

print("metodo simpson ejercicio 2")
print(" ")

a=-3
b=5
n=10
h=(b-a)/n
funcion=[]
x=[]

i=0
while i <= n:
    x.append((i*(b-a))/n)
    funcion.append(1-x[i]-4*x[i]**3+3*x[i]**5)
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

Vreal=6904
Error=abs(Vreal-Is)
print(f"Error real cometido: {Error}")
print(" ")