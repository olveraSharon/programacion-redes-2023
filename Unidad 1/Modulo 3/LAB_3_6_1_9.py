#Autor: Sharon Michelle Olvera Ibarra
#Descripción: Operando con listas - conceptos básicos
#Fecha: 02/10/2023

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
# Escribe tu código aquí.
unique_list = []

# Recorrer la lista original
for number in my_list:
    if number not in unique_list:
        unique_list.append(number)
print("La lista con elementos únicos:")
print(my_list)
