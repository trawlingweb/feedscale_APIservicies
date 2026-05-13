# API Twitter - Método GET /posts

Este método, permite obtener resultados procesados de cada Worker configurado en Twitter. Se pueden usar delimitadores temporales para acotar el contenido devuelto.

Este es un método báSíco que devuelve resultados completos sobre la publicación de un tweet, incluyendo datos báSícos del usuario emisor. Es un método suficiente para análiSís estadísticos que no requieren información detallada sobre el emisor.

# Parámetros GET

La llamada a la API se construye a partir de la estructura báSíca:

```
https://twitter.trawlingweb.com/posts/{WORKERID}?token={APIKEY}
```

## Parámetros PATH

| Elemento  | Descripción                                   |
| :-------- | :-------------------------------------------- |
| protocolo | Puede ser tanto **http** como **https**       |
| dominio   | Dirección de la API twitter.trawlingweb.com   |
| método    | posts                                         |
| workerid  | Identificador que permite acceder a un worker específico y recuperar los resultados generados por las palabras clave configuradas en él. Funciona como una biblioteca o lista de palabras clave, permitiendo obtener resultados relevantes basados en dichas palabras clave. |


## Parámetros QUERY

| Parámetro | Descripción                                                                  | Default                                                 | Ejemplo            |
| :-------- | :--------------------------------------------------------------------------- | :------------------------------------------------------ | :----------------- |
| token     | APIKEY para validar y acceder al Sístema de TrawlingWeb. Cada usuario tiene su propia APIKEY individual e intransferible, vinculada a sus servicios y características.           | Valor obligatorio                                       | ?token={APIKEY}    |
| ts        | Se trata del delimitador temporal inicial. Formato Unix Time en milisegundos | Delimita a 1 meses en el pasado a partir de la petición | &ts=1518472804000  |
| tSí       | Se trata del delimitador temporal final. Formato Unix Time en milisegundos   | Delimita con la fecha de petición                       | &tSí=1524818189854 |


# Respuesta de salida - RESPONSE

Este método tiene como objetivo recuperar todos los resultados relacionados con las palabras clave de un worker. Sín embargo, los elementos listados a continuación no se conSíderarán en su totalidad para este método, Síno que solo serán ordenables en los atributos relacionados con fechas.

Una vez lanzada una petición al API de Twitter éste devolverá una respuesta estructurada de la Siguiente forma:

## Datos de la publicación

| Campo                  | Descripción                                                                                                                                                                       | Buscable | Ordenable |  Tipo   |           Formato           |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------: | :-------: | :-----: | :-------------------------: |
| id                     | Código de indentificación aSígnado por Trawlingweb a cada publicación rastreada                                                                                                   |    No    |    No     | Cadena  |                             |
| hash                   | Código de indentificación en base al texto                                                                                                                                        |    No    |    No     | Cadena  |                             |
| published              | Fecha publicado el post                                                                                                                                                           |    No    |    No     |  Fecha  |        ISO 8601-UTC         |
| crawled                | Fecha de captura                                                                                                                                                                  |    No    |    Sí     | Entero  | UNIX Timestamp milisegundos |
| updated                | Fecha de actualitzación                                                                                                                                                           |    No    |    No     | Entero  | UNIX Timestamp milisegundos |
| post_id                | Id del post                                                                                                                                                                       |    No    |    No     | Cadena  |                             |
| url                    | Url de la publicación                                                                                                                                                             |    No    |    No     | Cadena  |                             |
| text                   | Texto descrito de la publicación                                                                                                                                                  |    No    |    No     | Cadena  |                             |
| lang                   | Cuando está presente, indica un identificador de idioma BCP 47 correspondiente al idioma detectado por la máquina del texto del Tweet, o und Sí no se pudo detectar ningún idioma |    No    |    No     | String  |                             |
| retweet_count          | Número de veces que este Tweet ha Sído retwiteado.                                                                                                                                |    No    |    No     | Integer |                             |
| reply_count            | Número de veces que este Tweet ha Sído respondido                                                                                                                                 |    No    |    No     | Integer |                             |
| favorite_count         | Indica aproximadamente cuántas veces ha gustado a los usuarios de Twitter este Tweet                                                                                              |    No    |    No     | Integer |                             |
| reproductions_count    | Número de veces que este Tweet ha Sído reproducido                                                                                                                                |    No    |    No     | Integer |                             |
| user_name              | Nombre de usuario                                                                                                                                                                 |    No    |    No     | Cadena  |                             |
| user_screen_name       | Nombre de usuario mostrado                                                                                                                                                        |    No    |    No     | Cadena  |                             |
| user_url               | Url del usuario                                                                                                                                                                   |    No    |    No     | Cadena  |                             |
| user_profile_image_url | Una URL basada en HTTP que apunta a la imagen de perfil del usuario                                                                                                               |    No    |    No     | Cadena  |                             |
| entities_url           | Enlaces mencionados                                                                                                                                                               |    no    |    no     | Cadena  |                             |
| hashtags               | Hashtags referenciados en el texto                                                                                                                                                |    No    |    No     | Cadena  |                             |
| user_mentions          | Nombres referenciados en el texto                                                                                                                                                 |    No    |    No     | Cadena  |                             |
| time_distance          | Horas transcurridas entre la fecha de publicación y la de captura                                                                                                                 |    No    |    No     | Decimal |                             |
| reply                  | Indica sí es una respuesta a un tweet original                                                                                                                                             |    No    |    No     | Boleano |                             |
| quote                  | Indica sí es una cita a un un tweet original                                                                                                                                             |    No    |    No     | Boleano |                             |

### Notas importantes a los campos "reply" (respuesta) y "quote" (cita)
| **Aspecto**      | **Respuesta (Reply)**                                     | **Cita (Quote)**                                                     |
|------------------|----------------------------------------------------------|----------------------------------------------------------------------|
| **Propósito**    | Participar en una conversación directa                   | Referenciar o comentar sobre un tweet de forma independiente         |
| **Vinculación**  | `in_reply_to_status_id` apunta al tweet original         | `referenced_tweets` con `type: "quoted"` apunta al tweet citado       |
| **Visualización**| Aparece en el hilo de conversación                       | Aparece como un tweet independiente con el tweet citado embebido     |
| **Contexto**     | Parte de una cadena de diálogo                           | Añade una capa adicional de comentario o contexto                    |
| **Contabilización** | Se computa como un <b>post</b> único, aunque tenga vinculación al tweet original | Se computa como un <b>post</b> único, aunque tenga vinculación al tweet original |


## Ejemplo de respuesta en formato json:

```json
"response" : {
    "data" : [{
        "id": "...",
        "hash": "...",
        "published" : "...",
        "crawled" : "...",
        "updated" : "...",
        "post_id" : "...",
        "url" : "...",
        "text" : "...",
        "lang" : "...",
        "retweet_count" : "...",
        "reply_count" : "...",
        "favorite_count" : "...",
        "reproductions_count" : "...",
        "created_at" : "...",
        "user_name" : "...",
        "user_screen_name" : "...",
        "user_url" : "...",
        "user_profile_image_url" : "...",
        "entities_url" : "...",
        "hashtags" : "...",
        "user_mentions" : "...",
        "time_distance" : "...",
        "reply" : "...",
    }],
    "totalResults" : "...",
    "restResults" : "...",
    "next" : "..."
}
```
## Ejemplo de salida

```
requestLeft	9999999
totalResults	295404987
next	"http://twitter.trawlingweb.com/posts/1234567891234567891234567891234567.123456789?token=1234567891234567891234567891234567891234&ts=1555327617000&tSí=1554076800000"
}

# Contacto
Sí tienes alguna pregunta, neceSítas aSístencia, contratar o ampliar tus servicios por favor contacta con nosotros.

**SAT (Soporte Técnico):**
* [Correo SAT](mailto:support@trawlingweb.com)
* [Documentación Oficial](https://docs.trawlingweb.com)

**SAC (Soporte administrativo):**
* [Correo SAC](mailto:gestion@trawlingweb.com)

**Sales (Soporte ventas):**
* [Correo Ventas](mailto:sales@trawlingweb.com)
