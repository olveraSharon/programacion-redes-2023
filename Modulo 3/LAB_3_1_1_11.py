#Autor:Sharon Michele Olvera Ibarra
#Descripción: Fundamentos de la sentencia if-else
#fecha: 29/09/2023

income = float(input("Introduce el ingreso anual:"))
if income<= 85528:
    tax = round(income * 0.18)- 556.02
else:
    tax = 14839.02 + (income - 85528) * 0.32
    tax = round(max(tax,0),0)
    tax= round(tax,0)
print("El impuesto es:", tax, "pesos")
