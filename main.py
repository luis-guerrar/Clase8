import problema1
from alumnos import alumnos
# Desde este momento iniciaremos el manejo de listas

edad = 12
altura = 1.79
nombre = "Juan"
estado = True
# Las listas pueden almacenar varios tipos de datos dentro de ella
lista1 = [10, 5, 3, 9]
lista2 = [1.78, 2.66, 1.55, 89.4, 6.9]
lista3 = ["Lunes", "Martes", "Miércoles"]
lista4 = ["Juan", 45, 1.92, False]


if __name__ == '__main__':
    # Len hace referencia a la cantidad de elementos de la lista, es muy útil para recorrerla
    print(len(lista1))
    print(len(lista2))
    print(len(lista3))
    print(len(lista4))
    print()
    print(lista1)
    lista1[0] = 1
    print()
    print(lista1)
    print(lista1[3])
    print()
    problema1.sumar_5_enteros()
    print()
    alumnos()

