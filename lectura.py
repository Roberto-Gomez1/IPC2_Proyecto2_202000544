import xml.etree.ElementTree as ET
from ListaCiudades import ciudades, listaSimple
from NodoInterno import NodoInterno

class lectura:
    
    def leer(entrada):
        
        listaCiudades = listaSimple()
        tree = ET.parse(entrada)
        root = tree.getroot()
        for item in root: 
            prueba =item.iter('ciudad')      
            for aa in prueba:
                ciudad = aa[0].text
                filas = aa[0].attrib['filas']
                columnas = aa[0].attrib['columnas']
                temporal = ciudades(ciudad)
                listaCiudades.insertar(temporal)
                it=0
                for ee in aa.iter('fila'):
                    it +=1
                    numero = aa[it].attrib['numero']
                    fila = aa[it].text
                    it1 = 0
                    for ii in str(fila):
                        it1+=1
                        if ii == "*":
                            n1 = NodoInterno(int(numero),int(it1),'*')
                            print(int(numero),int(it1),'*')
                            temporal.patrones.insertar(n1)
                        if ii == "C":
                            n2 = NodoInterno(int(numero),int(it1),'C')
                            print(int(numero),int(it1),'C')
                            temporal.patrones.insertar(n2)
                        if ii == "R":
                            n3 = NodoInterno(int(numero),int(it1),'R')
                            print(int(numero),int(it1),'R')
                            temporal.patrones.insertar(n3)
                        if ii == "E":
                            n4 = NodoInterno(int(numero),int(it1),'E')
                            print(int(numero),int(it1),'E')
                            temporal.patrones.insertar(n4)
                        if ii == " ":
                            n7 = NodoInterno(int(numero),int(it1),' ')
                            temporal.patrones.insertar(n7)
                for oo in aa.iter('unidadMilitar'):
                    it+=1
                    podoer = aa[it].text
                    ubicacionX = aa[it].attrib['fila']
                    ubicacionY = aa[it].attrib['columna']
                    n4 = NodoInterno(int(ubicacionX),int(ubicacionY),'U')
                    temporal.patrones.insertar(n4)
                
                temporal.patrones.graficarDot(ciudad)
            for uu in item.iter('robot'):
                robot = uu.iter('nombre')
                x=0
                for n in robot:
                    x+=1
                    nombre = uu[x-1].text
                    tipo = uu[x-1].attrib['tipo']
                    if tipo == 'ChapinRescue':
                        #print(nombre, tipo)
                        pass
                    else:
                        capacidad= uu[x-1].attrib['capacidad']
        listaCiudades.mostrar()