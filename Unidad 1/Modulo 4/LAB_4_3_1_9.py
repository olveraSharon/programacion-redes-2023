#Aurot: Sharon Michelle Olvera Ibarra
#Fecha: 06/10/2023
#Descripcion:Números primos: ¿Cómo encontrarlos?

import math

def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False

    # Comprueba divisores a partir de 3 hasta la raíz cuadrada de num
    for divisor in range(3, int(math.sqrt(num)) + 1, 2):
        if num % divisor == 0:
            return False

    return True

# Pruebas de números primos del 1 al 20
for i in range(1, 20):
    if is_prime(i):
        print(i, end=" ")
print()