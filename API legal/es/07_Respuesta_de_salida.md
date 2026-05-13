# API Legal - Respuesta de salida

Una vez lanzada una petición al API, éste devolverá una respuesta con dos tipos de datos diferenciados:

## Datos de noticia

| Campo           | descripción                                                                                            | Filtrable |  Tipo   |           Formato           |
| --------------- | ------------------------------------------------------------------------------------------------------ | :-------: | :-----: | :-------------------------: |
| id              | Código de indentificación asignado por Trawlingweb a cada publicación rastreada                        |    No     | Cadena  |                             |
| site_type       | Tipo de publicación                                                                                    |    No     | Cadena  |                             |
| profile         | Perfil de la publicación                                                                               |    No     | Cadena  |                             |
| edition_url     | Dirección web de la edición del boletín                                                                |    No     | Cadena  |                             |
| edition_url_pdf | Dirección el fichero pdf de la edición del boletín                                                     |    No     | Cadena  |                             |
| edition_id      | Identificador del boletín                                                                              |    Si     | Cadena  |                             |
| edition_name    | Siglas del boletín                                                                                     |    Si     | Cadena  |                             |
| edition_number  | Número de edición del boletín                                                                          |    Si     | Entero  |                             |
| published       | Fecha de publicación.                                                                                  |    Si     |  Fecha  |        ISO 8601-UTC         |
| crawled         | Fecha de procesamiento. La zona horaria es GMT +1                                                            |    Si     | Entero  | UNIX Timestamp milisegundos |
| language        | Idioma de la publicación                                                                               |    Si     | Cadena  |          ISO 639-1          |
| section         | Sección principal                                                                                      |    Si     | Cadena  |                             |
| subsection      | Subsección                                                                                             |    Si     | Cadena  |                             |
| department      | Departamento                                                                                           |    Si     | Cadena  |                             |
| topic           | Términos asociados                                                                                     |    No     | Cadena  |                             |
| Reference       | Identificador de la publicación                                                                        |    No     | Cadena  |                             |
| title           | Título de la publicación                                                                               |    Si     | Cadena  |                             |
| text            | Texto de la publicación                                                                                |    Si     | Cadena  |                             |
| text_raw        | Indica si el texto que se ha obtenido pertenece a la página completa (true) o a la publicación (false) |    No     | Boleano |                             |
| url_html        | Dirección web de la publicación                                                                        |    No     | Cadena  |                             |
| url_pdf         | Dirección del fichero pdf de la publicación                                                            |    No     | Cadena  |                             |
| url_epob        | Dirección del fichero epob de la publicación                                                           |    No     | Cadena  |                             |
| url_doc         | Dirección del fichero doc de la publicación                                                            |    No     | Cadena  |                             |
| url_xml         | Dirección del fichero xml de la publicación                                                            |    No     | Cadena  |                             |

## Datos de petición

| Datos        | Descripción                                                             |  Tipo  |
| :----------- | :---------------------------------------------------------------------- | :----: |
| requestLeft  | Total de consultas pendientes de la subscripción                        | Entero |
| totalResults | Total de resultados encontrados por la consulta                         | Entero |
| restResults  | Total de resultados encontrados pendientes de entrega                   | Entero |
| next         | URL para continuar con la paginación y así obtener todos los resultados | Cadena |

## Ejemplo de respuesta en formato json:

```
"json"
"response" : {
    "data" : [{
        "id" : "...",
        "site_type" : "...",
        "profile" : "...",
        "edition_url" : "...",
        "edition_url_pdf" : "...",
        "edition_id" : "...",
        "edition_name" : "...",
        "edition_number" : "...",
        "published" : "...",
        "crawled" : "...",
        "language" : "...",
        "section" : "...",
        "subsection" : "...",
        "department" : "...",
        "topic" : "...",
        "Reference" : "...",
        "title" : "...",
        "text" : "...",
        "text_raw" : "...",
        "url_pdf" : "...",
        "url_html" : "...",
        "url_epob" : "...",
        "url_doc" : "...",
        "url_xml" : "..."
    }],
    "requestLeft" : "...",
    "totalResults" : "...",
    "restResults" : "...",
    "next" : "..."
}
```
