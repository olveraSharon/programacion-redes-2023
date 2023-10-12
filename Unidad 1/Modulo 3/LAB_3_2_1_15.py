# Autor:Sharon Michelle Olvera Ibarra
#Descripción: Hipótesis de Collatz
#Ficha: 02/10/2023

c0 = int(input("Ingresa un número natural: "))

steps = 0

print("Secuencia de Collatz para c0 =", c0)

while c0 != 1:
    if c0 % 2 == 0:
        c0 = c0 // 2  
    else:
        c0 = 3 * c0 + 1  
    steps += 1
    
    print(c0)

print("Pasos necesarios para llegar a 1:", steps)
