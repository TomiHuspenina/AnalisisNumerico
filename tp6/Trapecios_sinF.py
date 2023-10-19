import math
from tabulate import tabulate

f=[]
x=[]
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
h=(b-a)/(n)
suma=0


i=1
while i<=n-1:
    suma=suma+f[i]
    i+=1

It=(0.5*h)*(f[0]+2*suma+f[n])

print(f"suma de 1 a n-1: {suma}")
print(" ")
print(f"It= {It}")