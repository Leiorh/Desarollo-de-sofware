import random

# Lista de palabras para el juego
palabras = ["ecuador", "navidad", "programacion", "encebollado", "fanesca"]

def iniciar_juego():
    palabra = random.choice(palabras).lower()
    letras_adivinadas = ["_"] * len(palabra)
    intentos = 5
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
        
        if letra in palabra:
            for i in range(len(palabra)):
                if palabra[i] == letra:
                    letras_adivinadas[i] = letra
            print("¡Correcto!")
        else:
            intentos -= 1
            print("Incorrecto. Pierdes un intento.")
        
        # Verificar victoria
        if "_" not in letras_adivinadas:
            print("\n¡Felicitaciones! ¡Ganaste!")
            print("La palabra era:", palabra)
            return
    
    print("\n¡Game Over! La palabra era:", palabra)

# Iniciar el juego
iniciar_juego()
