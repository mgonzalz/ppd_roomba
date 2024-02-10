from tkinter import *
from modulos.utils import *

# CONFIGURACIÓN ROOT
root = Tk()
root.title('Roomba Simulator')
root.geometry('800x600')
root.iconbitmap('img/roomba.ico')

title = Label(root, text='Roomba Simulator: Habitaciones rectangulares/cuadradas', font=('Modern', 20, 'bold'))
title.grid(row=0, column=0, columnspan=2, pady=20, sticky='nsew')

# VISUALIZACIÓN DE HABITACIONES CON OBJETOS
frame3 = Frame(root, padx=10, pady=10)
frame3.grid(row=1, column=1, sticky='nsew', rowspan=2)
frame3.grid_rowconfigure(1, weight=1)
frame3.grid_columnconfigure(2, weight=1)

canvas = Canvas(frame3, bg="white", bd=1, highlightthickness=1, relief='ridge')
canvas.grid(row=1, column=2, sticky='nsew')

# INFORMACIÓN: Habitación
frame = Frame(root, width=10)
frame.grid(row=1, column=0, sticky='w')

    # HABITACIÓN
nombre = StringVar()
x = StringVar()
y = StringVar()

Label(frame, text='Nombre de la habitación: ', width=20).grid(row=0, column=0, padx=10, pady=10, sticky='w')
Entry(frame, justify='right', width=15, textvariable=nombre).grid(row=0, column=1)

Label(frame, text='Ancho de la habitación: ').grid(row=1, column=0, padx=10, pady=10, sticky='w')
Entry(frame, justify='right', width=15, textvariable=x).grid(row=1, column=1)
Label(frame, text='m').grid(row=1, column=2, sticky='w')

Label(frame, text='Alto de la habitación: ').grid(row=2, column=0, padx=10, pady=10, sticky='w')
Entry(frame, justify='right', width=15, textvariable=y).grid(row=2, column=1)
Label(frame, text='m').grid(row=2, column=2, sticky='w')

button_hab = Button(frame, text='Agregar habitación', bg='#B7AEA1', fg='white', border=0, width=4, command=lambda:add_habitacion(nombre, x, y, canvas))
button_hab.grid(row=3, column=0, columnspan=2, padx=15, pady=10, sticky='nsew')

# INFORMACIÓN: Objeto
frame2 = Frame(root, width=10)
frame2.grid(row=2, column=0, sticky='w')
    # OBJETO
hab_obj = StringVar()
nombre_obj= StringVar()
x_obj = StringVar()
y_obj = StringVar()
coord_x = StringVar()
coord_y = StringVar()

Label(frame2, text='Habitación: ', width=20, anchor='w').grid(row=0, column=0, padx= 10, pady=10)
Entry(frame2, justify='right', width=15, textvariable=hab_obj).grid(row=0, column=1)

Label(frame2, text='Nombre del objeto: ').grid(row=1, column=0, padx=10, pady=10, sticky='w')
Entry(frame2, justify='right', width=15, textvariable=nombre_obj).grid(row=1, column=1)

Label(frame2, text='Ancho del objeto: ').grid(row=2, column=0, padx=10, pady=10, sticky='w')
Entry(frame2, justify='right', width=15, textvariable=x_obj).grid(row=2, column=1)
Label(frame2, text='m').grid(row=2, column=2, sticky='w')

Label(frame2, text='Alto del objeto: ').grid(row=3, column=0, padx=10, pady=10, sticky='w')
Entry(frame2, justify='right', width=15, textvariable=y_obj).grid(row=3, column=1)
Label(frame2, text='m').grid(row=3, column=2, sticky='w')

Label(frame2, text='Coordenada X: ').grid(row=4, column=0, padx=10, pady=10, sticky='w')
Entry(frame2, justify='right', width=15, textvariable=coord_x).grid(row=4, column=1)

Label(frame2, text='Coordenada Y: ').grid(row=5, column=0, padx=10, pady=10, sticky='w')
Entry(frame2, justify='right', width=15, textvariable=coord_y).grid(row=5, column=1)

button_obj = Button(frame2, text='Agregar objeto', bg='#B7AEA1', fg='white', border=0, width=4, command=lambda:add_object(hab_obj, nombre_obj, x_obj, y_obj, coord_x, coord_y))
button_obj.grid(row=6, column=0, columnspan=2, padx=15, pady=10, sticky='nsew')


root.mainloop()
