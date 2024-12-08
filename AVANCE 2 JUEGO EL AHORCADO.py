# AVANCE 2 JUEGO EL AHORCADO
import random

palabras = ["Ecuador", "Navidad", "Encebollado", "Programacion", "Fanesca"]

def iniciar_juego():
    palabra = random.choice(palabras).lower()
    letras_adivinadas = ["_"] * len(palabra)
    intentos = 6
    letras_usadas = []
    
    while intentos > 0:
        print("\nPalabra:", " ".join(letras_adivinadas))
        print("Intentos restantes:", intentos)
        print("Letras usadas:", ", ".join(letras_usadas))
        
        letra = input("Ingresa una letra: ").lower()
        
# Validaciones
        if letra in letras_usadas:
            print("Ya usaste esa letra. Intenta con otra.")
            continue
            
        letras_usadas.append(letra)