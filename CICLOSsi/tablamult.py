#Nombre Brandon de Jesus Garza Jasso    Matricula:  250218
#Tabla de multiplicar

acumulador=1
n=int(input(f"Que numero quieres saber su tabla : "))

for j in range (n):#numero de la tabla
    print(f"\nLa tabla de multiplkicar de {j+1} es: ")
    for i in range(10):#Multiplicaciones hasta 10
        mul=(j+1)*(i+1)
        print(f"{j+1} x {i+1} = {mul}")
    print("\n")


