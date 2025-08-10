#Nombre: Brandon de Jesus Garza Jasso       Matricula: 250218
#Leer 100  números. Determinar  la  media  de  los números positivos y la  media de los números negativos 

suma_pos =  0
contador_pos = 0
suma_ne = 0
contador_ne = 0

for i in range(1, 101):
    num = float(input(f"Ingrese el número {i}: "))
    
    # Si es 0, no contar para ningúno
    if num > 0:
        suma_pos += num
        contador_pos += 1
    elif num < 0:
        suma_ne += num
        contador_ne += 1
    # Si es 0, no se cuenta para ningún promedio

# Calcular medias
media_positivos = suma_pos / contador_pos if contador_pos > 0 else 0
media_negativos = suma_ne / contador_ne if contador_ne > 0 else 0

print("\nResultados:")
print(f"Media de positivos: {media_positivos:.2f}")
print(f"Media de negativos: {media_negativos:.2f}")
