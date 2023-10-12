#Autor: Sharon Michelle Olvera Ibarra
#Descripción: Variables un sencillo convertidor
#Fecha: 25/09/2023

kilometers = 12.25
miles = 7.38

# Conversión de millas a kilómetros
miles_to_kilometers = miles * 1.61

# Conversión de kilómetros a millas
kilometers_to_miles = kilometers / 1.61

print(miles, "millas son", round(miles_to_kilometers, 2), "kilómetros")
print(kilometers, "kilómetros son", round(kilometers_to_miles, 2), "millas")
