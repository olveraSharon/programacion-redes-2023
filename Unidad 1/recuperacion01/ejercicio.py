#Nombre: Sharon Michelle Olvera Ibarra
#Asignatura: Programación de redes
#Descripcion:Dentro del sript crear un diccionario llamado asignatura donde la clave sea
#el nombre de la asignatura y su valor un arreglo vacio. Iterar por cada clave del diccionario
#y de acuerdo a cada una de las unidades tematicas crear una lista de tus calificaciónes hasta el momento 
#Crear una función que tome como argumento un valor y despliegue una línea de asteriscos
#de acuerdo a la calificación.
#Crear una función qué tenga como parámetros el nombre de la asignatura y las lista de
#calificaciones, e invoque a la función del paso 7 para crear un histograma
#Iterar por cada elemento del diccionario y desplegar sus histogramas
#Nota: solo las primeras calificaciones son reales...

asignatura = {}

asignatura ['programacion de redes'] = []
asignatura ['conexion de redes wan'] = []
asignatura ['configuracion de servidores'] = []
asignatura ['ingles'] = []

asignatura ['programacion de redes'] = [6, 8, 8]
asignatura ['conexion de redes wan'] = [9, 9, 9]
asignatura ['configuracion de servidores'] = [8, 8, 9]
asignatura ['ingles'] = [9, 9, 9]

def ast (calificacion):
    print ('*' * calificacion)

def histograma (asignatura, calif):
    print(asignatura + "hisograma")
    for calificacion in calif :
        ast(calificacion)

for key, value in asignatura.items():
    histograma(key, value)








