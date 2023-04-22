def sumar_5_enteros():
    # Definición de variables
    lista = []
    contadorWhile = 0
    tamano = 5
    suma = 0

    # Ingresamos los números
    while contadorWhile < tamano:
        lista.append(int(input(f"Ingrese número {str(contadorWhile+1)}: ")))
        contadorWhile += 1

    # Sumamos los números
    contadorWhile = 0
    while contadorWhile < tamano:
        suma += lista[contadorWhile]
        contadorWhile += 1

    print("Los números de la lista son: ")
    for i in lista:
        print(i,end=', ')

    print(f"La suma de todos lo elementos es:\n{suma}")
