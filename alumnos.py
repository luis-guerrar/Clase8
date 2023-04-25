def alumnos():
    alumnos = []
    respuesta = True

    while respuesta:
        alumno = []

        alumno.append(input("Ingrese el nombre del alumno: \n"))
        alumno.append(float(input("Ingrese la primera nota: \n")))
        alumno.append(float(input("Ingrese la segunda nota: \n")))
        alumno.append(float(input("Ingrese la tercera nota: \n")))

        alumnos.append(alumno)

        respuesta = input("¿Desea ingresar otro alumno?\nPresione 's' para sí"
                          " cualquier otra letra para no\n")
        if respuesta == "s":
            respuesta = True
        else:
            respuesta = False

    if len(alumnos) > 0:
        print("Listado de la notas de los alumnos: \nNombre\tNota1\tNota2\tNota3")

        for alumno in alumnos:
            print(f"{str(alumno[0])}\t{str(alumno[1])}\t\t{str(alumno[2])}\t\t{str(alumno[3])}")

    if len(alumnos) > 0:
        print("\nListado de los promedios de los alumnos:\nNombre\tPromedio")
        for alumno in alumnos:
            promedio = (alumno[1]+alumno[2]+alumno[3])/3
            print(f"{alumno[0]}\t{str(round(promedio, 1))}")

    if len(alumnos) > 0:
        print(f"\nListado de los alumnos que perdieron la materia\n"
              f"Nombre\tPromedio")
        for alumno in alumnos:
            promedio = (alumno[1]+alumno[2]+alumno[3])/3
            if promedio < 3:
                print(f"{alumno[0]}\t{str(round(promedio, 1))}")