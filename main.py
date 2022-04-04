import sys
import tkinter as tk
from tkinter import ttk
from tkinter import *
import tkinter.font as tkFont
from tkinter import filedialog
from help import Leer_Archivo
import webbrowser
from lectura import lectura

def boton_cargaArchivo_command():
    arch = Leer_Archivo()
    print(arch)
    lectura.leer(arch)

def salir_interfaz():
    sys.exit()


def guardar_Archivo():
    Tk().withdraw()
    filedir = filedialog.askopenfilename(filetypes=[("Archivo data","*.form")])
    #texto = textt.get(1.0,'end')
    with open(filedir,"r+",encoding = "utf-8") as f:
        f.truncate(0)
        #f.write(texto)
    



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


guardar=tk.Button(root)
guardar["font"] = fuente
guardar["justify"] = "center"
guardar["text"] = "Guardar archivo"
guardar.place(x=190,y=10,width=121,height=50)
guardar["command"] = guardar_Archivo 



generar=tk.Button(root)
generar["font"] = fuente
generar["justify"] = "center"
generar["text"] = "Salir del Sistema"
generar.place(x=40,y=80,width=121,height=50)
generar["command"] = salir_interfaz 



salir = tk.Button(root)
salir["font"] = fuente
salir["justify"] = "center"
salir["text"] = "Sin opcion"
salir.place(x=190,y=80,width=121,height=50)
#salir["command"] = salir_interfaz 


fram.pack()
framee.pack()



root.mainloop()