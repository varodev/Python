import sys

#importamos la clase Image de Pillow
from PIL import Image

def ajustar_0_255(num_entrada):
    numero = int(num_entrada)

    if numero < 0:
        numero = 0
    elif numero >= 256:
        numero =  255

    return numero

class Pixel():
    def __init__(self, image, x, y):
        self.image = image
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def red(self):
        return self.image.px[self._x, self._y][0]

    @red.setter
    def red(self, value):
        rgb = self.image.px[self._x, self._y]
        self.image.px[self._x, self._y] = (ajustar_0_255(value), rgb[1], rgb[2])

    @property
    def green(self):
        return self.image.px[self._x, self._y][1]

    @green.setter
    def green(self, value):
        rgb = self.image.px[self._x, self._y]
        self.image.px[self._x, self._y] = (rgb[0], ajustar_0_255(value), rgb[2])

    @property
    def blue(self):
        return self.image.px[self._x, self._y][2]

    @blue.setter
    def blue(self, value):
        rgb = self.image.px[self._x, self._y]
        self.image.px[self._x, self._y] = (rgb[0], rgb[1], ajustar_0_255(value))

class Imagen():
    def __init__(self, fichero, width=0, height=0):
        
        if fichero:
            self.pil_image = Image.open(fichero).convert("RGB")
            if self.pil_image.mode != 'RGB':
                raise Exception('La imagen no es RGB')
        else:
            raise Exception('Fichero vacío')
            
        self.px = self.pil_image.load()
        size = self.pil_image.size
        self._width = size[0]
        self._height = size[1]
        self.x_actual = 0
        self.y_actual = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.x_actual < self.width and self.y_actual < self.height:
            x = self.x_actual
            y = self.y_actual
            self.incrementar_contadores()
            return Pixel(self, x, y)
        else:
            self.x_actual = 0
            self.y_actual = 0
            raise StopIteration()

    def incrementar_contadores(self):
        self.x_actual += 1
        if self.x_actual == self.width:
            self.x_actual = 0
            self.y_actual += 1


    @classmethod
    def file(cls, fichero):
        return Imagen(fichero)

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height


    def set_rgb(self, x, y, red, green, blue):
        self.px[x, y] = (red, green, blue)


    def mostrar(self):
        self.pil_image.show()

    def grabar(self,nombre_fichero):
        self.pil_image.save(nombre_fichero)

    def get_pixel(self, coordX, coordY):
        if (coordX < 0) or (coordX >= self._width) or (coordY < 0) or (coordY >= self.height):
            raise Exception('Coordenadas fuera de límites')
        return Pixel(self, coordX, coordY)



