##Nombre: Brandon de Jesus Garza Jasso       Matricula: 250218
#Escriba un programa interactivo para calificar a un grupo de  10 alumnos .el programa  debe  leer el nombre  y sus tres calificaciones para  cada

print("Calificaciones de 10 alumnos")

for i in range(1, 11):
    nomb = input(f"\nIngrese el nombre del alumno {i}: ")

    cal1 = float(input(f"Calificación 1 de {nomb}: "))
    cal2 = float(input(f"Calificación 2 de {nomb}: "))
    cal3 = float(input(f"Calificación 3 de {nomb}: "))

    prom = (cal1 + cal2 + cal3) / 3

    print(f"Alumno: {nomb} | Promedio: {prom:.2f}\n")
