#Nombre: Brandon de Jesus Garza Jasso       Matricula: 250218
#4 clientes que aun no han pagado recibirán un 15% de descuento si compran mas de 10 kilos.
kilo=20
suma=0
acumulador=0
for i in range(15):
    compra=float(input(f"Cliente numero {i+1} \nvalor del kilo hoy ${kilo} \nDe cuantos kilos fue su compra : "))
    if compra > 10:
        venta= compra * kilo
        compra=venta * .85
        print(f"---Su total de compra : ${compra}---")
    else:
        compra= compra * kilo
        print(f"---Su total de compra : ${compra}----")
    acumulador=acumulador+compra
print(f"\nSu total de venta generada : ${acumulador}")