# Lector Aleatorio de Artículos de Wikipedia

Este programa te permite explorar aleatoriamente artículos de Wikipedia. Obtiene un título de artículo al azar, muestra un resumen y te da la opción de leer el artículo completo.

## Descripción

El programa utiliza la biblioteca `wikipedia` para acceder a la API de Wikipedia y obtener información sobre los artículos. Sigue los siguientes pasos:

1. Genera un título de artículo aleatorio usando `wikipedia.random(1)`.
2. Obtiene el resumen del artículo utilizando `wikipedia.summary(article_title, sentences=1)`.
3. Si el título del artículo es ambiguo y genera un `DisambiguationError`, el programa generará un nuevo artículo aleatorio y repetirá el proceso.
4. Muestra el título del artículo y el resumen al usuario, preguntando si desea leer el artículo completo.
5. Si el usuario ingresa 's' (para 'sí'), el programa obtiene el contenido completo del artículo utilizando `wikipedia.page(article_title).content` y lo muestra.
6. Si el usuario ingresa 'n' (para 'no'), el programa genera otro artículo aleatorio y repite el proceso.

El programa se ejecuta en un bucle infinito hasta que el usuario elija leer un artículo completo, momento en el cual el bucle se interrumpe.

## Uso

1. Asegúrate de tener instalada la biblioteca `wikipedia`. Puedes instalarla utilizando pip: `pip install wikipedia`.
2. Ejecuta el programa.
3. El programa mostrará un título de artículo aleatorio y su resumen.
4. Responde a la indicación ingresando 's' para leer el artículo completo o 'n' para generar otro artículo aleatorio.
5. Si eliges leer el artículo completo, el programa obtendrá y mostrará su contenido.
6. Si eliges no leer el artículo completo, el programa generará otro artículo aleatorio y repetirá el proceso.

**Nota:** Este programa se basa en la API de Wikipedia, por lo tanto, se requiere una conexión a Internet estable para que funcione correctamente.

## Ejemplo

```
¿Quieres leer sobre 'Título del Artículo'?
Resumen: Resumen del artículo.

Ingresa 's' para sí o 'n' para no: n

¿Quieres leer sobre 'Otro Artículo'?
Resumen: Resumen de otro artículo.

Ingresa 's' para sí o 'n' para no: s

El contenido completo del artículo 'Otro Artículo' se muestra aquí...
```

En este ejemplo, el programa presenta dos artículos aleatorios y pregunta al usuario si desea leer cada uno. El usuario elige no leer el primer artículo y opta por leer el contenido completo del segundo artículo.

¡Disfruta explorando Wikipedia de forma aleatoria!
