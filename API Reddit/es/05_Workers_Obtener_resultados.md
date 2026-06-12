# API Reddit - Método GET /posts

Permite obtener resultados procesados de cada Worker configurado de Reddit.
Se pueden usar delimitadores temporales para acotar el contenido devuelto y consultas booleanas adicionales mediante `q=`.

# Parámetros GET

Veamos la estructura de la consulta de ejemplo:

```
https://reddit.trawlingweb.com/posts/{WORKERID}?token={APIKEY}&ts=1518472804000&tsi=1524818189854
```

## Parámetros PATH

| Elemento  | Descripción                                  |
| :-------- | :------------------------------------------- |
| protocolo | Puede ser tanto **http** como **https**      |
| dominio   | Dirección de la API reddit.trawlingweb.com   |
| método    | posts                                        |
| workerid  | WORKERID de acceso al sistema de TrawlingWeb.|

## Parámetros QUERY

| Parámetro | Descripción                                                                  | Default                                                 | Ejemplo                  |
| :-------- | :--------------------------------------------------------------------------- | :------------------------------------------------------ | :----------------------- |
| token     | APIKEY de acceso del cliente al sistema de TrawlingWeb.                      | Valor obligatorio                                       | ?token={APIKEY}          |
| q         | Consulta booleana / Lucene adicional (incluye filtro por `subreddit:`)       | Vacío                                                   | &q=subreddit:soccer      |
| ts        | Delimitador temporal inicial. Formato Unix Time en milisegundos              | Delimita a 1 mes en el pasado a partir de la petición   | &ts=1518472804000        |
| tsi       | Delimitador temporal final. Formato Unix Time en milisegundos                | Delimita con la fecha de petición                       | &tsi=1524818189854       |
| size      | Número máximo de resultados por respuesta                                    | `default_maxsize` del plan (típicamente 100)            | &size=50                 |

> Nota: los rangos `ts`/`tsi` se validan con un máximo de 1 mes hacia atrás respecto a la fecha actual. Si `ts > tsi` la API devuelve un error.

# Respuesta de salida - RESPONSE

Una vez lanzada una petición a la API de Reddit, esta devolverá una respuesta estructurada de la siguiente forma:

## Datos del post / comentario

| Campo            | Descripción                                                                       | Buscable | Ordenable |  Tipo  |              Formato              |
| ---------------- | --------------------------------------------------------------------------------- | :------: | :-------: | :----: | :--------------------------------: |
| id               | Código de identificación asignado por Trawlingweb                                  |    No    |    No     | Cadena |                                    |
| post_id          | ID del post o comentario en Reddit                                                |    No    |    No     | Cadena |                                    |
| url              | URL pública del post o comentario en Reddit                                       |    No    |    No     | Cadena |                                    |
| text             | Texto del post o comentario                                                       |    Sí    |    No     | Cadena |                                    |
| subreddit        | Subreddit donde aparece el contenido                                              |    Sí    |    No     | Cadena |                                    |
| published        | Fecha de publicación                                                              |    No    |    Sí     | Fecha  |          ISO 8601-UTC              |
| crawled          | Fecha y hora en que se capturó el contenido                                       |    No    |    Sí     | Entero | Timestamp UNIX en milisegundos     |

## Datos del autor

| Campo             | Descripción                                            | Buscable | Ordenable |  Tipo  | Formato |
| ----------------- | ------------------------------------------------------ | :------: | :-------: | :----: | :-----: |
| user_name         | Nombre del autor                                       |    Sí    |    No     | Cadena |         |
| user_screen_name  | Nombre técnico (u/username) del autor                  |    Sí    |    No     | Cadena |         |

## Datos de la petición

| Campo        | Descripción                                                             |  Tipo  |
| :----------- | :---------------------------------------------------------------------- | :----: |
| totalResults | Total de resultados encontrados por la consulta                         | Entero |
| restResults  | Resultados pendientes tras esta página                                  | Entero |
| next         | URL para continuar con la paginación y así obtener todos los resultados | Cadena |

## Ejemplo de respuesta en formato JSON:

```json
{
  "response": {
    "data": [
      {
        "id": "...",
        "post_id": "...",
        "url": "https://www.reddit.com/r/soccer/comments/abc123/title/",
        "text": "...",
        "subreddit": "soccer",
        "user_name": "...",
        "user_screen_name": "username",
        "published": "2024-08-03T11:00:04.000Z",
        "crawled": 1722682829465
      }
    ],
    "totalResults": 12345,
    "restResults": 12245,
    "next": "https://reddit.trawlingweb.com/posts/{WORKERID}?token={APIKEY}&ts=...&tsi=..."
  }
}
```

# API Reddit - Mejores prácticas

Con el fin de utilizar la API es necesario llamar a una URL de punto final con su token de acceso privado y su id de Worker.
Puede generar la URL de su llamada en nuestro Testeador visual de la API (que debe acceder a https://dashboard.trawlingweb.com/workers).

## Integridad de los datos

Cada solicitud a la API puede devolver un número máximo de resultados igual al `size` configurado (límite del plan). Sin embargo, puede haber muchos más resultados. Para consumir todos los datos ha de seguir realizando llamadas a la URL indicada en el parámetro **next** de la salida de cada solicitud.

## Ejemplo de salida

```
totalResults  295404987
restResults   295404887
next          "https://reddit.trawlingweb.com/posts/1234567891234567891234567891234567.12345678?token=1234567891234567891234567891234567891234&ts=1555327617000&tsi=1554076800000"
```

## Paginación

Al realizar peticiones a `/posts/:worker_id` estas devuelven un máximo definido por el plan (típicamente 100). Se habilita una URL de `next` para continuar con la obtención si los resultados superan dicha cantidad.

# Contacto
Si tienes alguna pregunta, necesitas asistencia, contratar o ampliar tus servicios por favor contacta con nosotros.

**SAT (Soporte Técnico):**
* [Correo SAT](mailto:support@trawlingweb.com)
* [Documentación Oficial](https://github.com/trawlingweb/APIservicies/tree/main/API%20Reddit)

**SAC (Soporte administrativo):**
* [Correo SAC](mailto:gestion@trawlingweb.com)

**Sales (Soporte ventas):**
* [Correo Ventas](mailto:sales@trawlingweb.com)
