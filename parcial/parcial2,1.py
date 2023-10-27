import math
from tabulate import tabulate
    
x=[]
funcion=[-0.2707,-0.2842,-0.2975,-0.3106,-0.3230,-0.3347, -0.3452,-0.3543,-0.3614,-0.3662, -0.3679,-0.3659,-0.3595,-0.3476,-0.3293,-0.3033,-0.2681,-0.2222,-0.1637,-0.0905,0]
funcion3=[]
matriz=[]
h=1
i=0
c=-20

while c<=0:
    x.append(c/10)
    print(f"f{c}: {funcion[i]}")
    c+=h
    i+=1
   
i=0
c=-20
for i in range(0, len(x)):
    print(f"c: {c}")
    if c == -20:

        funcionProg = ((-3 * funcion[i]) + (4 * funcion[i + 1]) - (funcion[i + 2])) / (2 * (h/10))
        funcion3.append(funcionProg)
        print(f"funcion3 p {i}: {funcion3[i]}")

    elif c == 0:

        funcionRegre = ((funcion[i - 2]) - (4 * funcion[i - 1]) + (3 * funcion[i])) / (2 * (h/10))
        funcion3.append(funcionRegre)
        print(f"funcion3 r {i}: {funcion3[i]}")

    else:

        if c - h >= -20 and c + h <= 0:
           
           funcionCentrada = ((funcion[i + 1]) - (funcion[i - 1])) / (2 * (h/10))
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
    matriz.append(fila)

print(tabulate(matriz, headers=["i","x", "funcion", "DevTres","dev3","dif3"]))
