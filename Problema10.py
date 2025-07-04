entrada = input("Ingrese los elementos de la lista separados por comas: ")
lista = [elemento.strip() for elemento in entrada.split(",")]
lista_resultado = [elem for i, elem in enumerate(lista) if i not in (0, 4, 5)]
print(f"La Lista resultante es la siguiente:{lista_resultado}")