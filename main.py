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
    ruta.delete(1.0,'end')
    arch = Leer_Archivo()
    ruta.insert(tk.INSERT, arch)
    #print(arch)
    #lectura.leer(arch)
    lectura.pru(arch)

def salir_interfaz():
    sys.exit()

def generar_espe():
    
    nombreciudad = textt.get(1.0,'end').replace(' ','').replace('\n','')
    aux_robot = nombrerobot.get(1.0,'end').replace(' ','').replace('\n','')
    aux_mision = mision.get(1.0,'end').replace(' ','').replace('\n','')
    direccion = ruta.get(1.0,'end').replace(' ','').replace('\n','')
    aux_e = x_E.get(1.0,'end').replace(' ','').replace('\n','')
    aux_e2= y_E.get(1.0,'end').replace(' ','').replace('\n','')
    aux_c= x_C.get(1.0,'end').replace(' ','').replace('\n','')
    aux_c2= y_C.get(1.0,'end').replace(' ','').replace('\n','')
    print("Se ha elegido la ciudad de: "+nombreciudad)
    print("La mision a realizar es: "+aux_mision)
    print("El robot elegido es: "+aux_robot)
    print("El punto de entrada es: "+aux_e+","+aux_e2)
    print("El Punto de Civiles es: "+aux_c+","+aux_c2)
    lectura.generar(direccion,nombreciudad)



root =Tk()
root.title('Menu')
fuente = tkFont.Font(family='Arial', size = 12)

fram = ttk.Frame(root)
framee = ttk.Frame(fram, width=580, height=210)


cArchivo=tk.Button(root)
cArchivo["font"] = fuente
cArchivo["justify"] = "center"
cArchivo["text"] = "Cargar archivo"
cArchivo.place(x=40,y=10,width=121,height=50)
cArchivo["command"] = boton_cargaArchivo_command 

label = tk.Label(root)
label["font"] = fuente
label["justify"] = "center"
label["text"] = "Ciudad"
label.place(x=215,y=12,width= 50, height=15)

textt = tk.Text(root)
textt["font"] = fuente
textt.place(x=190,y=30,width= 120, height=30)

label2 = tk.Label(root)
label2["font"] = fuente
label2["justify"] = "center"
label2["text"] = "Mision"
label2.place(x=325,y=12,width= 50, height=15)

mision = tk.Text(root)
mision["font"] = fuente
mision.place(x=320,y=30,width= 100, height=30)

label3 = tk.Label(root)
label3["font"] = fuente
label3["justify"] = "center"
label3["text"] = "Robot"
label3.place(x=455,y=12,width= 50, height=15)


nombrerobot = tk.Text(root)
nombrerobot["font"] = fuente
nombrerobot.place(x=430,y=30,width= 120, height=30)

label4 = tk.Label(root)
label4["font"] = fuente
label4["justify"] = "center"
label4["text"] = "Punto Entrada"
label4.place(x=190,y=125,width= 100, height=15)

x_E = tk.Text(root)
x_E["font"] = fuente
x_E.place(x=190,y=150,width= 30, height=30)

y_E = tk.Text(root)
y_E["font"] = fuente
y_E.place(x=235,y=150,width= 30, height=30)

label5 = tk.Label(root)
label5["font"] = fuente
label5["justify"] = "center"
label5["text"] = "Punto Civil"
label5.place(x=310,y=125,width= 100, height=15)

x_C = tk.Text(root)
x_C["font"] = fuente
x_C.place(x=320,y=150,width= 30, height=30)

y_C = tk.Text(root)
y_C["font"] = fuente
y_C.place(x=365,y=150,width= 30, height=30)

ruta = tk.Text(root)
ruta["font"] = fuente
ruta.place(x=900,y=30,width= 100, height=30)

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
generar.place(x=270,y=55,width=121,height=50)
generar["command"] = generar_espe 


fram.pack()
framee.pack()



root.mainloop()