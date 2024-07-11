resultado = 0
contador = 1

while contador <= 10:
    if contador % 2 == 0:
        resultado = contador + resultado
    contador = contador + 1
print("La suma de los numeros pares entre 1 y 10 da:", resultado)
