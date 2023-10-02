#Autor: Sharon Michelle Olvera Ibarra
#Descripción:Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. 
#Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta 
#de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, 
#introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el 
#primer, segundo y tercer años. Redondear cada cantidad a dos decimales.
#Fecha: 02/10/2023

# Lee la cantidad de dinero depositada en la cuenta de ahorros
monto_depositado = float(input("Ingresa la cantidad de dinero depositada: "))
# Calcula la cantidad de ahorros tas el primer año
saldo_despues_del_primer_a = monto_depositado * (1 + 0.04)
# Calcula el saldo después del segundo año con un 4% de interés
saldo_despues_del_segundo_a = saldo_despues_del_primer_a * (1 + 0.04)
# Calcula el saldo despues del tercer año con un 4% de interes
saldo_despues_del_tercer_a = saldo_despues_del_segundo_a * (1 + 0.04)


#Mostrar por pantalla la cantidad de ahorro tras cada uno de los tres años
print(f"Saldo después del primer año: {saldo_despues_del_primer_a:.2f}")
print(f"Saldo después del segundo año: {saldo_despues_del_segundo_a:.2f}")
print(f"Saldo después del tercer año: {saldo_despues_del_tercer_a:.2f}")


