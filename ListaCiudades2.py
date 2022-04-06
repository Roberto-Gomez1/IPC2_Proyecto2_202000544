class ciudades2:
    def __init__(self, ciudad,tipo,poder):
        self.ciudad = ciudad
        self.tipo = tipo
        self.poder =poder

class nodo:
    def __init__(self,ciudades = None, siguiente = None):
        self.ciudades = ciudades
        self.siguiente= siguiente

class listaSimple2:
    def __init__(self):
        self.primero= None

    def insertar(self, ciudad):
        if self.primero is None:
            self.primero = nodo(ciudades=ciudad)
            return
        actual = self.primero
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nodo(ciudades=ciudad)

    def mostrar(self):
        actual = self.primero
        while actual != None:
            if actual.ciudades.tipo is None:
                print("AuxCiudad: ", actual.ciudades.ciudad)
            actual = actual.siguiente
    def mostrar2(self):
        actual = self.primero
        while actual != None:
            if actual.ciudades.tipo =="ChapinFighter":
                print("AuxRobot: ", actual.ciudades.ciudad,"Tipo:",actual.ciudades.tipo,"Poder:",actual.ciudades.poder)
            elif actual.ciudades.tipo =="ChapinRescue":
                print("AuxRobot: ", actual.ciudades.ciudad,"Tipo:",actual.ciudades.tipo,"Poder:",actual.ciudades.poder)
            actual = actual.siguiente