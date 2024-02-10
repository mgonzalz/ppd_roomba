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
            else:
                messagebox.showerror('Error', 'Los valores deben ser positivos.')
        except ValueError:
            messagebox.showerror('Error', 'Los valores deben ser numéricos.')
    else:
        messagebox.showerror('Error', 'Todos los campos son obligatorios.')


def add_object(hab_var, nombre_var, x_var, y_var, coord_x_var, coord_y_var):
    hab = hab_var.get()
    nombre = nombre_var.get()
    x = x_var.get()
    y = y_var.get()
    coord_x = coord_x_var.get()
    coord_y = coord_y_var.get()

    if hab and nombre and x and y and coord_x and coord_y:
        try:
            x = float(x)
            y = float(y)
            coord_x = float(coord_x)
            coord_y = float(coord_y)

            if x > 0 and y > 0:
                for habitacion in habitaciones:
                    if habitacion.nombre == hab:
                        habitacion.add_objeto(nombre, x, y, coord_x, coord_y)

                        for var in [hab_var, nombre_var, x_var, y_var, coord_x_var, coord_y_var]:
                            var.set('')

                        messagebox.showinfo('Agregado', f'Objeto {nombre} agregado con éxito en la habitación {hab}.', icon=messagebox.INFO)
                        break
                else:
                    messagebox.showerror('Error', f'La habitación {hab} no existe.', icon=messagebox.ERROR)
        except ValueError:
            messagebox.showerror('Error', 'Los valores deben ser numéricos positivos.', icon=messagebox.ERROR)
    else:
        messagebox.showerror('Error', 'Todos los campos son obligatorios.', icon=messagebox.ERROR)
