#Creamos la clase padre
class Equipo(object):
    """docstring for Equipo"""
    #Definimos los atributos
    def __init__(self, nom, ciu, camp, numju):
        self.nombres = nom
        self.ciudad = ciu
        self.campeonatos = int(camp)
        self.numJugadores = int(numju)
     #Agregamos los metodos agregar y obtener
    def agregar_nombres(self, nom):
        self.nombres = nom
    
    def obtener_nombres(self):
        return self.nombres
        
    
    def agregar_ciudad(self, ciu):
        self.ciudad = ciu
    
    def obtener_ciudad(self):
        return self.ciudad
        
    def agregar_campeonatos(self, camp):
        self.campeonatos=int(camp)
    
    def obtener_campeonatos(self):
        return self.campeonatos
    
    def agregar_numJugadores(self, numju):
        self.numJugadores = int(numju)
    
    def obtener_numJugadores(self):
        return self.numJugadores
    
    def __str__(self):
        return "%s %s %d %d "%(self.obtener_nombres(), self.obtener_ciudad(), self.obtener_campeonatos(), self.obtener_numJugadores())

    def __repr__(self):
        return "%s %s %d %.2f "%(self.obtener_nombres(), self.obtener_ciudad(), self.obtener_campeonatos(), self.obtener_numJugadores())
#Creamos la clase Operaciones
class Operaciones(object):
    
    def __init__(self, listado):
        self.listado_equipos = listado
  #Metodo Ordenar nombres
    def ordenar_nombres(self):
        
        return sorted(self.listado_equipos, key=lambda equipo: equipo.obtener_nombres())
   #Metodo Ordenar Campeonato
    def ordenar_campeonatos(self):

        return sorted(self.listado_equipos, key=lambda equipo: equipo.obtener_campeonatos())