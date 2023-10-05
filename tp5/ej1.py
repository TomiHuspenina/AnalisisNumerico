import math

print("ejercicio 1")
x=0
h=0.1
i=0
while x<=0.7:
    exponencial=math.exp(x)
    funcion=exponencial*math.cos(x)

    mensaje1 = f"x {i}: {x}"
    mensaje2 = f"funcion {i}: {funcion}"
    print(mensaje1)
    print(mensaje2)
    x+=h
    i+=1
    
