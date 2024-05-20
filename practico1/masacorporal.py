#calcular indice de masa corporal

#preguntamos el nombre de la persona
nombre = input("Ingrese su nombre: ")

#preguntamos su peso
peso = float(input("Ingrese su peso en kilogramos: "))

#preguntamos su altura
altura = float(input("Ingrese su altura en metros: "))

#definimos el calculo de la funcion
IMC = peso/(altura * altura)

#imprimimos los datos
print("Hola " + nombre , "tu indice de masa muscular es" ,IMC)