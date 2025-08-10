#Diseñar un algoritmo para  imprimir los números impares en el rango del 1  al 100  

print("Números impares del 1 al 100:")

for i in range(1, 101):
    if i % 2 != 0:
        print(i, end=" ")
