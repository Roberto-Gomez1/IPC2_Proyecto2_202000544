from ListaCiudades2 import listaSimple2


class rutas:
    def __init__(self, ruta):
        self.ruta = ruta
        self.ciudad = listaSimple2()

class nodo:
    def __init__(self,rutas = None, siguiente = None):
        self.rutas = rutas
        self.siguiente= siguiente

class listarutas:
    def __init__(self):
        self.primero= None

    def insertar(self, ruta):
        if self.primero is None:
            self.primero = nodo(rutas=ruta)
            return
        actual = self.primero
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nodo(rutas=ruta)

    def mostrar(self):
        actual = self.primero
        while actual != None:
            print("Ruta: ", actual.rutas.ruta)
            actual = actual.siguiente