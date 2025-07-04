monto_consumo=float(input("Ingresar monto de consumo en el restaurante:"))
porcentaje_propina=float(input("Ingresar monto de porcentaje de propina para el mesero:"))
monto_propina=(porcentaje_propina/100)*monto_consumo
print(f"El monto total de propina sería:{monto_propina}")