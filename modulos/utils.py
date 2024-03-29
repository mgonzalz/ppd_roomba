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
                if habitaciones:
                    habitacion.coord_x = habitaciones[-1].coord_x + habitaciones[-1].x*10 #separación entre habitaciones.
                habitaciones.append(habitacion)
                display_habitacion(nombre, x, y, canvas)
                for i in [x_hab, y_hab , nombre_hab]:
                    i.set('')
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
                        canvas.itemconfig(habitacion.id_canvas, text=f'{habitacion.nombre}:\n{habitacion.x}x{habitacion.y}\nÁrea: {habitacion.get_area()}m²\nLimpieza: {habitacion.get_tiempo():.2f}s')
                        display_objecto(nombre, x, y, coord_x, coord_y, canvas)
                        for var in [hab_var, nombre_var, x_var, y_var, coord_x_var, coord_y_var]:
                            var.set('')
                        break
                else:
                    messagebox.showerror('Error', f'La habitación {hab} no existe.', icon=messagebox.ERROR)
        except ValueError:
            messagebox.showerror('Error', 'Los valores deben ser numéricos positivos.', icon=messagebox.ERROR)
    else:
        messagebox.showerror('Error', 'Todos los campos son obligatorios.', icon=messagebox.ERROR)


def display_habitacion(nombre, ancho ,alto, canvas):
    for i in habitaciones:
        if i.nombre == nombre:
            x, y = i.coord_x, i.coord_y
    x1, y1 = x, y
    x2, y2 = x1 + ancho * 10, y1 + alto * 10 # 1 metro equivale a 10 pixeles.
    area = habitaciones[-1].get_area() # al añadir la habitación, se trata del último elemento de la lista.
    tiempo = habitaciones[-1].get_tiempo()
    canvas.create_rectangle(x1, y1, x2, y2, fill='lightgrey')
    text = canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text=f'{nombre}:\n{ancho}x{alto}\nÁrea: {area}m²\nLimpieza: {tiempo:.2f}s', font=('Helveltica', 10, 'bold'), anchor='center', justify='center')
    habitaciones[-1].id_canvas = text # id en el objeto para modificar el texto en el canvas (área).

def display_objecto(nombre, ancho, alto, coord_x, coord_y, canvas):
    x1, y1 = 0, 0
    for i in habitaciones:
        for obj in i.objeto:
            if obj.nombre == nombre:
                x1, y1 = i.coord_x, i.coord_y
    x2, y2 = x1 + (coord_x + ancho) * 10, y1 + (coord_y + alto) * 10
    x1 += coord_x * 10
    y1 += coord_y * 10
    canvas.create_rectangle(x1, y1, x2, y2, fill='plum2')
    canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text=f'{nombre}', justify='center', anchor='center', font=('Helveltica', 10, 'bold'), fill='white')
