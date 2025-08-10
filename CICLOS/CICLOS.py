#Nombre Brandon de Jesus Garza Jasso    Matricula:  250218
#Leer 5 numeros y cual es el mas grande

#inicializar la variable con un numero muy pequeño
mayor = float("-inf")

#leer 5 numeros usando un vucle for

for i in range(5):
    num=float(input(f"Infrese el numero {i + 1}: "))
    #comparar el numero actial con el mayor hasta encontrarlo
    if num > mayor:
        mayor = num

    #imprimir el numero mayor
print(f"EL numero mayor es : {mayor}")
