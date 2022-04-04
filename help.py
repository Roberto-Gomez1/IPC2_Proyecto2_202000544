from tkinter import Tk
from tkinter.filedialog import askopenfilename

def Leer_Archivo():
    raiz1 = Tk
    filename1 = askopenfilename(filetypes=[("Archivo xml","*.xml")])
    return filename1

