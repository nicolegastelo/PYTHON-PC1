hora_str = input("Ingrese la hora:")
partes = hora_str.split(":")
hora = int(partes[0])
minutos = int(partes[1])
hora_decimal = hora + minutos / 60
if 7 <= hora_decimal <= 8:
    print("Es hora del desayuno")
elif 12 <= hora_decimal <= 13:
    print("Es hora del almuerzo")
elif 18 <= hora_decimal <= 19:
    print("Es hora de la cena")