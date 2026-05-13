# API Instagram - Método GET /comments

Permite obtener los **comentarios** capturados de un post concreto de Instagram. Está pensado como un **drill-down** desde `GET /posts`: primero se consultan las publicaciones de un Worker, y después, para cada publicación de la que se quieran ver los comentarios, se hace una llamada adicional a `/comments` indicando el `post_id`. **Cada llamada a `/comments` es una consulta facturable independiente** dentro de tu plan.

# Parámetros GET

Veamos la estructura de la consulta de ejemplo:

```
https://instagram.trawlingweb.com/comments?token={APIKEY}&post_id={POST_ID}
```

## Parámetros QUERY

| Parámetro | Descripción                                                                  | Default                                                  | Ejemplo                       |
| :-------- | :--------------------------------------------------------------------------- | :------------------------------------------------------- | :---------------------------- |
| token     | APIKEY de acceso del cliente al sistema de TrawlingWeb.                      | Valor obligatorio                                        | ?token={APIKEY}               |
| post_id   | Identificador de la publicación de Instagram cuyos comentarios se solicitan. Se obtiene del campo `post_id` del response de `GET /posts/{WORKERID}`. | Valor obligatorio                  | &post_id=3893360753113419201 |
| country_pref | Preferencia de país del cliente (ISO 3166-1 alpha-2, ej: `es`). **Obligatorio para contratos FeedScale Pay-per-Use**. Su omisión penaliza multiplicando x2.5 el coste de la request y conlleva riesgo de bloqueo de acceso. | Obligatorio (Pay-per-Use) | &country_pref=es |
| ts        | Delimitador temporal inicial. Formato Unix Time en milisegundos.              | Delimita a **30 días** en el pasado a partir de la petición | &ts=1518472804000          |
| tsi       | Delimitador temporal final. Formato Unix Time en milisegundos.                | Delimita con la fecha de petición                        | &tsi=1524818189854           |
| size      | (Opcional) Número de resultados por página. Máximo 100 (estándar) o 500 (admin). | 100                                                  | &size=50                     |

> **Nota — ventana temporal**: el endpoint `/comments` usa una ventana default de **30 días** (vs 1 mes de `/posts`), pensada porque los comentarios suelen consultarse en horizontes más cortos que las publicaciones.

> **Nota — flujo recomendado**: primero `GET /posts/{WORKERID}` para obtener la lista de publicaciones del Worker. Después, por cada `post_id` del que quieras ver los comentarios, una llamada a `GET /comments?post_id=...`. Cada llamada se factura como una consulta independiente.

# ⚠️ Importante — llamadas estériles también se facturan

`GET /comments?post_id=X` consulta el repositorio compartido de comentarios capturados por TrawlingWeb. Si **nadie** ha configurado un Worker `subtype=comments` que monitorice al autor del post solicitado, el endpoint devolverá:

```json
{ "response": { "data": [], "totalResults": 0, "restResults": 0 } }
```

… y **la llamada se facturará igualmente** dentro de tu cuota de consultas.

**Para evitar consultas estériles**, asegúrate de tener creado al menos un Worker con `type=instagram` y `subtype=comments` que monitorice al autor de los posts cuyos comentarios quieras analizar. La creación de Workers de tipo comments se documenta en [04_Workers_Creación.md](./04_Workers_Creación.md).

# Respuesta de salida - RESPONSE

Una vez lanzada una petición, el endpoint devuelve una respuesta estructurada. El **wrapper** (`data`, `totalResults`, `restResults`, `next`) es **idéntico** al de `/posts`, pero el shape interno de cada elemento es distinto: cada `data[i]` es un comentario, no una publicación.

## Datos del comentario

| Campo            | Descripción                                                                                | Buscable | Ordenable |  Tipo   |          Formato                |
| ---------------- | ------------------------------------------------------------------------------------------ | :------: | :-------: | :-----: | :-----------------------------: |
| id               | Identificador interno del documento. Determinista: `<parent_post_id>_<comment_id>`.        |    No    |    No     | Cadena  |                                 |
| comment_id       | ID del comentario en Instagram.                                                            |    No    |    No     | Cadena  |                                 |
| parent_post_id   | ID del post al que pertenece el comentario.                                                |    No    |    No     | Cadena  |                                 |
| parent_post_url  | URL del post padre.                                                                        |    No    |    No     | Cadena  |                                 |
| worker_id        | WORKERID del Worker que capturó el comentario.                                             |    No    |    No     | Cadena  |                                 |
| client_id        | ID interno del cliente al que pertenece el Worker.                                         |    No    |    No     | Entero  |                                 |
| type             | Tipo de documento — siempre `"comment"`.                                                   |    No    |    No     | Cadena  |                                 |
| platform         | Plataforma — siempre `"instagram_comments"`.                                               |    No    |    No     | Cadena  |                                 |
| text             | **Texto del comentario** (no del post).                                                    |    No    |    No     | Cadena  |                                 |
| likes            | **Me gusta del comentario** (no del post).                                                 |    No    |    No     | Entero  |                                 |
| ad_value         | Valor publicitario estimado (modelo híbrido: audience potential × CPM ajustado por likes). |    No    |    No     | Decimal |                                 |
| crawled          | Fecha y hora en que se procesó/capturó el comentario.                                      |    No    |    Sí     | Entero  | Timestamp UNIX en milisegundos  |
| raw              | Objeto crudo del scrape original. **No buscable** (`enabled: false` en el mapping).        |    No    |    No     | Objeto  |                                 |

## Datos del autor del comentario

| Campo            | Descripción                                                              | Buscable | Ordenable |  Tipo    | Formato |
| ---------------- | ------------------------------------------------------------------------ | :------: | :-------: | :------: | :-----: |
| user_name        | **Nombre de usuario del autor del comentario** (no del autor del post).  |    No    |    No     | Cadena   |         |
| user_screen_name | Nombre mostrado del autor del comentario. Coincide con `user_name` cuando Instagram no expone el "full name". | No | No | Cadena |  |
| user_profile     | URL de la foto de perfil del autor (puede estar vacía).                  |    No    |    No     | Cadena   |         |
| is_verified      | El autor del comentario tiene cuenta verificada.                         |    No    |    No     | Booleano |         |

## Datos heredados del post padre

> **Importante**: estos campos describen al **autor del POST** y a la **publicación**, no al autor del comentario ni al comentario en sí. Vienen heredados del post padre por convención del proyecto. Si necesitas analizar al autor del comentario, **no uses `user_followers` ni `user_followed`** — siempre verás los del medio al que pertenece el post.

| Campo          | Descripción                                                | Buscable | Ordenable |  Tipo   | Formato       |
| -------------- | ---------------------------------------------------------- | :------: | :-------: | :-----: | :-----------: |
| user_followers | Número de seguidores del **autor del POST padre**.         |    No    |    No     | Entero  |               |
| user_followed  | Número de cuentas seguidas por el **autor del POST padre**.|    No    |    No     | Entero  |               |
| published      | Fecha de publicación del **POST padre** (no del comentario).|   No    |    No     |  Fecha  | ISO 8601-UTC  |

## Datos del Worker (clasificación geográfica)

| Campo   | Descripción                                                          | Buscable | Ordenable |  Tipo   | Formato                |
| ------- | -------------------------------------------------------------------- | :------: | :-------: | :-----: | :--------------------: |
| country | País asociado al Worker que capturó el comentario (ISO 3166-1 alpha-2). | No    |    No     | Cadena  | Ej: `BR`, `ES`, `MX`   |
| lang    | Idioma del comentario. Se deriva automáticamente del campo `country`.|    No    |    No     | Cadena  | ISO 639-1 (`pt`, `es`, `en`...) |

## Datos de la petición

| Campo        | Descripción                                                             |  Tipo   |
| :----------- | :---------------------------------------------------------------------- | :-----: |
| requestLeft  | Total de consultas pendientes de la suscripción.                        | Entero  |
| totalResults | Total de resultados encontrados por la consulta.                        | Entero  |
| restResults  | Resultados restantes después del `size` actual.                         | Entero  |
| next         | URL para continuar con la paginación y obtener todos los resultados.    | Cadena  |

## Ejemplo de respuesta en formato JSON:

```json
{
  "data": [
    {
      "id": "3893360753113419201_18022373657822184",
      "comment_id": "18022373657822184",
      "parent_post_id": "3893360753113419201",
      "parent_post_url": "https://www.instagram.com/p/DYH_vofxc3B/",
      "worker_id": "66d3ba29a337dc2ca3f7745be24f5b29.c23551e0",
      "client_id": 1751,
      "country": "BR",
      "lang": "pt",
      "type": "comment",
      "platform": "instagram_comments",
      "text": "😢😢😢😢 Justiça",
      "user_name": "eurosangela.assuncao",
      "user_screen_name": "eurosangela.assuncao",
      "user_profile": "",
      "is_verified": false,
      "user_followers": 218323,
      "user_followed": 235,
      "likes": 0,
      "ad_value": 327.48,
      "published": "2026-05-09T16:40:51.000Z",
      "crawled": 1778599580642,
      "raw": { "...": "..." }
    }
  ],
  "totalResults": 91,
  "restResults": 90,
  "next": "https://instagram.trawlingweb.com/comments?token=...&post_id=3893360753113419201&ts=...&tsi=..."
}
```

# Diferencias clave respecto a `/posts`

Aunque comparten autenticación y wrapper, los dos endpoints sirven entidades distintas. Estos campos tienen **el mismo nombre con significado diferente**:

| Campo        | En `/posts`                          | En `/comments`                          |
| :----------- | :----------------------------------- | :-------------------------------------- |
| `user_name`  | Autor del post (cuenta del medio)    | Autor del **comentario** (otra persona) |
| `text`       | Caption del post                     | Texto del **comentario**                |
| `likes`      | Me gusta del post                    | Me gusta del **comentario**             |
| `type`       | "photo" / "video" / "carousel"       | Siempre `"comment"`                     |

# Mejores prácticas

## Flujo de uso recomendado

1. **`GET /posts/{WORKERID}`** — obtener la lista de publicaciones del Worker.
2. Para cada `post_id` del response que quieras analizar:
3. **`GET /comments?post_id={POST_ID}`** — obtener los comentarios de ese post.

Cada llamada a `/comments` se factura individualmente. Pide solo los `post_id` que realmente vayas a procesar.

## Integridad de los datos

Cada solicitud al API puede devolver un número máximo de **100 elementos** (estándar). Si los comentarios totales superan ese tope, deberás seguir realizando llamadas a la URL indicada en el parámetro **next** de la salida de cada solicitud.

## Paginación

Al realizar peticiones a `/comments?post_id=...`, el API devuelve un máximo de 100 resultados (o 500 para tokens admin). Cuando hay más, se incluye una `next` URL para continuar.

## Cobertura

Para que un comentario aparezca en este endpoint, alguien debe haber configurado un Worker `subtype=comments` que monitorice al autor del post. Si solicitas un `post_id` que **nadie** monitoriza, recibirás `data: []` y `totalResults: 0` — y la llamada se facturará. Antes de hacer drill-down masivo, asegúrate de tener Workers de comments configurados para tus cuentas de interés.

# Contacto

Si tienes alguna pregunta, necesitas asistencia, contratar o ampliar tus servicios por favor contacta con nosotros.

**SAT (Soporte Técnico):**
* [Correo SAT](mailto:support@trawlingweb.com)
* [Documentación Oficial](https://docs.trawlingweb.com)

**SAC (Soporte administrativo):**
* [Correo SAC](mailto:gestion@trawlingweb.com)

**Sales (Soporte ventas):**
* [Correo Ventas](mailto:sales@trawlingweb.com)
