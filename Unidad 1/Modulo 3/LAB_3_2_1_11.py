#Autor: Sharon Michelle Olvera Ibarra
#Descripción:  La sentencia continue - El Bonito Devorador de Vocales
#Fecha:02/10/2023

word_without_vowels = ""

# Indicar al usuario que ingrese una palabra
# y asignarla a la variable user_word.
user_word = input("Por favor, ingresa una palabra: ")
user_word = user_word.upper()
word_without_vowels = ""

for letter in user_word:
   # Completa el cuerpo del bucle.

# Imprimir la palabra asignada a word_without_vowels.

    if letter in "AEIOU":
        continue
    word_without_vowels += letter

# Imprimir la palabra sin vocales
print("Palabra sin vocales:", word_without_vowels)
