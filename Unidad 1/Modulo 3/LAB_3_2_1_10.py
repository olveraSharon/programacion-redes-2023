#Autor: Sharon Michelle Olvera Ibarra
#Descripción: La sentencia continue
#Fecha: 02/10/2023



# Indicar al usuario que ingrese una palabra
# y asignarlo a la variable user_word.
user_word = input("Por favor, ingresa una palabra: ")
user_word = user_word.upper()

letras_no_consumidas = ""

for letter in user_word:
    # Completa el cuerpo del bucle for.
    if letter in "AEIOU":
        continue
    letras_no_consumidas += letter

for letter in letras_no_consumidas:
    print(letter)
