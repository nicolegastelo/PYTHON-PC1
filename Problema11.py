entrada = input("Ingrese los elementos de la lista separados por comas: ")
lista_usuario = [elemento.strip() for elemento in entrada.split(",")]
lista_sin_duplicados = []
for elemento in lista_usuario:
    if elemento not in lista_sin_duplicados:
        lista_sin_duplicados.append(elemento)
print(f"La Lista procesada es la siguiente:{lista_sin_duplicados}")