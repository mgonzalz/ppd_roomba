from .classZona import Zona
from tkinter import messagebox, END
habitaciones = [] # Lista que contiene todas las habitaciones.

def add_habitacion(nombre_hab, x_hab, y_hab, canvas):
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
                display_habitacion(nombre, x, y, canvas)
                for i in [x_hab, y_hab , nombre_hab]:
                    i.set('')
                messagebox.showinfo('Agregado', f'Habitación {nombre} agregada con éxito.', icon=messagebox.INFO)
            else:
                messagebox.showerror('Error', 'Los valores deben ser positivos.')
        except ValueError:
            messagebox.showerror('Error', 'Los valores deben ser numéricos.')
    else:
        messagebox.showerror('Error', 'Todos los campos son obligatorios.')


def add_object(hab_var, nombre_var, x_var, y_var, coord_x_var, coord_y_var, canvas):
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
                        display_objecto(nombre, x, y, coord_x, coord_y, canvas)
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


def display_habitacion(nombre, ancho ,alto, canvas):
    x1, y1, x2, y2 = 0, 0, ancho * 10, alto * 10 # 1 metro equivale a 10 pixeles.
    canvas.create_rectangle(x1, y1, x2, y2, fill='lightgrey')
    canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text=f'{nombre}:\n{ancho}x{alto}\nÁrea: m²', font=('Helveltica', 10, 'bold'), anchor='center', justify='center')


def display_objecto(nombre, ancho, alto, coord_x, coord_y, canvas):
    x1, y1, x2, y2 = coord_x * 10, coord_y * 10, (coord_x + ancho) * 10, (coord_y + alto) * 10
    canvas.create_rectangle(x1, y1, x2, y2, fill='plum2')
    canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text=f'{nombre}', justify='center', anchor='center', font=('Helveltica', 10, 'bold'), fill='white')
