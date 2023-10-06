import math
    
print("ejercicio 3")
x=[]
funcion=[]
fDerivada=[]
newDerivada=[]
h = 1  
i = 0
c = -10  

while c <= 10:
    x.append(c / 10.0)  
    funcion.append((x[i]**3+3*x[i]-2)/(x[i]**2-4))
    fDerivada.append((x[i]**4-15*x[i]**2+4*x[i]-12)/((x[i]**2-4)**2))
    newDerivada.append((x[i]**4-15*x[i]**2+4*x[i]-12)/((x[i]**2-4)**2))
    print(f"funcion {i+1}: {funcion[i]}")
    print(f"X: {x[i]}")
    c += h
    i += 1

i = 0
c = -10  
while c <= 10:
    if c == -10:
        funcionProg = ((-3 * funcion[i]) + (4 * funcion[i + 1]) - (funcion[i + 2])) / (2 * h / 10.0)  
        print(f"Derivada P {i}:  {funcionProg}")
    elif c == 10:
        funcionRegre = ((funcion[i - 2]) - (4 * funcion[i - 1]) + (3 * funcion[i])) / (2 * h / 10.0)  
        print(f"Derivada R {i}:  {funcionRegre} ")
    else:
        if c - h >= -10 and c + h <= 10:  
            funcionCentrada = ((funcion[i + 1]) - (funcion[i - 1])) / (2 * h / 10.0)  
            print(f"Derivada C {i}:  {funcionCentrada} ")
    c += h
    i += 1

i = 0
c = -10
print(" ")
while c <= 10:
    print(f"derivada calculada {i}: {fDerivada[i]}")
    c += h
    i += 1


#forma de los 5 puntos

print(" ")
print("Forma de los 5 puntos")
i = 0
c = -10
newDif=[]
print(" ")
while c <= 10:

    if c == -10 or c == -10 + h:

        newFuncionProg = ((-25 * funcion[i]) + (48 * funcion[i + 1]) - (36*funcion[i + 2]) + (16*funcion[i+3])-(3*funcion[i+4])) / (12 * h / 10.0)
        print(f"Derivada P {i}:  {newFuncionProg}")
        newDif.append(abs(newDerivada[i]-newFuncionProg))

    elif c == 10 or c == 10-h:

        newFuncionRegre = ((3*funcion[i - 4]) - (16 * funcion[i - 3]) + (36 * funcion[i-2]) - (48*funcion[i-1]) + (25*funcion[i])) / (12 * h / 10.0)
        print(f"Derivada R {i}:  {newFuncionRegre} ")
        newDif.append(abs(newDerivada[i]-newFuncionRegre))

    else:

        if c - h >= h or c + 2*h < len(funcion):
           
           newFuncionCentrada = ((funcion[i - 2]) - (8*funcion[i - 1]) + (8*funcion[i+1]) - (funcion[i+2])) / (12 * h / 10.0)
           print(f"Derivada C {i}:  {newFuncionCentrada} ")
           newDif.append(abs(newDerivada[i]-newFuncionCentrada))

    c += h
    i += 1

i = 0
c = -10
print(" ")
while c <= 10:
    print(f"derivada calculada {i}: {newDerivada[i]}")
    c += h
    i += 1

i = 0
c = -10
print(" ")
while c <= 10:
    print(f"diferencia {i}: {newDif[i]}")
    c += h
    i += 1