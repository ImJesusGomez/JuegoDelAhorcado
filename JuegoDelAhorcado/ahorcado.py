import random


def generar_palabras():
  """
  Esta función elige aleatoriamente una palabra de la lista de palabras disponibles, la convierte en una lista de caracteres y crea otra lista de guiones bajos (_) para representar las letras ocultas que el jugador debe adivinar.
  """

  lista_palabras = ["informatica", "software", "hardware", "python", "java", "javascript", "programacion", "variable", "constante"]
  palabra_original = random.choice(lista_palabras)

  palabra_original = list(palabra_original)
  palabra_adivinar = list(palabra_original)

  contador = 0
  for letra in palabra_adivinar:
    palabra_adivinar[contador] = "_"
    contador += 1
  return palabra_original, palabra_adivinar

def impresion_ahorcado(fallos):
  """
  Esta función toma un argumento fallos que indica cuántos intentos fallidos ha tenido el jugador. Dependiendo del número de fallos, se imprime una representación gráfica del ahorcado.
  """
  ahorcado = """
+---+
|   
|   
|   
|   
|
========
"""
  if fallos == 1:
    ahorcado = """
+---+
|   |
|   
|   
|   
|   
|
========"""
  elif fallos == 2:
    ahorcado = """
+---+
|   |
|   O
|  
|   
|  
|
========"""
  elif fallos == 3:
    ahorcado = """
+---+
|   |
|   O
|   |
|   |
|  
|
========"""
  elif fallos == 4:
    ahorcado = """
+---+
|   |
|   O
|  |||
|   |
|  
|
========"""
  elif fallos == 5:
    ahorcado = """
+---+
|   |
|   O
|  ||| 
|   |
|  | |
|
========"""
  else:
    ahorcado
  return ahorcado


def main():
  """
  Es la función principal del juego. Se encarga de llamar a las otras funciones y ejecutar el bucle principal del juego. Muestra el mensaje de bienvenida y maneja la lógica del juego.
  """
  palabra_original, palabra_adivinar = generar_palabras()
  fallos = 0
  adivinar = True

  print("Bienvenido al juego del ahorcado".center(60, "-"))
  while adivinar:
    if fallos == 5:
      print(impresion_ahorcado(fallos))
      print(" ".join(palabra_adivinar))
      print(f"Oh no! Haz perdido\nLa palabra era {"".join(palabra_original)}")
      adivinar = False
    else:
      if palabra_adivinar == palabra_original:
        print("Felicidades, haz adivinado la palabra!!")
        print("".join(palabra_original))
        adivinar = False
      else:
        print(impresion_ahorcado(fallos))
        print(" ".join(palabra_adivinar))
        letra = input("\nIngresa una letra: ")
        
        contador = 0
        if letra in palabra_original:
          for caracter in palabra_original:
            if letra == palabra_original[contador]:
              palabra_adivinar[contador] = letra
            else: 
              pass
            contador += 1
        else:
          print(f"Oh no, {letra} no está en la palabra")
          fallos += 1

main()