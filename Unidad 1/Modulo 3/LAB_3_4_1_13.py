#Autor: Sharon Michelle Olvera Ibarra
#Descripción:Lo básico de las listas - Los Beatles
#Fecha: 02/10/2023

# Paso 1: Crea una lista vacía llamada Beatles.
Beatles = []

# Paso 2: Emplea el metodo para agregar los miembros
Beatles.append("John Lennon")
Beatles.append("Paul McCartney")
Beatles.append("George Harrison")

# Paso 3: emplear bucles para pedir al usuario que agregue más miembros.
for i in range(2):
    new_member = input("Agrega un nuevo miembro de la banda: ")
    Beatles.append(new_member)

# Paso 4: usar intrucción para eliminar a Stu Sutcliffe y Pete Best de la lista.
del Beatles[3:5]

# Paso 5: Agregar a Ringo Starr al principio de la lista.
Beatles.insert(0, "Ringo Starr")

# Paso 1
print("Paso 1:", Beatles)

# Paso 2
print("Paso 2:", Beatles)

# Paso 3
print("Paso 3:", Beatles)

# Paso 4
print("Paso 4:", Beatles)

# Paso 5
print("Paso 5:", Beatles)

# Probando la longitud de la lista
print("Los Fav", len(Beatles))
