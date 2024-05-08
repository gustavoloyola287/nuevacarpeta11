#conversor de moneda, de dolares eeuu a euros

#dolar u$s 1 = euro 0.93
euro = .93
dolar = int(input("Ingrese cantidad de dolares u$s "))

cantidad = float(dolar/euro)

print("Tengo en total:", cantidad)