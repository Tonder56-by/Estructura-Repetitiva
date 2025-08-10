#Nombre: Brandon de Jesus Garza Jasso       Matricula: 250218
#Calcular la media aritmética de n números ingresados por teclado

n = int(input("¿Cuántos números desea ingresar? "))

suma = 0

for i in range(1, n + 1):
    num = float(input(f"Ingrese el número {i}: "))
    suma += num

media = suma / n if n > 0 else 0

print(f"\n📊 La media aritmética es: {media:.2f}")
