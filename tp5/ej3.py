import math
    
print("ejercicio 1")
x=[]
funcion=[]
fDerivada=[]
h = 1  
i = 0
c = -10  

while c <= 10:
    x.append(c / 10.0)  
    funcion.append((x[i]*x[i]*x[i]+3*x[i]-2)/(x[i]*x[i]-4))
    print(f"funcion {i+1}: {funcion[i]}")
    print(f"X: {x[i]}")
    c += h
    i += 1

i = 0
c = -10  
while c <= 10:
    if c == -10:
        funcionProg = ((-3 * funcion[i]) + (4 * funcion[i + 1]) - (funcion[i + 2])) / (2 * h / 10.0)  
        print(f"Derivada P:  {funcionProg}")
    elif c == 10:
        funcionRegre = ((funcion[i - 2]) - (4 * funcion[i - 1]) + (3 * funcion[i])) / (2 * h / 10.0)  
        print(f"Derivada R:  {funcionRegre} ")
    else:
        if c - h >= -10 and c + h <= 10:  
            funcionCentrada = ((funcion[i + 1]) - (funcion[i - 1])) / (2 * h / 10.0)  
            print(f"Derivada C:  {funcionCentrada} ")
    c += h
    i += 1