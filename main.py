from tkinter import *
from modulos.utils import *

# CONFIGURACIÓN ROOT
root = Tk()
root.title('Roomba Simulator')
root.geometry('800x600')
root.iconbitmap('img/roomba.ico')

title = Label(root, text='Roomba Simulator: Habitaciones rectangulares/cuadradas', font=('Modern', 20, 'bold'))
title.grid(row=0, column=0, columnspan=2, pady=20, sticky='nsew')

# INFORMACIÓN
frame = Frame(root, width=30)
frame.grid(row=1, column=0, sticky='w')

    # HABITACIÓN
nombre = StringVar()
x = StringVar()
y = StringVar()

Label(frame, text='Nombre de la habitación: ').grid(row=0, column=0, padx=10, pady=10, sticky='w')
Entry(frame, justify='right', width=15, textvariable=nombre).grid(row=0, column=1)
Label(frame, text='m').grid(row=0, column=2, sticky='w')

Label(frame, text='Ancho de la habitación: ').grid(row=1, column=0, padx=10, pady=10, sticky='w')
Entry(frame, justify='right', width=15, textvariable=x).grid(row=1, column=1)
Label(frame, text='m').grid(row=1, column=2, sticky='w')

Label(frame, text='Alto de la habitación: ').grid(row=2, column=0, padx=10, pady=10, sticky='w')
Entry(frame, justify='right', width=15, textvariable=y).grid(row=2, column=1)
Label(frame, text='m').grid(row=2, column=2, sticky='w')

button_hab = Button(frame, text='Agregar habitación', bg='#B7AEA1', fg='white', border=0, width=4, command=lambda:add_habitacion(nombre, x, y))
button_hab.grid(row=3, column=0, columnspan=2, padx=15, pady=10, sticky='nsew')

    # OBJETO

root.mainloop()
