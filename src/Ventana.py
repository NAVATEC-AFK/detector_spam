import tkinter as tk
from tkinter import messagebox

def mostrar_mensaje():
    messagebox.showinfo("Aviso", "Boton Presionado")
ventana = tk.Tk()
ventana.title("Ventana Simple") 

Label = tk.Label(ventana, text = "!Hola Mundo")
Label.pack(pady=10)

boton = tk.Button(ventana, text ="Haz click aquí", command= mostrar_mensaje)
boton.pack(pady=10)

    
ventana.mainloop()

