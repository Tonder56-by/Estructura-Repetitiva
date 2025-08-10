#Nombre: Brandon de Jesus Garza Jasso       Matricula: 250218
#Sacar el Factorial

acumulador=1
n=int(input(f"De que numero quieres su factorial: "))

for i in range(n):
    #Factorial
    acumulador=acumulador*(i+1)

    print(f"El factorial de {n} es : {acumulador}")
