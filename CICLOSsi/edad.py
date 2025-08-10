#Nombre Brandon de Jesus Garza Jasso    Matricula:  250218
#Una persona debe realizar un muestreo con 50 personas para determinar el  promedio de peso de los niños, jóvenes, adultos y viejos que existen en su  zona habitacional. Se determinan las categorías con base  en la sig, tabla:  CATEGORIA  EDAD  
#Niños 0 ­ 12  
#Jóvenes 13 ­ 29  
#Adultos 30 ­ 59  
#Viejos 60 en adelante 

peso_ninos = peso_jovenes = peso_adultos = peso_viejos = 0
cont_ninos = cont_jovenes = cont_adultos = cont_viejos = 0

print("Muestreo de 50 personas\n")

for i in range(1, 51):
    print(f"Persona {i}:")
    edad = int(input("  Edad: "))
    peso = float(input("  Peso (kg): "))

    if 0 <= edad <= 12:
        peso_ninos += peso
        cont_ninos += 1
    elif 13 <= edad <= 29:
        peso_jovenes += peso
        cont_jovenes += 1
    elif 30 <= edad <= 59:
        peso_adultos += peso
        cont_adultos += 1
    elif edad >= 60:
        peso_viejos += peso
        cont_viejos += 1
    else:
        print("\nEdad inválida.")

prom_ninos = peso_ninos / cont_ninos if cont_ninos > 0 else 0
prom_jovenes = peso_jovenes / cont_jovenes if cont_jovenes > 0 else 0
prom_adultos = peso_adultos / cont_adultos if cont_adultos > 0 else 0
prom_viejos = peso_viejos / cont_viejos if cont_viejos > 0 else 0

# Mostrar resultados
print("\n Promedio de peso por categoría:")
print(f"Niños: {prom_ninos:.2f} kg")
print(f"Jóvenes: {prom_jovenes:.2f} kg")
print(f"Adultos: {prom_adultos:.2f} kg")
print(f"Viejos: {prom_viejos:.2f} kg")
