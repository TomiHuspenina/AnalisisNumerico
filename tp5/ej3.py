import math
from tabulate import tabulate

print("ejercicio 3")
x = []
funcion = []
derivada = []
funcion3 = []
funcion5 = []
dif = []
newDif = []
newDerivada = []
matriz = []
h = 1  
i = 0
c = -10  

while c <= 10:
    x.append(c / 10.0)  
    funcion.append((x[i]**3+3*x[i]-2)/(x[i]**2-4))
    derivada.append((x[i]**4-15*x[i]**2+4*x[i]-12)/((x[i]**2-4)**2))
    newDerivada.append((x[i]**4-15*x[i]**2+4*x[i]-12)/((x[i]**2-4)**2))

    c += h
    i += 1

i=0
c=-10
while c<=10:
    if c == -10:
        funcionProg = ((-3 * funcion[i]) + (4 * funcion[i + 1]) - (funcion[i + 2])) / (2 * h / 10.0)  
        funcion3.append(funcionProg)
        dif.append(abs(derivada[i] - funcionProg))
        
    elif c == 10:
        funcionRegre = ((funcion[i - 2]) - (4 * funcion[i - 1]) + (3 * funcion[i])) / (2 * h / 10.0)
        funcion3.append(funcionRegre)
        dif.append(abs(derivada[i] - funcionRegre))
       
    else:
        if c-h >= -10 and c < 10:
            funcionCentrada = ((funcion[i + 1]) - (funcion[i - 1])) / (2 * h / 10.0)
            funcion3.append(funcionCentrada)
            dif.append(abs(derivada[i] - funcionCentrada))
           
    c+=h
    i+=1

i=0
c=-10
while c<= 10:

    if c == -10 or c == -9:
        newFuncionProg = ((-25 * funcion[i]) + (48 * funcion[i + 1]) - (36 * funcion[i + 2]) + (16 * funcion[i + 3]) - (3 * funcion[i + 4])) / (12 * h / 10.0)
        funcion5.append(newFuncionProg)
        newDif.append(abs(newDerivada[i] - newFuncionProg))
    
    elif c == 10 or c == 10 - h:
        newFuncionRegre = ((3 * funcion[i - 4]) - (16 * funcion[i - 3]) + (36 * funcion[i - 2]) - (48 * funcion[i - 1]) + (25 * funcion[i])) / (12 * h / 10.0)
        funcion5.append(newFuncionRegre)
        newDif.append(abs(newDerivada[i] - newFuncionRegre))
    
    else:
        if c-2*h >= -10 and c+h < 10:
            newFuncionCentrada = ((funcion[i - 2]) - (8 * funcion[i - 1]) + (8 * funcion[i + 1]) - (funcion[i + 2])) / (12 * h / 10.0)
            funcion5.append(newFuncionCentrada)
            newDif.append(abs(newDerivada[i] - newFuncionCentrada))
        

    c += h
    i += 1

print(" ")


i=0
while i<len(x):
    fila = list()
    fila.append(x[i])
    fila.append(funcion[i])
    fila.append(funcion3[i])
    fila.append(derivada[i])
    fila.append(dif[i])
    fila.append(funcion5[i])
    fila.append(newDerivada[i])
    fila.append(newDif[i])
    matriz.append(fila)
    i+=1

print(tabulate(matriz, headers=["x", "funcion", "DevTres", "dev3", "dif3", "DevCinco", "dev5", "dif5"]))
