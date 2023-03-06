# Actividades de la seecion Basica para Python
#Crear una funcion que acepte una lista como parametro y devuelva la
# suma de los elementos de la lista.

def suma_lista(lista):
    suma = 0
    for elemento in lista:
        suma += elemento
    return suma
lista_numero = [1, 2, 3, 4, 5]
print("La suma de los elementos de la lista: ", suma_lista(lista_numero))
