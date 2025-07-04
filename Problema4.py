N=int(input("Ingrese un número entero positivo: "))
if N <= 0:
    print("El número debe ser un entero positivo mayor que cero.")
else:
    suma=N*(N+1)/2  
    print(f"La suma de los primeros {N} enteros positivos es: {suma}")