#Autor:Sharon Michelle Olvera Ibarra
#Descripción: Lo esencial del bucle while- Adivina el numero secreto
#Fecha: 29/09/2023


secret_number = 777

print(
"""
+==================================+
| ¡Bienvenido a mi juego, muggle!  |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")

# Solicita al usuario que ingrese un número
while True:
    user_number = int(input("Introduce un número: "))
    
    # El numero que se ingreso coincide con el numero
    if user_number == secret_number:
        print("¡Bien hecho, muggle! Eres libre ahora")
        break  
    else:
        print("¡Ja, ja! ¡Estás atrapado en mi bucle!")  # Mensaje de error si no adivina el número secreto
