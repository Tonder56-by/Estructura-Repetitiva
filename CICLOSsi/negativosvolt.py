#Nombre: Brandon de Jesus Garza Jasso       Matricula: 250218
#Leer 15 números negativos y convertirlos a positivos e imprimir dichos números. 

print("Ingrese 15 números negativos:")

for i in range(1, 16):
    num = float(input(f"Número {i}: "))

    # Verificamos si es negativo, si no, advertimos
    if num >= 0:
        print("\nDebe ingresar un número NEGATIVO.")
    else:
        num = abs(num)  # Convierte a positivo
        print(f"Convertido a positivo: {num}")
