num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
print("Elija una opción:")
print("1 - Sumar los dos números")
print("2 - Restar (primer número menos segundo)")
print("3 - Multiplicar los dos números")
opcion = input("Ingrese el número de opción (1, 2 o 3): ")
if opcion == "1":
    resultado = num1 + num2
    print(f"La suma es:{resultado}")
elif opcion == "2":
    resultado = num1 - num2
    print(f"La resta es:{resultado}")
elif opcion == "3":
    resultado = num1 * num2
    print(f"La multiplicación es:{resultado}")
else:
    print("Opción inválida, no es correcta")