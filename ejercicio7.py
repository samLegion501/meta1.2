import random

num = random.randint(1, 10)
adivina = None

while adivina != num:
    adivina = input("Adivina un numero entre el 1 y 10: ")
    adivina = int(adivina)

    if adivina == num:
        print("¡Felicidades! ¡ganaste!")
        break
    else:
        print("no, lo siento. ¡intentar otra vez!")