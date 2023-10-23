import wikipedia
import random
import requests
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, Spacer
import textwrap

def guardar_articulo_pdf(article_title, article_content):
    # Solicitar al usuario el nombre del archivo
    file_name = input(f"Ingresa el nombre del archivo PDF para guardar el artículo '{article_title}': ") + ".pdf"

    try:
        # Crear un archivo PDF
        c = canvas.Canvas(file_name, pagesize=letter)
        width, height = letter
        margin = 50  # Margen izquierdo
        line_height = 14  # Altura de línea

        c.setFont("Helvetica", 12)

        # Título del artículo
        title_style = getSampleStyleSheet()['Title']
        elements = []
        elements.append(Paragraph(f"<u>{article_title}</u>", title_style))
        elements.append(Spacer(1, 0.2 * inch))  # Espacio entre el título y el contenido

        # Contenido del artículo
        y = height - 70
        lines = article_content.split('\n')
        for line in lines:
            wrapped_lines = textwrap.wrap(line, width=70)  # Ajusta el texto a un ancho específico
            for wrapped_line in wrapped_lines:
                if y <= margin + line_height:
                    c.showPage()  # Cambiar de página si el espacio se agota
                    c.setFont("Helvetica", 12)
                    y = height - 50
                c.drawString(margin, y, wrapped_line)
                y -= line_height

        for element in elements:
            element.wrapOn(c, width, height)
            element.drawOn(c, margin, height - 50)

        c.showPage()  # Terminar la página
        c.save()  # Guardar el archivo PDF

        print(f"El artículo '{article_title}' ha sido guardado en '{file_name}'.")
    except Exception as e:
        print(f"No se pudo guardar el artículo en PDF: {e}")

while True:
    # Solicitar al usuario que ingrese una categoría
    category = input("Ingresa una categoría para buscar un artículo aleatorio (o escribe 'salir' para salir): ")

    if category.lower() == "salir":
        print("Saliendo del programa...")
        break

    # Utiliza la API de MediaWiki para obtener categorías asociadas a la página
    S = requests.Session()
    URL = "https://en.wikipedia.org/w/api.php"
    PARAMS = {
        "action": "query",
        "format": "json",
        "prop": "categories",
        "titles": category
    }

    R = S.get(url=URL, params=PARAMS)
    DATA = R.json()

    PAGES = DATA["query"]["pages"]

    for k, v in PAGES.items():
        if "categories" in v:
            for cat in v['categories']:
                print(cat["title"])
        else:
            print("No se encontraron categorías para la página proporcionada.")

    try:
        # Obtener una lista de artículos en la categoría
        articles = wikipedia.page(category).links

        if articles:
            # Elegir un artículo aleatorio de la lista
            article_title = random.choice(articles)

            try:
                # Obtener el resumen del artículo
                article_summary = wikipedia.summary(article_title, sentences=1)
            except wikipedia.exceptions.DisambiguationError:
                print("La categoría es ambigua. Intenta nuevamente con una categoría más específica.")
                continue

            # Preguntar al usuario qué acción desea realizar
            print(f"¿Qué deseas hacer con '{article_title}'?\nResumen: {article_summary}")
            print("1. Leer el artículo")
            print("2. Guardar el artículo en un archivo PDF")
            print("3. Buscar otro artículo")
            user_input = input("Ingresa el número de la opción (o escribe 'salir' para salir): ")

            if user_input.lower() == "salir":
                print("Saliendo del programa...")
                break

            if user_input == "1":
                try:
                    article_content = wikipedia.page(article_title).content
                    print(article_content)
                except Exception as e:
                    print(f"No se pudo obtener el contenido del artículo: {e}")
            elif user_input == "2":
                try:
                    article_content = wikipedia.page(article_title).content
                    guardar_articulo_pdf(article_title, article_content)
                except Exception as e:
                    print(f"No se pudo obtener el contenido del artículo: {e}")
            elif user_input == "3":
                continue
            else:
                print("Opción no válida. Volviendo al menú principal.")
        else:
            print(f"No se encontraron artículos en la categoría '{category}'. Intenta nuevamente con otra categoría.")
            continue
    except wikipedia.exceptions.DisambiguationError:
        print("La categoría es ambigua. Intenta nuevamente con una categoría más específica.")
        continue
    except wikipedia.exceptions.HTTPTimeoutError:
        print("Se produjo un error de tiempo de espera al conectarse a Wikipedia. Inténtalo de nuevo más tarde.")
        break
    except wikipedia.exceptions.PageError:
        print("No se pudo encontrar la página solicitada en Wikipedia. Intenta nuevamente con otra categoría.")
        break
    except Exception as e:
        print(f"Se ha producido un error inesperado: {e}")
        break

