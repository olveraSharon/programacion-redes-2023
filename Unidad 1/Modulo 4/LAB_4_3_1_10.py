#Aurot: Sharon Michelle Olvera Ibarra
#Fecha: 06/10/2023
#Descripcion:Números primos: ¿Cómo encontrarlos?

def liters_100km_to_miles_gallon(liters):
    miles_per_gallon = 100 / (liters * 0.621371 / 0.264172)
    return miles_per_gallon

def miles_gallon_to_liters_100km(miles):
    liters_per_100km = 100 / (miles * 1609.344 / 3.785411784)
    return liters_per_100km

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))