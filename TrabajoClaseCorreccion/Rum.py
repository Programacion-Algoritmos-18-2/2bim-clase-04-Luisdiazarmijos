#Importamos los paquetes
from paquete_archivos.miarchivo import MiArchivo , MiArchivoEscribir
from modelado.equipo import *
#Creamos un objeto de tipo archivopara leer el archivo
m = MiArchivo()
#Objeto para escribir el archivo
m2= MiArchivoEscribir()
lista = m.obtener_informacion()
lista = [l.split("|") for l in lista]

#Declaramos una lista
lista_equipos =[]

#For para recorrer la lista
for d in lista:
    #Objeto para imprimir 
    p = Equipo(d[0], d[1], d[2], d[3])
 # Usamos el metodo append de las listas se crea una copia de la original
    lista_equipos.append(p)
  
  
operaciones = Operaciones(lista_equipos)
x =int(input("Seleccione la opcion que desee ingresar:\n 1  Si desea ordenar por Nombre\n 2  Si desea ordenar por Campeonato\n "))
if x==1:
    lista_equipos2 = operaciones.ordenar_nombres()
if x==2:
    lista_equipos2 = operaciones.ordenar_campeonatos()

    
for i in lista_equipos2:
    m2.agregar_informacion(i)
    print(i)
m.cerrar_archivo()
m2.cerrar_archivo()


        





   

