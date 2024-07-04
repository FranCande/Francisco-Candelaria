nombre_alumno = input("Ingrese el nombre del alumno: ")
apellido_alumno = input("Ingrese el apellido del alumno: ")
nota_1 = float(input("Ingrese su primera nota: "))
nota_2 = float(input("Ingrese su segunda nota: "))
nota_3 = float(input("Ingrese su tercera nota: "))
promedio_notas = "{:.2f}".format((nota_1 + nota_2 + nota_3) / 3)

print("Las notas del alumno " + nombre_alumno , apellido_alumno + " son las siguientes: " + "\nNota 1: " + str(nota_1) + "\nNota 2: " + str(nota_2) + "\nNota 3: " + str(nota_3) + "\nPromedio: " + str(promedio_notas) + ".")
