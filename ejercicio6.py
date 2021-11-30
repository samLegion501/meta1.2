from random import randint

opciones = ("piedra","papel","tijera")
def main():
    computer = opciones[randint(0,2)]

    print("\nBienvenido al Piedra, Papel o Tijera\n")
    player = input("Opcion del usuario: ").lower()
    print("Opcion de la computadora: " + computer)

    if player == computer:
        print("Empate")
    elif player == "piedra" and computer == "papel":
        print("Computadora gana")
    elif player == "roca" and computer == "tijera":
        print("Usuario gana")
    elif player == "papel" and computer == "roca":
        print("Usuario gana")
    elif player == "papel" and computer == "tijera":
        print("Computadora gana")
    elif player == "tijera" and computer == "roca":
        print("Computadora gana")
    elif player == "tijera" and computer == "papel":
        print("Usuario gana")
    elif player == "fin":
        exit("Nos vemos pronto") 
        StopIteration

    main()

main()        

