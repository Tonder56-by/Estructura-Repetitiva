#Nombre: Brandon de Jesus Garza Jasso       Matricula: 250218
# Calcular la suma de cuatro números introducidos por teclado

suma = 0

for i in range(1, 5):
    num = float(input(f"Ingrese el número {i}: "))
    suma += num

print(f"\nLa suma de sus cuatro números es: {suma}")
