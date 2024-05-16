# Pedimos al usuario que ingrese una frase
frase = input("Ingresa una frase: ")

# Creamos una lista vacía para almacenar las letras separadas
letras_separadas = []

# Iteramos sobre cada carácter en la frase
for letra in frase:
    # Agregamos cada letra a la lista de letras separadas
    letras_separadas.append(letra)

# Imprimimos la lista de letras separadas
print("La frase separada en letras es:", letras_separadas)