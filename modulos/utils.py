from .classZona import Zona, Objeto
from tkinter import messagebox, END
habitaciones = [] # Lista que contiene todas las habitaciones.

def add_habitacion(nombre_hab, x_hab, y_hab):
    nombre = nombre_hab.get()
    x = x_hab.get()
    y = y_hab.get()
    if nombre and x and y:
        try:
            x = float(x)
            y = float(y)
            if x > 0 and y > 0:

                habitacion = Zona(nombre, x, y)
                habitaciones.append(habitacion)
                for i in [x_hab, y_hab , nombre_hab]:
                    i.set('')
                messagebox.showinfo('Agregado', f'Habitación {nombre} agregada con éxito.', icon=messagebox.INFO)
        except ValueError:
            messagebox.showerror('Error', 'Los valores deben ser numéricos positivos.')
    else:
        messagebox.showerror('Error', 'Todos los campos son obligatorios.')
