#Autor: Sharon Michelle Olvera Ibarra
#Descripción: La sentencia breack- Atascado en bucle
#Fecha: 02/10/2023

p = ""

# Configura la palabra secreta
p_secreta = "chupacabra"

# Bucle while para solicitar palabras al usuario
while p != p_secreta:
    p = input("Ingresa una palabra: ")
    
# Cuando el usuario ingrese la palabra secreta, el bucle se romperá
print("¡Has dejado el bucle con éxito.")
