"""
En este ejercicio tenéis que crear una lista de RadioButton 
que muestre la opción que se ha seleccionado y que contenga 
un botón de reinicio para que deje todo como al principio.
"""
import tkinter as tk
from tkinter import ttk

# ventana
ventana = tk.Tk()
ventana.geometry('300x320')
ventana.resizable(False, False)
ventana.title('Ejercicio 1 - Tema 10')

# Funcion que muestra valor automaticamente
def mostrar_valor():
    label.config(text="Eleccion: " + seleccionar_valor.get())

# Funcion que reinicia valor
def reiniciar_valor():
    label.config(text="Elija una opcion")

seleccionar_valor = tk.StringVar()
opciones = (('Opcion 1'),
         ('Opcion 2'),
         ('Opcion 3'),
         ('Opcion 4'),
         ('Opcion 5'),
         ('Opcion 6'),
         ('Opcion 7'))

# Label de Opcion seleccionada
label = ttk.Label(text="Elija una opcion")
label.pack(fill='x', padx=5, pady=5)

# Lista de RadioButton
for opcion in opciones:
    r = ttk.Radiobutton(
        ventana,
        text=opcion,
        value=opcion,
        variable=seleccionar_valor,
        command=mostrar_valor
    )
    r.pack(fill='x', padx=5, pady=5)

# Boton Reiniciar
button = ttk.Button(
    ventana,
    text="Reiniciar",
    command=reiniciar_valor)
button.pack(fill='x', padx=5, pady=5)

ventana.mainloop()