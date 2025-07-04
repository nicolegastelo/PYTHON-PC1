num_payasos=int(input("Ingrese el número de payasos vendidos: "))
num_munecas=int(input("Ingrese el número de muñecas vendidas: "))
peso_total_payasos=num_payasos*112
peso_total_munecas=num_munecas*75
peso_total_paquete=peso_total_payasos + peso_total_munecas
print(f"El peso total del paquete es: {peso_total_paquete} gramos")