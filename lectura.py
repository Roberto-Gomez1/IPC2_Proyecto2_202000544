import xml.etree.ElementTree as ET
from ListaCiudades import ciudades, listaSimple
from ListaCiudades2 import ciudades2
from ListaRobot import listaRobot, robots
from ListaRuta import listarutas, rutas
from NodoInterno import NodoInterno
from MatrizDispersa import MatrizDispersa

class lectura:
    
    def leer(entrada):
        robo = listaRobot()
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
                            #print(int(numero),int(it1),'*')
                            temporal.patrones.insertar(n1)
                        if ii == "C":
                            n2 = NodoInterno(int(numero),int(it1),'C')
                            #print(int(numero),int(it1),'C')
                            temporal.patrones.insertar(n2)
                        if ii == "R":
                            n3 = NodoInterno(int(numero),int(it1),'R')
                            #print(int(numero),int(it1),'R')
                            temporal.patrones.insertar(n3)
                        if ii == "E":
                            n4 = NodoInterno(int(numero),int(it1),'E')
                            #print(int(numero),int(it1),'E')
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
                x=0
                for n in uu.iter('nombre'):
                    x+=1
                    nombre = uu[x-1].text
                    tipo = uu[x-1].attrib['tipo']
                    if tipo == 'ChapinRescue':
                        aux= robots(x,nombre,tipo,0)
                        robo.insertar(aux)
                        pass
                    else:
                        capacidad= uu[x-1].attrib['capacidad']
                        aux1= robots(x,nombre,tipo,capacidad)
                        robo.insertar(aux1)
        robo.mostrar()
        listaCiudades.mostrar()


    def pru(entrada):
        url = listarutas()
        tree = ET.parse(entrada)
        root = tree.getroot()
        auxiliar = rutas(entrada)
        url.insertar(auxiliar)
        print("-------Ciudades a elegir-------------")
        for item in root: 
            prueba =item.iter('ciudad')      
            for aa in prueba:
                
                ciudad = aa[0].text
                print(ciudad)
                temp = ciudades2(ciudad,None,'')
                auxiliar.ciudad.insertar(temp)
                it=0
                for ee in aa.iter('fila'):
                    it +=1
                    numero = aa[it].attrib['numero']
                    fila = aa[it].text
                    it1 = 0
                    for ii in str(fila):
                        it1+=1
                        if ii == "C":
                            print("Punto de Civiles: ","X: ",int(numero),"Y: ",int(it1))
                            #auxiliar.ciudad.insertar(n2)
                        if ii == "E":
                            print("Punto de Entrada: ","X:", int(numero),"Y: ",int(it1))
                            #auxiliar.ciudad.insertar(n4)   
            for uu in item.iter('robot'):
                    x=0
                    for n in uu.iter('nombre'):
                        x+=1
                        nombre = uu[x-1].text
                        tipo = uu[x-1].attrib['tipo']
                        if tipo == 'ChapinRescue':
                            aux= ciudades2(nombre,tipo,0)
                            auxiliar.ciudad.insertar(aux)
                            pass
                        else:
                            capacidad= uu[x-1].attrib['capacidad']
                            aux1= ciudades2(nombre,tipo,capacidad)
                            auxiliar.ciudad.insertar(aux1)
        #url.mostrar()
        print("-------Misiones a elegir:-------------")
        print("Rescate")
        print("Extraccion")
        print("-------Robots a Elegir-------------")
        auxiliar.ciudad.mostrar2()
        auxiliar.ciudad.mostrar3()
        

    def generar(entrada,nombre):
        url = listarutas()
        robo = listaRobot()
        listaCiudades = listaSimple()
        tree = ET.parse(entrada)
        root = tree.getroot()
        for item in root: 
            prueba =item.iter('ciudad')      
            for aa in prueba:
                ciudad = aa[0].text
                if nombre == ciudad:
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
                                #print(int(numero),int(it1),'*')
                                temporal.patrones.insertar(n1)
                            if ii == "C":
                                n2 = NodoInterno(int(numero),int(it1),'C')
                                #print(int(numero),int(it1),'C')
                                temporal.patrones.insertar(n2)
                            if ii == "R":
                                n3 = NodoInterno(int(numero),int(it1),'R')
                                #print(int(numero),int(it1),'R')
                                temporal.patrones.insertar(n3)
                            if ii == "E":
                                n4 = NodoInterno(int(numero),int(it1),'E')
                                #print(int(numero),int(it1),'E')
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
                    fkj = temporal.patrones.reC()
                    xcu = temporal.patrones.reEntrada()
                    #temporal.patrones.camino(xcu,fkj)
                    temporal.patrones.graficarDot(ciudad)
                for uu in item.iter('robot'):
                    x=0
                    for n in uu.iter('nombre'):
                        x+=1
                        nombre = uu[x-1].text
                        tipo = uu[x-1].attrib['tipo']
                        if tipo == 'ChapinRescue':
                            aux= robots(x,nombre,tipo,0)
                            robo.insertar(aux)
                            pass
                        else:
                            capacidad= uu[x-1].attrib['capacidad']
                            aux1= robots(x,nombre,tipo,capacidad)
                            robo.insertar(aux1)
        
        #robo.mostrar()
        #listaCiudades.mostrar()
