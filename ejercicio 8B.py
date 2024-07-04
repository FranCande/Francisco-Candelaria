nombre_producto = input ("Ingrese el nombre del producto")
precio_producto = float(input ("Ingrese un numero"))
IVA = 0.21
valor_iva = precio_producto * IVA
valor_final_producto = (precio_producto * IVA) + precio_producto

print("El valor del IVA es de: $" + "{:.2f}".format(valor_iva) + "\nEl precio final del producto es de: $" + "{:.2f}".format(valor_final_producto))
