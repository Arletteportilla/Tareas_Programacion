import math


class Punto:
    def init(self, x=0, y=0):
        self.x = x
        self.y = y

    def __mod__(self):
        return "({},{})".format(self.x, self.y)


class Rectangulo:
    def __init__(self, plnicial=Punto(),pFinal =Punto()):
        self.pInicial=plnicial
        self.pFinal=pFinal
        self.vBase=abs(self.pFinal.x - self.pInicial.x)
        self.vAltura=abs(self.pFinal.y - self.pInicial.y)
        self.vArea=self.vBase * self.vAltura
def base(self):
    print("La base del rectángulo es {)".format(self.vBase))
def altura(self):
    print("La altura del rectángulo es {".format(self.vAltura))
def area(self):
    print("El área del rectángulo es ()". format(self.vArea))

a = Punto(2,3)
b = Punto(5,5)
c = Rectangulo(a,b)
c.vBase()
c.vAltura()
c.vArea()