"""
Crear una case ANIMAL con atributos especie y edad.
Metodos como COMER Y DORMIR
"""
class Animal:
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad=edad

    def comer(self):
        print("El", self.especie, "esta comiendo")

    def dormir(self):
        print("El", self.especie, "esta durmiendo")
perro =Animal("Perro",3)
perro.comer()
perro.dormir()
