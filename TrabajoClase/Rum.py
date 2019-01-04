#Importamos los paquetes
from paquete_archivos.miarchivo import MiArchivo
from modelado.equipo import equipo, Operaciones
#Creamos un objeto de tipo archivo
m = MiArchivo()

lista = m.obtener_informacion()
lista = [l.split("|") for l in lista]

# print(lista)
#Declaramos una lista
lista = lista[1:]
lista_equipos =[]

#For para recorrer la lista
for d in lista:
    # print(d)
    #Objeto para imprimir 
    p = equipo(d[1], d[2], d[3], d[0])
 # Usamos el metodo append de las listas se crea una copia de la original
    lista_personas.append(p)
    #Creamos un objeto
operaciones = Operaciones(lista_equipo)
#Imprimimos opraciones
print(operaciones)

        





   

