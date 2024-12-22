-	Importación del módulo random
import random: Este módulo se utiliza para realizar operaciones relacionadas con la aleatoriedad. En este caso, sirve para seleccionar una palabra aleatoria de la lista palabras.
-	Lista de palabras
palabras = ["Ecuador", "Navidad", "Encebollado", "programación", "Fanesca"]: Es una lista que contiene las palabras posibles para el juego. Cada vez que se inicie el juego, se seleccionará una de estas palabras al azar.
-	Función iniciar juego
La función principal del juego del ahorcado. Se encarga de manejar la lógica completa del juego. Detalle por pasos:
-	Selección de palabra y configuración inicial:
palabra = random.choice(palabras).lower(): Selecciona aleatoriamente una palabra de la lista palabras y la convierte a minúsculas para simplificar la comparación de letras.
letras_adivinadas = ["_"] * len(palabra): Crea una lista que representa el estado actual de las letras adivinadas, inicialmente vacías (_) tantas como la longitud de la palabra.
intentos = 6: Define el número máximo de intentos permitidos para adivinar la palabra.
letras_usadas = []: Inicializa una lista vacía para registrar las letras que el jugador ya intentó.
Bucle principal del juego:
while intentos > 0: Se repite mientras el jugador tenga intentos restantes.
Mostrar estado actual:
print("\nPalabra:", " ".join(letras_adivinadas)): Muestra el estado actual de la palabra adivinada con los espacios y letras descubiertas.
print("Intentos restantes:", intentos): Indica cuántos intentos le quedan al jugador.
print("Letras usadas:", ", ".join(letras_usadas)): Lista las letras que el jugador ha intentado hasta el momento.
Entrada del jugador:
letra = input ("Ingresa una letra: ").lower(): Solicita al jugador ingresar una letra y la convierte a minúsculas para comparación.
Validación de la entrada:
Verificar si la letra ya se usó:
if letra in letras usadas: Si la letra ya está en la lista letras_usadas, se informa al jugador y se salta al siguiente ciclo del bucle.
Registrar la letra:
letras_usadas.append(letra): Agrega la letra ingresada a la lista de letras usadas.
-	Verificar si la letra está en la palabra:
if letra in palabra: Si la letra ingresada está en la palabra:
Se recorre cada carácter de la palabra: for i in range(len(palabra)):
Si coincide con la letra ingresada: if palabra[i] == letra:
Actualiza el estado de las letras adivinadas: letras_adivinadas[i] = letra
Imprime un mensaje indicando que fue correcto.
-	Si no está en la palabra:
intentos -= 1: Resta un intento al contador.
Informa al jugador que falló.
Verificar victoria:
if "_" not in letras adivinadas: Si no quedan guiones bajos (_) en letras_adivinadas, significa que el jugador adivinó todas las letras de la palabra.
Imprime un mensaje de victoria con la palabra correcta.
Termina el juego con return.
-	Finalizar el juego al perder:
Si el jugador agota los intentos, se imprime un mensaje con la palabra correcta: print("\n¡Game Over! La palabra era:", palabra)
