edad = int(input("¿Cual es su edad?"))
if(edad < 10):
    print("Eres niño/niña")
elif(edad > 10 and edad < 13):
    print("Eres pre-adolescente")
elif(edad > 13 and edad < 17):
    print("Eres adolescente")
else:
    print("Eres mayor")