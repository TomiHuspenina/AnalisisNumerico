import math
    
print("ejercicio 2")
x=[]
funcion=[]
fDerivada=[]
derivada=[]
newDerivada=[]
dif=[]
h = 1  # Usar enteros para h
i = 0
c = 10  # Usar enteros para c

while c <= 20:
    x.append(c / 10.0)  # Convertir c a punto flotante para x
    exponencial = math.exp(3 * x[i])
    funcion.append(5 * exponencial * math.sin(2 * x[i]))
    derivada.append(5*(exponencial*3*math.sin(2*x[i])+math.cos(2*x[i])*2*exponencial))
    newDerivada.append(5*(exponencial*3*math.sin(2*x[i])+math.cos(2*x[i])*2*exponencial))

    print(f"funcion {i+1}: {funcion[i]}")
    print(f"X: {x[i]}")
    c += h
    i += 1

i = 0
c = 10  # Restablecer c
while c <= 20:
    if c == 10:
        funcionProg = ((-3 * funcion[i]) + (4 * funcion[i + 1]) - (funcion[i + 2])) / (2 * h / 10.0)  # Convertir h a punto flotante para la derivada
        print(f"Derivada P:  {funcionProg}")
        dif.append(abs(derivada[i]-funcionProg))
    elif c == 20:
        funcionRegre = ((funcion[i - 2]) - (4 * funcion[i - 1]) + (3 * funcion[i])) / (2 * h / 10.0)  # Convertir h a punto flotante para la derivada
        print(f"Derivada R:  {funcionRegre} ")
        dif.append(abs(derivada[i]-funcionRegre))
    else:
        if c - h >= 10 and c + h <= 20:  # Asegurarse de que los valores estén dentro del rango adecuado
            funcionCentrada = ((funcion[i + 1]) - (funcion[i - 1])) / (2 * h / 10.0)  # Convertir h a punto flotante para la derivada
            print(f"Derivada C:  {funcionCentrada} ")
            dif.append(abs(derivada[i]-funcionCentrada))
    c += h
    i += 1

i = 0
c = 10
print(" ")
while c <= 20:
    print(f"derivada calculada {i}: {derivada[i]}")
    c += h
    i += 1

i = 0
c = 10
print(" ")
while c <= 20:
    print(f"diferencia {i}: {dif[i]}")
    c += h
    i += 1

#forma de los 5 puntos

print(" ")
print("Forma de los 5 puntos")
i = 0
c = 10
newDif=[]
print(" ")
while c <= 20:

    if c==10 or c==10+ h:

        newFuncionProg = ((-25 * funcion[i]) + (48 * funcion[i + 1]) - (36*funcion[i + 2]) + (16*funcion[i+3])-(3*funcion[i+4])) / (12 * h / 10.0)
        print(f"Derivada P {i}:  {newFuncionProg}")
        newDif.append(abs(newDerivada[i]-newFuncionProg))

    elif c == 20 or c == 20-h:

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
c = 10
print(" ")
while c <= 20:
    print(f"derivada calculada {i}: {newDerivada[i]}")
    c += h
    i += 1

i = 0
c = 10
print(" ")
while c <= 20:
    print(f"diferencia {i}: {newDif[i]}")
    c += h
    i += 1