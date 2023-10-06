import math
    
print("ejercicio 1")
x=[]
funcion=[]
fDerivada=[]
derivada=[]
dif=[]
h = 1  # Usar enteros para h
i = 0
c = 10  # Usar enteros para c

while c <= 20:
    x.append(c / 10.0)  # Convertir c a punto flotante para x
    exponencial = math.exp(3 * x[i])
    funcion.append(5 * exponencial * math.sin(2 * x[i]))
    derivada.append(5*(exponencial*3*math.sin(2*x[i])+math.cos(2*x[i])*2*exponencial))

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