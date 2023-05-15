from random import randint

intentos = 0 
numero_secreto = randint(1,100)
nombre = input("Escribe tu nombre gafo: ")

print(f"Vale {nombre}, he pensado un numero entre 1 y el 100\n Tienes 8 intentos para adivinar el numero")

while intentos < 8:
  estimado = int(input("Ingresa un numero: "))
  intentos += 1

  if estimado < numero_secreto:
    print("Esta por arriba")
    
  elif estimado > numero_secreto:
    print("Esta por abajo")

  else:
    print(f"Vale {nombre}, lo has adiviando en {intentos} intentos")
    break
    
if estimado != numero_secreto:
  print(f"lo siento {nombre}, se agotaron los intentos, el numero secreto era {numero_secreto}")
