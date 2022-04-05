import sys
import tkinter as tk
from tkinter import ttk
from tkinter import *
import tkinter.font as tkFont
from tkinter import filedialog
from help import Leer_Archivo
import webbrowser
from lectura import lectura

arch=''
def boton_cargaArchivo_command():
    
    arch = Leer_Archivo()
    ruta.insert(tk.INSERT, arch)
    #print(arch)
    #lectura.leer(arch)
    lectura.pru(arch)

def salir_interfaz():
    sys.exit()

def generar_espe():
    nombreciudad = textt.get(1.0,'end').replace(' ','').replace('\n','')
    direccion = ruta.get(1.0,'end').replace(' ','').replace('\n','')
    lectura.generar(direccion,nombreciudad)
    #print(nombreciudad)
    #print(direccion)



root =Tk()
root.title('Menu')
fuente = tkFont.Font(family='Arial', size = 12)

fram = ttk.Frame(root)
framee = ttk.Frame(fram, width=360, height=180)


cArchivo=tk.Button(root)
cArchivo["font"] = fuente
cArchivo["justify"] = "center"
cArchivo["text"] = "Cargar archivo"
cArchivo.place(x=40,y=10,width=121,height=50)
cArchivo["command"] = boton_cargaArchivo_command 

textt = tk.Text(root)
textt["font"] = fuente
textt.place(x=200,y=30,width= 100, height=30)


ruta = tk.Text(root)
ruta["font"] = fuente
ruta.place(x=600,y=30,width= 100, height=30)

salir=tk.Button(root)
salir["font"] = fuente
salir["justify"] = "center"
salir["text"] = "Salir del Sistema"
salir.place(x=40,y=80,width=121,height=50)
salir["command"] = salir_interfaz 



generar = tk.Button(root)
generar["font"] = fuente
generar["justify"] = "center"
generar["text"] = "Generar"
generar.place(x=190,y=80,width=121,height=50)
generar["command"] = generar_espe 


fram.pack()
framee.pack()



root.mainloop()