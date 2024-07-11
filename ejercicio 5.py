cantidad_numeros = 0
suma = 0

while cantidad_numeros <5:
    if cantidad_numeros <5:
        numero = float(input("Ingrese un numero: "))
        cantidad_numeros = cantidad_numeros + 1
        suma = suma + numero

print("La suma de estos numeros es ", suma)
print("El promedio de la suma es ", suma / 5)

