import math
from tabulate import tabulate

f=[]
x=[]
matriz=[]
valorf=0
valorx=0

n=int(input("ingrese n:   "))

i=0
while i<=n:
   valorx=float(input(f"ingrese x[{i}]   "))
   x.append(valorx)
   valorf=float(input(f"ingrese f[{x[i]}]   "))
   f.append(valorf)
   print(" ")
   i+=1

a=x[0]
b=x[n]
fimpar=0
fpar=0

i=1
while i<=n-1:
   fimpar=fimpar+f[i]
   i+=2

i=0
while i<=n:
   fila=list()
   fila.append(i)
   fila.append(x[i])
   fila.append(f[i])
   matriz.append(fila)
   i+=1

print(tabulate(matriz, headers=["i", "x[i]", "f[x]"]))

print(" ")
print(f"impar: {fimpar}")
print(" ")

i=2
while i<=n-2:
   fpar=fpar+f[i]
   i+=2

print(f"par: {fpar}")
print(" ")

Is=((b-a)/(3*n))*(f[0]+4*fimpar+2*fpar+f[n])

print(f"Is= {Is}")