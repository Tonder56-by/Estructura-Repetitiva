#Nombre: Brandon de Jesus Garza Jasso       Matricula: 250218
#leer 5 numeros usando un Bucle for

mayor = float("-inf")
contador=0
acumulador=0


for i in range(5):
    num=float(input(f"Infrese el numero {i + 1}: "))
    acumulador=acumulador+num
    #comparar el numero actial con el mayor hasta encontrarlo
    if num > mayor:
        mayor = num
        contador=contador+1

    #imprimir el numero mayor
print(f"EL numero mayor es : {mayor}")
print(f"Numero de cambio : {contador}")
print(f"Total sumado : {acumulador}")
