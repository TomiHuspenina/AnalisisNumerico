import math
from tabulate import tabulate
    
print("ejercicio 1")
x=[]
funcion=[]
derivada=[]
dif=[]
newDerivada=[]
funcion3=[]
funcion5=[]
newDif=[]
matriz=[]
h=0.1
i=0
c=0

while c<=0.7:
    x.append(c)
    exponencial = math.exp(x[i])
    funcion.append(exponencial * math.cos(x[i]))
    derivada.append(exponencial*(math.cos(x[i])-math.sin(x[i])))
    newDerivada.append(exponencial*(math.cos(x[i])-math.sin(x[i])))
    
    c+=h
    i+=1
   
i=0
c=0
while c <= 0.7:
    #forma de los 3 puntos
    if c == 0:

        funcionProg = ((-3 * funcion[i]) + (4 * funcion[i + 1]) - (funcion[i + 2])) / (2 * h)
        dif.append(abs(derivada[i]-funcionProg))
        funcion3.append(funcionProg)

    elif c == 0.7:

        funcionRegre = ((funcion[i - 2]) - (4 * funcion[i - 1]) + (3 * funcion[i])) / (2 * h)
        dif.append(abs(derivada[i]-funcionRegre))
        funcion3.append(funcionRegre)

    else:

        if c - h >= 0 and c + h < len(funcion):
           
           funcionCentrada = ((funcion[i + 1]) - (funcion[i - 1])) / (2 * h)
           dif.append(abs(derivada[i]-funcionCentrada))
           funcion3.append(funcionCentrada)
    c+=h
    i+=1

i=0
c=0
while c<=0.7:
    # forma de los 5 puntos
    if c==0 or c==h:

        newFuncionProg = ((-25 * funcion[i]) + (48 * funcion[i + 1]) - (36*funcion[i + 2]) + (16*funcion[i+3])-(3*funcion[i+4])) / (12 * h)
        newDif.append(abs(newDerivada[i]-newFuncionProg))
        funcion5.append(newFuncionProg)

    elif c == 0.7 or c == 0.7-h:

        newFuncionRegre = ((3*funcion[i - 4]) - (16 * funcion[i - 3]) + (36 * funcion[i-2]) - (48*funcion[i-1]) + (25*funcion[i])) / (12 * h)
        newDif.append(abs(newDerivada[i]-newFuncionRegre))
        funcion5.append(newFuncionRegre)

    else:

        if c - h >= h and c + 2*h < len(funcion):
           
           newFuncionCentrada = ((funcion[i - 2]) - (8*funcion[i - 1]) + (8*funcion[i+1]) - (funcion[i+2])) / (12 * h)
           newDif.append(abs(newDerivada[i]-newFuncionCentrada))
           funcion5.append(newFuncionCentrada)

    c += h
    i += 1

print(" ")

for i in range(len(x)):

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

print(tabulate(matriz, headers=["x", "funcion", "DevTres","dev3","dif3" ,"DevCinco" , "dev5", "dif5"]))
