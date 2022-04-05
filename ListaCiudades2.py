class ciudades2:
    def __init__(self, ciudad):
        self.ciudad = ciudad


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
            print("AuxCiudad: ", actual.ciudades.ciudad)
            actual = actual.siguiente