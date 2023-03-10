"""
Crea una clase 'Perro' que herede de la clase 'Animal y agrege atributos y color, metos como 'ladrar'
"""
# name 'Animal' is not defined

class Perro(Animal):
    def __init__(self, especie, edad, raza, color):
        super().__init__(especie, edad)
        self.raza = raza
        self.color = color

    def ladrar(self):
        print("!Guau!, soy un", self.raza, "de color", self.color)

    def comer(self):
        print("!Guau!, soy un", self.raza, "de color", self.color)    

mi_perro=Animal("Perro", 5,"Labrador","negro")
mi_perro.comer()
mi_perro.ladrar()