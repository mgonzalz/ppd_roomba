class Zona():
    def __init__(self, x1, x2, y1, y2, xobjeto, yobjeto):
        if all(isinstance(coord, float) for coord in (x1, x2, y1, y2, xobjeto, yobjeto)):
            self.x1 = x1
            self.x2 = x2
            self.y1 = y1
            self.y2 = y2
            self.xobjeto = xobjeto
            self.yobjeto = yobjeto
        else:
            raise ValueError("Los valores deben ser flotantes")
    def get_area(self):
        return (self.x2 - self.x1) * (self.y2 - self.y1)
    def get_x(self):
        return self.x2 - self.x1
    def get_y(self):
        return self.y2 - self.y1


class Seccion(Zona):
    def __init__(self, x1, x2, y1, y2, xobjeto, yobjeto, xseccion, yseccion):
        super().__init__(x1, x2, y1, y2, xobjeto, yobjeto)
        self.xseccion = xseccion
        self.yseccion = yseccion
