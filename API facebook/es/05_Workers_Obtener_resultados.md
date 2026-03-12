# API Facebook - Método GET /posts

Permite obtener resultado capturados de cada Worker configurado de Facebook.
Se pueden usar delimitadores temporales para acotar el contenido devuelto.

# Parámetros GET

La llamada a la API se construye a partir de la estructura básica:

```
https://facebook.trawlingweb.com/posts/{WORKERID}?token={APIKEY}
```

## Parámetros PATH

| Elemento  | Descripción                                   |
| :-------- | :-------------------------------------------- |
| protocolo | Puede ser tanto **http** como **https**       |
| dominio   | Dirección de la API Facebook.trawlingweb.com   |
| método    | posts                                         |
| workerid  | Identificador que permite acceder a un worker específico y recuperar los resultados generados por las palabras clave configuradas en él. Funciona como una biblioteca o lista de palabras clave, permitiendo obtener resultados relevantes basados en dichas palabras clave. |


## Parámetros QUERY

| Parámetro | Descripción                                                                  | Default                                                 | Ejemplo            |
| :-------- | :--------------------------------------------------------------------------- | :------------------------------------------------------ | :----------------- |
| token     | APIKEY para validar y acceder al sistema de TrawlingWeb. Cada usuario tiene su propia APIKEY individual e intransferible, vinculada a sus servicios y características.           | Valor obligatorio                                       | ?token={APIKEY}    |
| country_pref| Preferencia de país del cliente (ISO 3166-1 alpha-2, ej: `es`). **Obligatorio para contratos FeedScale Pay-per-Use**. Su omisión penaliza multiplicando x2.5 el coste de la request y conlleva riesgo de bloqueo de acceso. | Obligatorio (Pay-per-Use)                               | &country_pref=es              |
| ts        | Se trata del delimitador temporal inicial. Formato Unix Time en milisegundos | Delimita a 1 meses en el pasado a partir de la petición | &ts=1518472804000  |
| tsi       | Se trata del delimitador temporal final. Formato Unix Time en milisegundos   | Delimita con la fecha de petición                       | &tsi=1524818189854 |


# Respuesta de Salida - RESPONSE

Al realizar una solicitud a la API de Facebook, se devolverá una respuesta estructurada de la siguiente manera:

## Datos del Post

| Campo                      | Descripción                                                                                                           | Buscable | Ordenable |  Tipo   |           Formato           |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------- | :------: | :-------: | :-----: | :-------------------------: |
| id                         | Código de identificación asignado por Trawlingweb a cada post rastreado                                                |    No    |    No     | Cadena  |                             |
| post_id                    | ID original del post                                                                                                   |    No    |    No     | Cadena  |                             |
| hash_text                  | Hash generado a partir del texto del post                                                                              |    No    |    No     | Cadena  |                             |
| user_name                  | Nombre del usuario que hizo el post                                                                                    |    No    |    No     | Cadena  |                             |
| user_screen_name           | Nombre de usuario mostrado                                                                                             |    No    |    No     | Cadena  |                             |
| user_url                   | URL del perfil del usuario                                                                                             |    No    |    No     | Cadena  |                             |
| user_icon                  | URL que apunta a la imagen de perfil del usuario                                                                       |    No    |    No     | Cadena  |                             |
| published                  | Fecha y hora en que se publicó el post                                                                                 |    No    |    No     |  Fecha  |        ISO 8601-UTC         |
| url                        | URL del post en Facebook                                                                                               |    No    |    No     | Cadena  |                             |
| text                       | Contenido de texto del post                                                                                            |    No    |    No     | Cadena  |                             |
| likes_num                  | Número de "me gusta" que recibió el post                                                                               |    No    |    No     | Entero  |                             |
| comments_num               | Número de comentarios en el post                                                                                       |    No    |    No     | Entero  |                             |
| type                       | Tipo de post (por ejemplo, historia, foto)                                                                             |    No    |    No     | Cadena  |                             |
| language                   | Idioma detectado del post, identificado por una etiqueta de idioma BCP 47                                              |    No    |    No     | Cadena  |                             |
| language_detection_precision | Precisión de la detección del idioma como un porcentaje                                                              |    No    |    No     | Entero  |                             |
| screen                     | ID de pantalla, relacionado con el proceso de captura de la API                                                        |    No    |    No     | Entero  |                             |
| last_article               | Fecha del último artículo procesado                                                                                    |    No    |    No     |  Fecha  |        ISO 8601-UTC         |
| oldest_article             | Fecha del artículo más antiguo procesado                                                                               |    No    |    No     |  Fecha  |        ISO 8601-UTC         |
| hash                       | Hash generado basado en los metadatos del post                                                                         |    No    |    No     | Cadena  |                             |
| crawled                    | Fecha y hora en que se capturó el post                                                                                 |    No    |    Sí     | Entero  | Timestamp UNIX en milisegundos |
| updated                    | Fecha y hora en que se actualizó por última vez el post                                                                |    No    |    Sí     | Entero  | Timestamp UNIX en milisegundos |
| time_distance              | Tiempo transcurrido entre la fecha de publicación y la fecha de captura, medido en horas                               |    No    |    No     | Decimal |                             |

## Ejemplo de respuesta en formato JSON:

```json
{
  "data": [
    {
      "id": "...",
      "post_id": "...",
      "hash_text": "...",
      "user_name": "...",
      "user_screen_name": "...",
      "user_url": "...",
      "user_icon": "...",
      "published": "2024-08-03T23:01:25.601Z",
      "url": "...",
      "text": "...",
      "likes_num": 35,
      "comments_num": 12,
      "type": "...",
      "language": "...",
      "language_detection_precision": 99,
      "screen": 0,
      "last_article": "2024-08-03T23:01:25.601Z",
      "oldest_article": "2024-08-03T23:01:25.601Z",
      "hash": "...",
      "crawled": 1722726103860,
      "updated": 1722726103860,
      "time_distance": 0.01
    }
  ],
  "totalResults": "...",
  "restResults": "...",
  "next": "..."
}
```

## Ejemplo de salida

```
requestLeft	9999999
totalResults	295404987
next	"http://facebook.trawlingweb.com/posts/1234567891234567891234567891234567.123456789?token=1234567891234567891234567891234567891234&ts=1555327617000&tsi=1554076800000"
```

# Contacto
Si tienes alguna pregunta, necesitas asistencia, contratar o ampliar tus servicios por favor contacta con nosotros.

**SAT (Soporte Técnico):**
* [Correo SAT](mailto:support@trawlingweb.com)
* [Documentación Oficial](https://docs.trawlingweb.com)

**SAC (Soporte administrativo):**
* [Correo SAC](mailto:gestion@trawlingweb.com)

**Sales (Soporte ventas):**
* [Correo Ventas](mailto:sales@trawlingweb.com)

