print ("¿Cuál es el monto de la factura, por favor?")
monto= int(input())
print ("¿Entre cuantas personas pagaran la factura?")
cant= int(input())

iva= (monto*.18)
subtotal=iva + monto
total = subtotal/cant
redondeado = round(total)

iva2= (monto*.20)
subtotal2=iva2 + monto
total2 = subtotal2/cant
redondeado2 = round(total2)

iva3= (monto*.25)
subtotal3=iva3 + monto
total3 = subtotal3/cant
redondeado3 = round(total3)

print("La propina del 18% es de $" + str(iva) + " lo que eleva el total a $" + str(subtotal)+ ", Dividido entre los comensales cada uno pagaria: $"+ str(redondeado))
print("La propina del 20% es de $" + str(iva2) + " lo que eleva el total a $" + str(subtotal2)+ ", Dividido entre los comensales cada uno pagaria: $"+ str(redondeado2))
print("La propina del 25% es de $" + str(iva3) + " lo que eleva el total a $" + str(subtotal3)+ ", Dividido entre los comensales cada uno pagaria: $"+ str(redondeado3))