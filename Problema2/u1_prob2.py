#Autor: Sharon Michelle Olvera Ibarra
#Descripción: Escribir un programa en Python que almacene las asignaturas que un estudiante de Infraestructura en
# redes digitales lleva durante el cuarto cuatrimestre (por ejemplo, Probabilidad y Estadística, Electrónica para IDC 
#Física, Conexión de redes WAN, Administración de servidores I, Programación de Redes e inglés IV), pregunta la nota 
#que ha sacado en la unidad I de cada asignatura, después las muestre en pantalla con el mensaje “En <asignatura> has
# sacado <nota>” donde asignatura es cada una de las asignaturas de la lista y <nota> cada una de las correspondientes
# notas.
#Fecha:02/10/2023

# Definir la lista de asignaturas
asignaturas = [
    "Probabilidad y Estadística",
    "Electrónica para IDC Física",
    "Conexión de redes WAN",
    "Administración de servidores I",
    "Programación de redes",
    "Ingles IV"
]
# Agregar notas de asignatura
notas = {}
# Solicitar la nota de cada materia en unidad I
for asignatura in asignaturas:
    nota = float(input(f"Ingrese la nota de la unidad I para {asignatura}: "))
    notas[asignatura] = nota

# Mostrar en la pantalla las notas de cada materia
for asignatura, nota in notas.items():
    print(f"En {asignatura} has sacado {nota}")


