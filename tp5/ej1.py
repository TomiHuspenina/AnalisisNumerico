import math
    
print("ejercicio 1")

#forma de los tres puntos

x=[]
funcion=[]
fDerivada=[]
derivada=[]
dif=[]
newDerivada=[]
h=0.1
i=0
c=0

while c <= 0.7:
    x.append(c)
    exponencial = math.exp(x[i])
    funcion.append(exponencial * math.cos(x[i]))
    derivada.append(exponencial*(math.cos(x[i])-math.sin(x[i])))
    newDerivada.append(exponencial*(math.cos(x[i])-math.sin(x[i])))

    print(f"funcion {i}: {funcion[i]}")
    print(f"X: {x[i]}")

    i += 1
    c += h

i = 0
c = 0
print(" ")

while c <= 0.7:

    if c == 0:

        funcionProg = ((-3 * funcion[i]) + (4 * funcion[i + 1]) - (funcion[i + 2])) / (2 * h)
        print(f"Derivada P {i}:  {funcionProg}")
        dif.append(abs(derivada[i]-funcionProg))

    elif c == 0.7:

        funcionRegre = ((funcion[i - 2]) - (4 * funcion[i - 1]) + (3 * funcion[i])) / (2 * h)
        print(f"Derivada R {i}:  {funcionRegre} ")
        dif.append(abs(derivada[i]-funcionRegre))

    else:

        if c - h >= 0 and c + h < len(funcion):
           
           funcionCentrada = ((funcion[i + 1]) - (funcion[i - 1])) / (2 * h)
           print(f"Derivada C {i}:  {funcionCentrada} ")
           dif.append(abs(derivada[i]-funcionCentrada))

    c += h
    i += 1

i = 0
c = 0
print(" ")
while c <= 0.7:
    print(f"derivada calculada {i}: {derivada[i]}")
    c += h
    i += 1

i = 0
c = 0
print(" ")
while c <= 0.7:
    print(f"diferencia {i}: {dif[i]}")
    c += h
    i += 1

#forma de los 5 puntos

print(" ")
print("Forma de los 5 puntos")
i = 0
c = 0
newDif=[]
print(" ")
while c <= 0.7:

    if c==0 or c==h:

        newFuncionProg = ((-25 * funcion[i]) + (48 * funcion[i + 1]) - (36*funcion[i + 2]) + (16*funcion[i+3])-(3*funcion[i+4])) / (12 * h)
        print(f"Derivada P {i}:  {newFuncionProg}")
        newDif.append(abs(newDerivada[i]-newFuncionProg))

    elif c == 0.7 or c == 0.7-h:

        newFuncionRegre = ((3*funcion[i - 4]) - (16 * funcion[i - 3]) + (36 * funcion[i-2]) - (48*funcion[i-1]) + (25*funcion[i])) / (12 * h)
        print(f"Derivada R {i}:  {newFuncionRegre} ")
        newDif.append(abs(newDerivada[i]-newFuncionRegre))

    else:

        if c - h >= h and c + 2*h < len(funcion):
           
           newFuncionCentrada = ((funcion[i - 2]) - (8*funcion[i - 1]) + (8*funcion[i+1]) - (funcion[i+2])) / (12 * h)
           print(f"Derivada C {i}:  {newFuncionCentrada} ")
           newDif.append(abs(newDerivada[i]-newFuncionCentrada))

    c += h
    i += 1

i = 0
c = 0
print(" ")
while c <= 0.7:
    print(f"derivada calculada {i}: {newDerivada[i]}")
    c += h
    i += 1

i = 0
c = 0
print(" ")
while c <= 0.7:
    print(f"diferencia {i}: {newDif[i]}")
    c += h
    i += 1