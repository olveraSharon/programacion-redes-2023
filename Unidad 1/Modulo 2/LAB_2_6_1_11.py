#Autor: Sharon Michelle Olvera Ibarra
#Descripsión: operadores y expresiones
#Fecha: 29/09/2023

hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

# Calcula el total de minutos
total_mins = hour * 60 + mins + dura

# Calcula las nuevas horas y minutos
new_hour = total_mins // 60
new_mins = total_mins % 60

# Asegura que las horas estén en el rango de 0 a 23
new_hour = new_hour % 24

print(f"El evento finaliza a las {new_hour:02}:{new_mins:02}")

