"""
Crear una clase 'Persona' con atributos como nombre, edad y genero 
"""

class Persona:
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad= edad
        self.genero = genero
    
        
    def saludar(self):
        print("Hola, mi nombre es",self.nombre, "tengo ", self.edad, "años y soy ", self.genero )
#personal = Persona("Juan", 30, "Masculino")
personal=Persona(str(input("Escribe tu nombre: ")), input("Dime tu edad: ")  , input("Escribe tu Genero: "))
personal.saludar()