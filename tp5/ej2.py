import math
from tabulate import tabulate

print("ejercicio 2")

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
c = 10

while c <= 20:
    x.append(c / 10.0)
    exponencial = math.exp(3 * x[i])
    funcion.append(5 * exponencial * math.sin(2 * x[i]))
    derivada.append(5 * (exponencial * 3 * math.sin(2 * x[i]) + math.cos(2 * x[i]) * 2 * exponencial))
    newDerivada.append(5 * (exponencial * 3 * math.sin(2 * x[i]) + math.cos(2 * x[i]) * 2 * exponencial))

    c+=h
    i+=1

i=0
c=10
while c<=20:
    if c == 10:
        funcionProg = ((-3 * funcion[i]) + (4 * funcion[i + 1]) - (funcion[i + 2])) / (2 * h / 10.0)  
        funcion3.append(funcionProg)
        dif.append(abs(derivada[i] - funcionProg))
        
    elif c == 20:
        funcionRegre = ((funcion[i - 2]) - (4 * funcion[i - 1]) + (3 * funcion[i])) / (2 * h / 10.0)
        funcion3.append(funcionRegre)
        dif.append(abs(derivada[i] - funcionRegre))
       
    else:
        if c-h >= 10 and c < 20:
            funcionCentrada = ((funcion[i + 1]) - (funcion[i - 1])) / (2 * h / 10.0)
            funcion3.append(funcionCentrada)
            dif.append(abs(derivada[i] - funcionCentrada))
           
    c+=h
    i+=1

i=0
c=10
while c<= 20:

    if c == 10 or c == 11:
        newFuncionProg = ((-25 * funcion[i]) + (48 * funcion[i + 1]) - (36 * funcion[i + 2]) + (16 * funcion[i + 3]) - (3 * funcion[i + 4])) / (12 * h / 10.0)
        funcion5.append(newFuncionProg)
        newDif.append(abs(newDerivada[i] - newFuncionProg))
    
    elif c == 20 or c == 20 - h:
        newFuncionRegre = ((3 * funcion[i - 4]) - (16 * funcion[i - 3]) + (36 * funcion[i - 2]) - (48 * funcion[i - 1]) + (25 * funcion[i])) / (12 * h / 10.0)
        funcion5.append(newFuncionRegre)
        newDif.append(abs(newDerivada[i] - newFuncionRegre))
    
    else:
        if c-2*h >= 10 and c+h < 20:
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
