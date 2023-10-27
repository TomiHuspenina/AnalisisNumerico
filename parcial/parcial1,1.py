import math
from tabulate import tabulate
    
x=[]
funcion=[]
derivada=[]
dif=[]
funcion3=[]
matriz=[]
h=2
i=0
c=0

while c<=20:
    x.append(c/10)
    funcion.append(((3*x[i]-1)/(x[i]**2+1))**2)
    derivada.append((2*(3*x[i]-1)*(-3*x[i]**2+2*x[i]+3))/((x[i]**2+1)**3))
    
    c+=h
    i+=1
   
i=0
c=0
for i in range(0, len(x)):
    print(f"c: {c}")
    if c == 0:

        funcionProg = ((-3 * funcion[i]) + (4 * funcion[i + 1]) - (funcion[i + 2])) / (2 * (h/10))
        dif.append(abs(derivada[i]-funcionProg))
        funcion3.append(funcionProg)
        print(f"funcion3 p {i}: {funcion3[i]}")

    elif c == 20:

        funcionRegre = ((funcion[i - 2]) - (4 * funcion[i - 1]) + (3 * funcion[i])) / (2 * (h/10))
        dif.append(abs(derivada[i]-funcionRegre))
        funcion3.append(funcionRegre)
        print(f"funcion3 r {i}: {funcion3[i]}")

    else:

        if c - h >= 0 and c + h <= 20:
           
           funcionCentrada = ((funcion[i + 1]) - (funcion[i - 1])) / (2 * (h/10))
           dif.append(abs(derivada[i]-funcionCentrada))
           funcion3.append(funcionCentrada)
           print(f"funcion3 c {i}: {funcion3[i]}")
    c+=h

print(f"funcion3 len: {len(funcion3)}")

for i in range(0, len(x)):

    fila = list()
    fila.append(i)
    fila.append(x[i])
    fila.append(funcion[i])
    fila.append(funcion3[i])
    fila.append(derivada[i])
    fila.append(dif[i])
    matriz.append(fila)

print(tabulate(matriz, headers=["i","x", "funcion", "DevTres","dev3","dif3"]))
