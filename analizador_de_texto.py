texto = input("Ingrese un texto de su eleccion: ")
letras = []

texto = texto.lower()

letras.append(input("Ingrese la primera letra: ").lower())
letras.append(input("Ingrese la segunda letra: ").lower())
letras.append(input("Ingrese la tercera letra: ").lower())

print("\n")
print("Cantidad de letras")
canti_letras = texto.count(letras[0])
canti_letras1 = texto.count(letras[1])
canti_letras2 = texto.count(letras[2])

print(f"Hemos encontrado la letra '{letras[0]}' repetida {canti_letras} veces")
print(f"Hemos encontrado la letra '{letras[1]}' repetida {canti_letras1} veces")
print(f"Hemos encontrado la letra '{letras[2]}' repetida {canti_letras2} veces")

print("\n")
print("Cantidad de Palabras")
palabras = texto.split()
print(f"Hemos encontrado '{len(palabras)}' palabras dentro de tu texto")

print("\n")
print("Letra de Inicio y Final")
letra_inicio = texto[0]
letra_final = texto [-1]
print(f"La letra inicial es '{letra_final}' y  la final es  '{letra_final}'")

print("\n")
print("Texto invertido")
palabras.reverse()
texto_invertido = ' '.join(palabras)
print(f"Ordenando tu texto al reves seria asi '{texto_invertido}'")

print("\n")
print("Busdcando la palabra Python")
buscar_py = 'python' in texto
dic = {True:'si',False:'no'}
print(f"La palabra 'Python' {dic[buscar_py]} se encuentra en el texto")