from tkinter import *


# CONFIGURACIÓN ROOT
root = Tk()
root.title('Roomba Simulator')
root.geometry('800x600')
root.config(bg='white')
root.iconbitmap('img/roomba.ico')

title = Label(root, text='Roomba Simulator: Habitaciones rectangulares/cuadradas', font=('Helveltica', 20, 'bold'), bg='white')
title.grid(row=0, column=0, pady=20, sticky='nsew')

# CONFIGURACIÓN MEDIDAS
x = StringVar()
y = StringVar()

datos = Frame(root, bg='white', width=200, height=400)
datos.grid(row=1, column=0, pady=20, sticky=NW)

    # ANCHO: X
x_title = Label(datos, text='Ancho:', font=('Helveltica', 15), bg='white')
x_title.grid(row=0, column=0, pady=20)

x = Entry(datos, font=('Helveltica', 15), bg='white', justify='right')
x.grid(row=0, column=1, pady=20)

Label(datos, text='m', font=('Helveltica', 15), bg='white').grid(row=0, column=2, pady=20)

    # ALTURA: Y
y_title = Label(datos, text='Alto:', font=('Helveltica', 15), bg='white')
y_title.grid(row=1, column=0, pady=20)

y = Entry(datos, font=('Helveltica', 15), bg='white', justify='right')
y.grid(row=1, column=1, pady=20)

Label(datos, text='m', font=('Helveltica', 15), bg='white').grid(row=1, column=2, pady=20)

    # BOTÓN: CREAR HABITACIÓN
button = Button(datos, text='Crear habitación', font=('Helvetica', 15), bg='white', width=15, height=1)
button.grid(row=0, column=3, rowspan=2, padx=20, pady=20, sticky='nsew')



root.mainloop()
