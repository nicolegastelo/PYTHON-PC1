edad=int(input("Ingrese la edad del cliente: "))
if edad < 4:
    precio=0
elif edad <= 18:
    precio=5
else:
    precio=10
print(f"El precio de la entrada es: ${precio}")