#Nombre Brandon de Jesus Garza Jasso    Matricula:  250218
#Suponga que se tiene un conjunto de calificaciones de un grupo de 40 alumnos. Realizar un algoritmo para  calcular  la  calificación media  y la  calificación mas baja  de  todo el  grupo.
total_alumnos = 40
suma_calificaciones = 0
calif_minima = None

for i in range(1, total_alumnos + 1):
    calif = float(input(f"Ingrese la calificación del alumno {i}: "))
    suma_calificaciones += calif

    if calif_minima is None or calif < calif_minima:
        calif_minima = calif

promedio = suma_calificaciones / total_alumnos

print("\n Resultados:")
print(f"Calificación media del grupo: {promedio:.2f}")
print(f"Calificación más baja: {calif_minima}")
