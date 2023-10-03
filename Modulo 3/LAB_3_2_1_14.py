#Autor: Sharon Michelle Olvera Ibarra
#Descripción: Fundamentos del bucle while
#Fecha:02/10/2023


blocks = int(input("Ingresa el número de bloques: "))

height = 0  
blocks_needed = 1  

while blocks >= blocks_needed:
    height += 1 
    blocks -= blocks_needed  
    blocks_needed += 1  

print("La altura de la pirámide:", height)

