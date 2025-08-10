#Nombre: Brandon de Jesus Garza Jasso       Matricula: 250218
#Calcular la suma de los cuadrados de los 100 primeros números naturales. 

suma_cuadrados = 0

for i in range(1, 101):
    suma_cuadrados += i ** 2  # i**2 es el cuadrado 

print(f"La suma de los cuadrados de los 100 primeros números es: {suma_cuadrados}")
