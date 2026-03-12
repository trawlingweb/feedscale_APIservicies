# API NEWS & BLOGS - Respuesta de salida

Una vez lanzada una petición al API, éste devolverá una respuesta con dos tipos de datos diferenciados:

## Datos de noticia

| Campo           | descripción                                                                                  | Buscable | Ordenable |          Tipo           |           Formato           | Servicio |
| --------------- | -------------------------------------------------------------------------------------------- | :------: | :-------: | :---------------------: | :-------------------------: | :-------: |
| id              | Código de indentificación asignado por Trawlingweb a cada publicación rastreada.             |    No    |    No     |         Cadena          |                             | API News |
| title           | Título de la publicación.                                                                    |    Si    |    No     |         Cadena          |                             | API News |
| text            | Cuerpo de texto de la publicación.                                                           |    Si    |    No     |         Cadena          |                             | API News |
| published       | Fecha de publicación.                                                                        |    Si    |    Si     |          Fecha          |        ISO 8601-UTC         | API News |
| crawled         | Fecha de indexación. La zona horaria es GMT +1                                                  |    Si    |    Si     |         Entero          | UNIX Timestamp milisegundos | API News |
| url             | Dirección web de la publicación                                                              |    No    |    No     |         Cadena          |                             | API News |
| author          | Autor de la publicación                                                                      |    Si    |    No     |         Cadena          |                             | API News |
| language        | Idioma de la publicación                                                                     |    Si    |    No     |         Cadena          |          ISO 639-1          | API News |
| domain          | Dominio web donde se ha encontrado la publicación.                                           |    Si    |    No     |         Cadena          |                             | API News |
| site            | Sitio web donde se ha encontrado la publicación.                                             |    Si    |    No     |         Cadena          |                             | API News |
| site_type       | Tipo de sitio web segun el tipo de contenidos publicados (news, blogs, discusions y general) |    Si    |    No     |         Cadena          |                             | API News |
| site_language   | Idioma del sitio web.                                                                        |    Si    |    No     |         Cadena          |          ISO 639-1          | API News |
| site_country    | País del sitio web.                                                                          |    Si    |    No     |         Cadena          |         ISO 3166-2          | API News |
| site_region     | Región del sitio web                                                                         |    Si    |    No     |         Cadena          |        ISO 3166-2:ES        | API News |
| site_section    | Sección del sitio web donde se ha encontrado la publicación.                                 |    No    |    No     |         Cadena          |                             | API News |
| section         | Sección en la que se ha encontrado la publicación                                            |    No    |    No     |         Cadena          |                             | API News |
| value           | Valor económico estimado                                                                     |    No    |    No     | Número en coma flotante |                             | API News |
| rank            | Ranking del dominio                                                                          |    No    |    No     |         Entero          |                             | API News |
| unique_visitors | Número de visitantes únicos estimados                                                        |    No    |    No     |         Entero          |                             | API News |
| **url_image**     | URL de la imagen destacada de la publicación (Addon)                                      |    No    |    No     |         Cadena          |                             | Addon   |   

## Datos de petición

| Datos        | Descripción                                                             |  Tipo  | Servicio |
| :----------- | :---------------------------------------------------------------------- | :----: | :-------: |
| requestLeft  | Total de consultas pendientes de la subscripción                        | Entero | API News |
| totalResults | Total de resultados encontrados por la consulta                         | Entero | API News |
| restResults  | Total de resultados encontrados pendientes de entrega                   | Entero | API News |
| next         | URL para continuar con la paginación y así obtener todos los resultados | Cadena | API News |

## Ejemplos de respuesta en formatos json:

### Respuesta básica:

```json
{"response":
{
"data": [
{
"site_region": "",
"site_type": "news",
"author": "Marta Sierra",
"crawled": 1728546820509,
"unique_visitors": 6823823,
"language": "es",
"section": "",
"published": "2024-10-10T07:42:05.000Z",
"title": "El miedo que bloqueó a Ana Peleteiro en su final olímpica",
"site_section": "https://www.infobae.com/tag/espana-deportes/",
"url": "https://www.infobae.com/espana/deportes/2024/10/10/el-miedo-que-bloqueo-a-ana-peleteiro-en-su-final-olimpica",
"site": "infobae.com",
"site_country": "ar",
"domain": "infobae.com",
"rank": 403,
"text": "La deportiva, que obtuvo el bronce en Tokio, no consiguió medalla olímpica en los Juegos de París 2024 y quedó en una sexta posición Imagen de archivo de la triplista española Ana Peleteiro en los Juegos Olímpicos de París 2024, tras uno de sus saltos (REUTERS/Dylan Martinez) Ana Peleteiro vio truncado su deseo de conseguir su segundo medalla olímpica en París 2024. La deportista española, especialista en la prueba de triple salto, ha hablado sobre lo que pasó ese 3 de agosto con Vicky Berrocal en el podcast de Podium A solas con: “Me daba miedo lesionarme”. La triplista no se lesionó, pero se quedó sin medalla al obtener un sexto puesto. Peleteiro se estrenó en la competición olímpica en Tokio 2020, en la que consiguió una medalla de bronce con un salto de 14,87 metros, convirtiendo la marca en el récord de España. París podría haber sido la oportunidad para hacerse con una nueva medalla o incluso batir su propio récord. Sin embargo, la lluvia se lo impidió. La tarde del 3 de agosto el cielo del Stade de Francia era oscuro y húmedo. Peleteiro hizo un primer salto de 14,55 metros, “la mejor apertura de competición de mi vida”, expresa la atleta. En el segundo se quedó corta con una marca de 13,73 metros al apoyarse mal en el step. Para su tercer salto, la lluvia comenzó a caer con fuerza, mojando la pista en la que las deportivas se jugaban la competición. Todas las deportistas, a excepción de Ana Peleteiro y la cubana Povea, hicieron menos metros en sus siguientes saltos a causa del clima, pero los 14,59 metros que consiguió en su cuarto intento no le permitieron subir al podio. “Yo soy una deportista de saltar más al final de la competición. Si miras mi currículum en todos los campeonatos, mis mejores saltos siempre son en el cuarto o el quinto intento. Como que me voy calentando, soy una diésel...”. La atleta española Ana Peleteiro en una imagen de archivo durante los Juegos Olímpicos de París 2024 (EFE/Julio Muñoz) La organización se afanó en secar la tabla durante el resto del concurso, pero la mente de la gallega no paraba de darle vueltas a la posibilidad de sufrir una lesión: “Como yo aquí ahora me rompa un tendón de Aquiles o un isquio porque resbalo en la tabla, que ahora deslizan mucho y le ha pasado a mucha gente...”. Con ese pensamiento y ante el hecho de que la lluvia no finalizaba, Peleteiro no consiguió enfocarse del todo en la competición y no superó los 14,67 metros con los que la estadounidense Jasmine Moore quedó el tercera posición. En su charla con Vicky Berrocal ha hablado de que, en esos momentos, pensó en su hija de dos años y en que, si esa lesión se producía, apartaría temporalmente el deporte: “Me veo con 28 años, una hija y una lesión que me aparta dos años, y a lo mejor aparto de manera temporal el atletismo, vuelvo a tener otro niño y mis prioridades cambian”. La atleta ha explicado que nunca ha priorizado el deporte como lo más importante de su vida, lo que le ha permitido dar un cambio y trasladarse al pueblo en el que nació, Ribeira. Al terminar la temporada, anunció que abandonaba el grupo de Iván Pedroso, que la había estado entrenando en Guadalajara desde 2016. Ahora se encuentra bajo las órdenes de su marido, Benjamin Compaoré, que también es atleta especialista en triple salto. Ana Peleteiro, aunque no cumplió sus propias expectativas en París 2024, tendrá una nueva oportunidad para conseguir su segunda medalla olímpica en los Juegos de Los Ángeles 2028. Ana Peleteiro, atleta olímpica de triple salto.",
"site_language": "es",
"value": 25476.1,
"id": "07836b97f2830eae484ef5d34f522ceb"
    }],
    "requestLeft" : "...",
    "totalResults" : "...",
    "restResults" : "...",
    "next" : "..."
}
}
```

### Respuesta con Addon `url_image`

```json
{"response":
{
"data": [
{
"site_region": "",
"site_type": "news",
"author": "Marta Sierra",
"crawled": 1728546820509,
"unique_visitors": 6823823,
"language": "es",
"section": "",
"published": "2024-10-10T07:42:05.000Z",
"title": "El miedo que bloqueó a Ana Peleteiro en su final olímpica",
"site_section": "https://www.infobae.com/tag/espana-deportes/",
"url": "https://www.infobae.com/espana/deportes/2024/10/10/el-miedo-que-bloqueo-a-ana-peleteiro-en-su-final-olimpica",
"url_image": "https://www.infobae.com/resizer/v2/CHUZQPCM3VCS6E4TUQIZXVQHP4.jpg?auth=b5c6866d84991f4798722859bdf94b06cf6fac83c095bdcaca6925ef41dbe250&smart=true&width=992&height=661&quality=85",
"site": "infobae.com",
"site_country": "ar",
"domain": "infobae.com",
"rank": 403,
"text": "La deportiva, que obtuvo el bronce en Tokio, no consiguió medalla olímpica en los Juegos de París 2024 y quedó en una sexta posición Imagen de archivo de la triplista española Ana Peleteiro en los Juegos Olímpicos de París 2024, tras uno de sus saltos (REUTERS/Dylan Martinez) Ana Peleteiro vio truncado su deseo de conseguir su segundo medalla olímpica en París 2024. La deportista española, especialista en la prueba de triple salto, ha hablado sobre lo que pasó ese 3 de agosto con Vicky Berrocal en el podcast de Podium A solas con: “Me daba miedo lesionarme”. La triplista no se lesionó, pero se quedó sin medalla al obtener un sexto puesto. Peleteiro se estrenó en la competición olímpica en Tokio 2020, en la que consiguió una medalla de bronce con un salto de 14,87 metros, convirtiendo la marca en el récord de España. París podría haber sido la oportunidad para hacerse con una nueva medalla o incluso batir su propio récord. Sin embargo, la lluvia se lo impidió. La tarde del 3 de agosto el cielo del Stade de Francia era oscuro y húmedo. Peleteiro hizo un primer salto de 14,55 metros, “la mejor apertura de competición de mi vida”, expresa la atleta. En el segundo se quedó corta con una marca de 13,73 metros al apoyarse mal en el step. Para su tercer salto, la lluvia comenzó a caer con fuerza, mojando la pista en la que las deportivas se jugaban la competición. Todas las deportistas, a excepción de Ana Peleteiro y la cubana Povea, hicieron menos metros en sus siguientes saltos a causa del clima, pero los 14,59 metros que consiguió en su cuarto intento no le permitieron subir al podio. “Yo soy una deportista de saltar más al final de la competición. Si miras mi currículum en todos los campeonatos, mis mejores saltos siempre son en el cuarto o el quinto intento. Como que me voy calentando, soy una diésel...”. La atleta española Ana Peleteiro en una imagen de archivo durante los Juegos Olímpicos de París 2024 (EFE/Julio Muñoz) La organización se afanó en secar la tabla durante el resto del concurso, pero la mente de la gallega no paraba de darle vueltas a la posibilidad de sufrir una lesión: “Como yo aquí ahora me rompa un tendón de Aquiles o un isquio porque resbalo en la tabla, que ahora deslizan mucho y le ha pasado a mucha gente...”. Con ese pensamiento y ante el hecho de que la lluvia no finalizaba, Peleteiro no consiguió enfocarse del todo en la competición y no superó los 14,67 metros con los que la estadounidense Jasmine Moore quedó el tercera posición. En su charla con Vicky Berrocal ha hablado de que, en esos momentos, pensó en su hija de dos años y en que, si esa lesión se producía, apartaría temporalmente el deporte: “Me veo con 28 años, una hija y una lesión que me aparta dos años, y a lo mejor aparto de manera temporal el atletismo, vuelvo a tener otro niño y mis prioridades cambian”. La atleta ha explicado que nunca ha priorizado el deporte como lo más importante de su vida, lo que le ha permitido dar un cambio y trasladarse al pueblo en el que nació, Ribeira. Al terminar la temporada, anunció que abandonaba el grupo de Iván Pedroso, que la había estado entrenando en Guadalajara desde 2016. Ahora se encuentra bajo las órdenes de su marido, Benjamin Compaoré, que también es atleta especialista en triple salto. Ana Peleteiro, aunque no cumplió sus propias expectativas en París 2024, tendrá una nueva oportunidad para conseguir su segunda medalla olímpica en los Juegos de Los Ángeles 2028. Ana Peleteiro, atleta olímpica de triple salto.",
"site_language": "es",
"value": 25476.1,
"id": "07836b97f2830eae484ef5d34f522ceb"
    }],
    "requestLeft" : "...",
    "totalResults" : "...",
    "restResults" : "...",
    "next" : "..."
}
}
```
### Ejemplo de salida de una llamada a la API:

#### Standard
```
requestLeft	9999999
totalResults	295404987
restResults	295404887
next	"http://api.trawlingweb.com/?token=0000000000000000000000000000&q=casa&ts=1517443760316&tsi=1524818189854"

```
#### AdHoc
```
requestLeft	9999999
totalResults	295404987
restResults	295404887
next	"http://SIGLAS_CLIENTE.trawlingweb.com/?token=0000000000000000000000000000&q=casa&ts=1517443760316&tsi=1524818189854"

```

# Contacto
Si tienes alguna pregunta, necesitas asistencia, contratar o ampliar tus servicios por favor contacta con nosotros.

**SAT (Soporte Técnico):**
* [Correo SAT](mailto:support@trawlingweb.com)
* [Documentación Oficial](https://docs.trawlingweb.com)

**SAC (Soporte administrativo):**
* [Correo SAC](mailto:gestion@trawlingweb.com)

**Sales (Soporte ventas):**
* [Correo Ventas](mailto:marketing@trawlingweb.com)


