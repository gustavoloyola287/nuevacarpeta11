#conversor de temperatura
print("""Presione "1" y enter para pasar de Fahrenheit a Celsius o 
Presione "2" y enter para pasar de Celsius a Fahrenheit""")
opcion = int(input("Elija su opción: "))
if opcion == 1: 

#convertir celsius a fahrenheit
    celsius = float(input("""Hola usuario ingrese los grados Celsius 
    que desea convertir a Fahrenheit: """))
    F = ((celsius * (9/5))) + 32
    print("La temperatura equivalente en Fahrenheit es ",F, "grados")
elif opcion == 2:
#convertir de fahrenheit a celsius
    F = float(input("""Ingrese la cantidad de grados Fahrenheit 
    que quiere convertir a Celsius: """))
    celsius = ((F - 32) * (5/9))
    print("La temperatura equivalente en Celsius es  ",celsius, "grados")