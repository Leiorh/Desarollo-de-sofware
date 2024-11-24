import random

# Lista de palabras para el juego
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
        