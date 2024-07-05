producto1=float(input("Ingrese el primer precio del producto: "))
producto2=float(input("Ingrese el segundo precio del producto: "))
producto3=float(input("Ingrese el tercer precio del producto: "))
suma=producto1+producto2+producto3
print("La suma de los 3 precios: ", suma)
promedio=suma/3
print("El promedio es: ", promedio)
iva=suma*21/100
facturaciones_iva = suma + iva
print ("El precio total con iva es ",facturaciones_iva)
