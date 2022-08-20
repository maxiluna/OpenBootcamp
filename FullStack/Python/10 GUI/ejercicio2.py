"""
Este segundo ejercicio, tendréis que crear una 
interfaz sencilla la cual debe de contener una 
lista de elementos seleccionables, también debe 
de tener un label con el texto que queráis.
"""
import tkinter as tk
from tkinter import Listbox, ttk

# ventana
ventana = tk.Tk()
ventana.geometry('300x320')
ventana.resizable(False, False)
ventana.title('Ejercicio 2 - Tema 10')

# Label de Opcion seleccionada
label = ttk.Label(text="Seleccione una opcion")
label.pack(fill='x', padx=5, pady=5)

# Lista de Elementos
lista = Listbox(ventana)
lista.insert(1, "Elemento 1")
lista.insert(2, "Elemento 2")
lista.insert(3, "Elemento 3")
lista.insert(4, "Elemento 4")
lista.insert(5, "Elemento 5")
lista.insert(6, "Elemento 6")
lista.insert(7, "Elemento 7")
lista.pack(fill='x', padx=5, pady=5)

ventana.mainloop()
