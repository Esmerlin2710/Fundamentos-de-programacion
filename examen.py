"""
Crea un programa donde:

Definas una variable numero_secreto con un valor entre 1 y 10
Pidas al usuario que adivine el número (máximo 3 intentos)
Usa un ciclo while para los intentos
Indica si el número es mayor o menor que el intento
Muestra si ganó o perdió al final

Si el usuario agota los intentos sal del programa
"""

numero_secreto = 4
def random():
    
    intentos = 1
    ganador = False
    print("-" * 50)
    print("!!Bienvenidos a: adivina el numero!!!")
    print("-" * 50)


    while intentos <= 3:
        print(f"Intento #{intentos}")
        eleccion = input(("Intenta adivinar el numero del 1 al 10: "))
        
        
        if eleccion.isdigit():
            eleccion = int(eleccion)
            if eleccion == numero_secreto:
                print("Felicidades, haz adivinado el numero.")
                ganador = True
                break
            elif eleccion < numero_secreto:
                print("El número secreto es MAYOR.")
                intentos += 1
            else:
                print("El número secreto es MENOR.")
                intentos += 1
                
        else:
            print("Ingrese un numero.")

    if ganador:
        print("Has ganado.")
    else:
        print("Has perdido.")

random()