#Autor: Sharon Michelle Olvera Ibarra
#Descripción: Fundamentos de la sentencia if-elif-else
#Fecha: 29/09/2023

year = int(input("Introduce un año:"))


if year >= 1582:

    if (year / 4 != 0) or (year % 100 == 0 and year % 400 != 0):
        print("Año Común")
    else:
        print("Año Bisiesto")
else:
    print("No dentro del período del calendario Gregoriano")
