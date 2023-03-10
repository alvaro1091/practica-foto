"""
Crear una clase RECTANGULO con atributo como ancho y altura.
"""

class Rectangulo: 
    def __init__(self, ancho, altura) -> None:
       self.ancho=ancho
       self.altura= altura

    def area(self):
        return self.ancho * self.altura
    
    def perimetro(self):
        return 2*(self.ancho + self.altura)
    
rectangulo1 = Rectangulo(10,7)
print("El area del rectangulo es :", rectangulo1.area())
print("El perimetro del rectangulo es :", rectangulo1.perimetro())
