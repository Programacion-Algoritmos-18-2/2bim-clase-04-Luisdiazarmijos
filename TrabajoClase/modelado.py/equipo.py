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
        self.nombres =nom
        pass
    
    def obtener_nombres(self):
        return self.nombres
        pass
    
    def agregar_ciudad(self, ciu):
        self.ciudad = ciu
    
    def obtener_ciudad(self):
        return self.ciudad
        pass
    def agregar_campeonatos(self, camp):
        self.campeonatos=int(camp)
        pass
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

class Operaciones(object):
    
    def __init__(self, listado):
        self.listado_equipos = listado

    def ordenar(self):
        """
            https://docs.python.org/3/howto/sorting.html
            >>> sorted(student_objects, key=lambda student: student.age)   # sort by age
        """
        return sorted(self.listado_estudiantes, key=lambda estudiante: estudiante.nombres)