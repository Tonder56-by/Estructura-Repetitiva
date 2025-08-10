#Nombre: Brandon de Jesus Garza Jasso       Matricula: 250218
#Realizar un programa que lea 50 números e imprima el número mayor

mayor = float("-inf")

#leer 5 numeros usando un bucle for

for i in range(50):
    num=float(input(f"Infrese el numero {i + 1}: "))
    #comparar el numero actial con el mayor hasta encontrarlo
    if num > mayor:
        mayor = num

    #imprimir el numero mayor
print(f"EL numero mayor es : {mayor}")