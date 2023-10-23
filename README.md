# Programa para Descargar Artículos de Wikipedia en PDF

Este programa en Python utiliza la biblioteca de Wikipedia y ReportLab para buscar artículos en Wikipedia, mostrar su contenido y guardarlos en archivos PDF. Además, permite al usuario salir del programa en cualquier momento.

## Requisitos

Asegúrate de tener instaladas las siguientes bibliotecas de Python:

- wikipedia
- requests
- reportlab

Puedes instalar estas bibliotecas utilizando pip:

```
pip install wikipedia-api
pip install requests
pip install reportlab
```

## Uso

1. Ejecuta el programa en tu entorno de Python.
2. El programa te pedirá que ingreses una categoría para buscar un artículo aleatorio en Wikipedia. Si deseas salir en cualquier momento, simplemente escribe "salir".
3. El programa recuperará una lista de categorías asociadas a la página ingresada y te permitirá seleccionar un artículo aleatorio.
4. Luego, te mostrará un resumen del artículo y te dará las siguientes opciones:
   - Leer el artículo (ingresa "1").
   - Guardar el artículo en un archivo PDF (ingresa "2").
   - Buscar otro artículo (ingresa "3").
   - Salir del programa (ingresa "salir").

## Guardar un Artículo en PDF

Si eliges la opción "2" para guardar un artículo en un archivo PDF, el programa te solicitará un nombre para el archivo. El artículo se guardará en un archivo PDF con el nombre que elijas en el directorio de trabajo actual.

## Salir del Programa

Puedes salir del programa en cualquier momento escribiendo "salir" como la categoría de búsqueda o como la respuesta a las opciones. El programa se cerrará sin procesar más acciones.

## Notas

- Si el programa no puede encontrar la página solicitada en Wikipedia, te lo informará y te dará la opción de buscar otro artículo.
- Si se produce un error inesperado, el programa mostrará un mensaje de error y se cerrará.
- El programa utiliza la biblioteca ReportLab para generar archivos PDF. Asegúrate de que los archivos PDF se generen correctamente y estén formateados de acuerdo a tus necesidades.

¡Disfruta explorando y guardando artículos de Wikipedia en PDF con este programa!
