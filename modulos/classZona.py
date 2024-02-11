class Zona():
    def __init__(self, nombre, x, y):
        if all(isinstance(coord, float) for coord in (x,y)) and isinstance(nombre, str):
            self.nombre = nombre
            self.x = x
            self.y = y
            self.objeto = [] # Objetos innaccesibles para el Roomba.
        else:
            raise ValueError("Los valores, ancho y alto, deben ser flotantes y el nombre debe ser un string.")
    def add_objeto(self, nombre_obj, xobj, yobj, coord_x, coord_y): #xobj, yobj = ancho y alto del objeto; coord_x, coord_y = coordenadas cartesianas del objeto.
        if all(isinstance(coord, float) for coord in (xobj, yobj, coord_x, coord_y)) and isinstance(nombre_obj, str):
            self.objeto.append(Objeto(nombre_obj, xobj, yobj, coord_x, coord_y))
        else:
            raise ValueError("Los valores, ancho y alto junto a las coordenadas, deben ser flotantes y el nombre debe ser un string.")
    def get_area(self):
        area = self.x * self.y
        for obj in self.objeto:
            area -= obj.get_area()
        return area
    def __str__(self):
        return f'Habitación: {self.nombre}\nAncho: {self.x} m\nAlto: {self.y} m\nÁrea: {self.get_area()} m²\nObjetos: {len(self.objeto)}\n\n'


class Objeto(Zona):
    def __init__(self, nombre, x, y, coord_x, coord_y):
        self.nombre = nombre
        self.x = x
        self.y = y
        self.coord_x = coord_x
        self.coord_y = coord_y
    def get_area(self):
        return self.x * self.y
    def __str__(self):
        return f'Objeto: {self.nombre}\nAncho: {self.x} m\nAlto: {self.y} m\nÁrea: {self.get_area()} m²\nCoordenadas: ({self.coord_x}, {self.coord_y})\n\n'
