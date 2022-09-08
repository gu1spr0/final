import tkinter as tk
from tkinter import messagebox
import operaciones as op

global ESTADO_ACTIVO
global ESTADO_INACTIVO

ESTADO_ACTIVO = 'AC'
ESTADO_INACTIVO = 'AN'

def agregar_materia():
    nombre = txt_nombre.get()
    sigla = txt_sigla.get()
    carga = txt_carga.get()
    materia = (nombre, sigla, carga, ESTADO_ACTIVO)
    id = op.insertar_materia(materia)
    txt_nombre.delete(0, 'end')
    txt_sigla.delete(0, 'end')
    txt_carga.delete(0, 'end')
    messagebox.showinfo("Materia insertada correctamente", f'id = {id}')


ventana = tk.Tk()
ventana.config(width=215, height=200)
ventana.title("Administración de inscripciones")

lbl_nombre = tk.Label(text="Ingrese nombre de materia:")
lbl_nombre.place(x=5, y=10)
txt_nombre = tk.Entry()
txt_nombre.place(x=5, y=35, width=200, height=25)

lbl_sigla = tk.Label(text="Ingrese sigla de materia:")
lbl_sigla.place(x=5, y=60)
txt_sigla = tk.Entry()
txt_sigla.place(x=5, y=85, width=200, height=25)

lbl_carga = tk.Label(text="Ingrese carga horaria:")
lbl_carga.place(x=5, y=110)
txt_carga = tk.Entry()
txt_carga.place(x=5, y=135, width=200, height=25)

btn_aceptar = tk.Button(text="Aceptar", command=agregar_materia)
btn_aceptar.place(x=5,y=165,width=90,height=25)

btn_aceptar = tk.Button(text="Cancelar")
btn_aceptar.place(x=115,y=165,width=90,height=25)

ventana.mainloop()