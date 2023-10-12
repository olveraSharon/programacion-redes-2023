#Autor: Sharon Michelle Olvera Ibarra
#Descripción: Lo básico de las listas
#Fecha: 02/10/2023

hat_list = [1, 2, 3, 4, 5]  # Esta es una lista existente de números ocultos en el sombrero.

# Paso 1: escribe una línea de código que solicite al usuario
# reemplazar el número de en medio con un número entero ingresado por el usuario.
user_number = int(input("Ingresa un número entero para reemplazar el número central: "))
hat_list[len(hat_list) // 2] = user_number


# Paso 2: escribe aquí una línea de código que elimine el último elemento de la lista.
del hat_list[-1]

# Paso 3: escribe aquí una línea de código que imprima la longitud de la lista existente.
print("Longitud de la lista existente:", len(hat_list))

print(hat_list)
