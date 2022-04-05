class robots:
    def __init__(self, id,nombre, tipo, poder):
        self.id = id
        self.nombre = nombre
        self.tipo = tipo
        self.poder = poder

class nodoRobo:
    def __init__(self,robots = None, siguiente = None):
        self.robots = robots
        self.siguiente= siguiente

class listaRobot:
    def __init__(self):
        self.primero= None

    def insertar(self, robot):
        if self.primero is None:
            self.primero = nodoRobo(robots=robot)
            return
        actual = self.primero
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nodoRobo(robots=robot)

    def mostrar(self):
        actual = self.primero
        while actual != None:
            print("ID: ", actual.robots.id,"Nombre: ",actual.robots.nombre,"Tipo: ",actual.robots.tipo, "Poder de Pelea:",actual.robots.poder)
            actual = actual.siguiente
        