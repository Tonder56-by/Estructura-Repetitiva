#Nombre: Brandon de Jesus Garza Jasso       Matricula: 250218
#En un centro de verificación de automóviles se desea saber el promedio de puntos contaminantes de los primeros 25 automóviles que lleguen. Asimismo se desea saber los puntos contaminantes del carro que menos
#contamino y del que mas contamino.
mayor=float("-inf")
menor=None
acumulador=0
prom=0
puntos=0

for i in range(25):
    nc=float(input(f"Puntuacion obtenida en la verificacion numero: {i+1} "))
    acumulador=acumulador+nc

    if nc > mayor:
        mayor= nc
    if menor is None or nc < menor:
        menor = nc
        auto_min = i

prom=acumulador/25
print(f"El promedio de los 25 es de:  {prom}")
print(f"El mayor {mayor}")
print(f"el menor {menor}")

