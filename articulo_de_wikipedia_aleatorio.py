import wikipedia
import random

while True:
    # Obtener un artículo aleatorio
    article_title = wikipedia.random(1)

    # Obtener el resumen del artículo
    try:
        article_summary = wikipedia.summary(article_title, sentences=1)
    except wikipedia.exceptions.DisambiguationError as e:
        # Si el título del artículo es ambiguo, obtener uno nuevo
        continue

    # Preguntar si el usuario quiere leer el artículo
    print(f"¿Quieres leer sobre '{article_title}'?\nResumen: {article_summary}")
    user_input = input("Ingresa 's' para sí o 'n' para no: ")

    # Si la respuesta es "sí", mostrar el artículo completo
    if user_input.lower() == "s":
        article_content = wikipedia.page(article_title).content
        print(article_content)
        break  # Salir del bucle infinito

    # Si la respuesta es "no", obtener otro artículo aleatorio
    else:
        continue
