# API Twitter - Método GET /posts_full Search

Permite obtener resultados capturados de cada Worker configurado en Twitter. Se pueden utilizar delimitadores temporales para acotar el contenido devuelto.

Este es un método avanzado que devuelve resultados completos sobre la publicación de un tweet, ampliando la información en comparación con el método básico. Además de los datos básicos del usuario emisor, este método incluye más detalles relativos al emisor. Es ideal para análisis estadísticos que requieren información detallada sobre el emisor y sus publicaciones.

Adicionalmente, en comparación con otros métodos, este permite utilizar delimitadores temporales para acotar el contenido devuelto, junto con expresiones de búsqueda booleana para refinar aún más los resultados.

# Parámetros GET

Veamos la estructura de la consulta de ejemplo:

```
https://twitter.trawlingweb.com/posts_full/?token={APIKEY}&q={Boollean_Expression}
```

## Parámetros PATH

| Elemento  | Descripción                                 |
| :-------- | :------------------------------------------ |
| protocolo | Puede ser tanto **http** como **https**     |
| dominio   | Dirección de la API twitter.trawlingweb.com |
| método    | posts                                       |

## Parámetros QUERY

| Parámetro | Descripción                                                                                                                                                                                                                | Default                                                 | Ejemplo                       |
| :-------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------ | :---------------------------- |
| token     | APIKEY de acceso del cliente al sistema de TrawlingWeb.                                                                                                                                                                    | Valor obligatorio                                       | ?token={APIKEY}               |
| country_pref| Preferencia de país del cliente (ISO 3166-1 alpha-2, ej: `es`). **Obligatorio para contratos FeedScale Pay-per-Use**. Su omisión penaliza multiplicando x2.5 el coste de la request y conlleva riesgo de bloqueo de acceso. | Obligatorio (Pay-per-Use)                               | &country_pref=es              |
| ts        | Se trata del delimitador temporal inicial. Formato Unix Time en milisegundos                                                                                                                                               | Delimita a 1 meses en el pasado a partir de la petición | &ts=1518472804000             |
| tsi       | Se trata del delimitador temporal final. Formato Unix Time en milisegundos                                                                                                                                                 | Delimita con la fecha de petición                       | &tsi=1524818189854            |
| q         | Expresión construida con palabras o expresiones clave que configura los filtros de búsqueda. Permite hacer combinaciones con los distintos tipos de filtros disponibles mediante los operadores booleanos _y_, _o_ y _no_. |                                                         | &q=("barcelona" AND "Madrid") |

# Respuesta de salida - RESPONSE

Este método tiene como objetivo recuperar todos los resultados relacionados con las palabras clave de un worker. Además, utilizando este método, algunos de los elementos listados a continuación se considerarán buscables y ordenables en los atributos relacionados con fechas.

Una vez enviada una petición al API de Twitter, se recibirá una respuesta estructurada de la siguiente manera:

## Datos de la publicación

| Campo                   | Descripción                                                                                                                                                                       | Buscable | Ordenable |  Tipo   |           Formato           |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------: | :-------: | :-----: | :-------------------------: |
| id                      | Código de indentificación asignado por Trawlingweb a cada publicación rastreada                                                                                                   |    Sí    |    No     | Cadena  |                             |
| hash                    | Código de indentificación en base al texto                                                                                                                                        |    No    |    No     | Cadena  |                             |
| published               | Fecha de publicación (Ver sección mejores prácticas, Uso de las Fechas published y Crawled)                                                                                                                                                           |    Sí    |    Sí     |  Fecha  |        ISO 8601-UTC         |
| crawled                 | Fecha de captura (Ver sección mejores prácticas, Uso de las Fechas published y Crawled)                                                                                                                                                                                                           |    Sí    |    Sí     | Entero  | UNIX Timestamp milisegundos |
| updated                 | Fecha de actualitzación                                                                                                                                                           |    Sí    |    Sí     | Entero  | UNIX Timestamp milisegundos |
| post_id                 | Id del post                                                                                                                                                                       |    No    |    No     | Cadena  |                             |
| url                     | Url de la publicación                                                                                                                                                             |    Sí    |    No     | Cadena  |                             |
| text                    | Texto descrito de la publicación                                                                                                                                                  |    Sí    |    No     | Cadena  |                             |
| lang                    | Cuando está presente, indica un identificador de idioma BCP 47 correspondiente al idioma detectado por la máquina del texto del Tweet, o und si no se pudo detectar ningún idioma |    Sí    |    No     | Cadena  |                             |
| retweet_count           | Número de veces que este Tweet ha sido retwiteado.                                                                                                                                |    No    |    No     | Entero |                             |
| reply_count             | Número de veces que este Tweet ha sido respondido                                                                                                                                 |    No    |    No     | Entero |                             |
| favorite_count          | Indica aproximadamente cuántas veces ha gustado a los usuarios de Twitter este Tweet                                                                                              |    No    |    No     | Entero |                             |
| reproductions_count     | Número de veces que este Tweet ha sido reproducido                                                                                                                                |    No    |    No     | Entero |                             |
| entities_url            | Enlaces mencionados                                                                                                                                                               |    Sí    |    No     | Cadena  |                             |
| url_image               | Enlaces de imagenes                                                                                                                                                               |    no    |    no     | Cadena  |                             |
| hashtags                | Hashtags referenciados en el texto. Si dentro del atributo texto, no del atributo hashtags.                                                                                                                                                |    Sí    |    No     | Cadena  |                             |
| user_mentions           | Nombres referenciados en el texto                                                                                                                                                 |    No    |    No     | Cadena  |                             |
| time_distance           | Horas transcurridas entre la fecha de publicación y la de captura                                                                                                                 |    No    |    No     | Decimal |                             |
| reply                   | Indica sí es un Retweet                                                                                                                                             |    No    |    No     | Booleano |                             |
| user_id                 | Código de indentificación de usuario                                                                                                                                              |    Sí    |    No     | Entero  |                             |
| user_name               | Nombre de usuario                                                                                                                                                                 |    Sí    |    No     | Cadena  |                             |
| user_screen_name        | Nombre de usuario mostrado                                                                                                                                                        |    Sí    |    No     | Cadena  |                             |
| user_creation_date      | Fecha de creación del usuario                                                                                                                                                     |    No    |    No     |  Fecha  |        ISO 8601-UTC         |
| user_url                | Url del usuario                                                                                                                                                                   |    Sí    |    No     | Cadena  |                             |
| user_profile_image_url  | Una URL basada en HTTP que apunta al abatar del perfil del usuario                                                                                                                |    No    |    No     | Cadena  |                             |
| user_profile_banner_url | Una URL basada en HTTP que apunta al banner del perfil del usuario                                                                                                                |    No    |    No     | Cadena  |                             |
| user_description        | Texto descrito del usuario                                                                                                                                                        |    No    |    No     | Cadena  |                             |
| user_external_url       | Url del la descripción del usuario                                                                                                                                                |    No    |    No     | Cadena  |                             |
| user_location           | Ubicación que el usuario específica                                                                                                                                               |    Sí    |    No     | Cadena  |                             |
| user_follower_count     | Número de seguidores del usuario                                                                                                                                                  |    No    |    No     | Entero |                             |
| user_following_count    | Número de seguidos del usuario                                                                                                                                                    |    No    |    No     | Entero |                             |
| user_favourites_count   | Número de favoritos del usuario                                                                                                                                                   |    No    |    No     | Entero |                             |
| user_is_private         | Usuario privado                                                                                                                                                                   |    Sí    |    No     | Booleano |                             |
| user_is_verified        | Usuario verificado                                                                                                                                                                |    Sí    |    No     | Booleano |                             |
| user_is_blue_verified   | Usuario verificado como Blue                                                                                                                                                      |    Sí    |    No     | Booleano |                             |
| user_number_of_tweets   | Número de Tweets realiados por el usario                                                                                                                                          |    No    |    No     | Entero |                             |

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
        "entities_url" : "...",
        "url_image" : "...",
        "hashtags" : "...",
        "user_mentions" : "...",
        "time_distance" : "...",
        "reply" : "...",
        "user_name" : "...",
        "user_screen_name" : "...",
        "user_creation_date" : "...",
        "user_url" : "...",
        "user_profile_image_url" : "...",
        "user_profile_banner_url" : "...",
        "user_description" : "...",
        "user_external_url" : "...",
        "user_location" : "...",
        "user_follower_count" : "...",
        "user_following_count" : "...",
        "user_favourites_count" : "...",
        "user_is_private" : "...",
        "user_is_verified" : "...",
        "user_is_blue_verified" : "...",
        "user_number_of_tweets" : "...",
    }],
    "totalResults" : "...",
    "restResults" : "...",
    "next" : "..."
}
```

# API Twitter - Mejores prácticas

## Integridad de los datos

Cada solicitud al API puede devolver un número máximo de 500 elementos coincidentes con su consulta. Sin embargo, pueden haber muchos más resultados. Para consumir todos los datos ha de seguir realizando llamadas a la URL indicada en el parámetro **next** de las salida de cada solicitud.

## Ejemplo de salida

```
requestLeft	9999999
totalResults	295404987
next	"http://twitter.trawlingweb.com/posts_full/1234567891234567891234567891234567.123456789?token=1234567891234567891234567891234567891234&ts=1555327617000&tsi=1554076800000"
}
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

