# API NEWS & BLOGS - Output Response

Once a request is made to the API, it will return a response with two differentiated data types:

## News Data

| Field           | Description                                                                                  | Searchable | Sortable |          Type           |           Format           | Service |
| --------------- | -------------------------------------------------------------------------------------------- | :------: | :-------: | :---------------------: | :-------------------------: | :-------: |
| id              | Identification code assigned by Trawlingweb to each tracked publication.             |    No    |    No     |         String          |                             | API News |
| title           | Title of the publication.                                                                    |    Yes   |    No     |         String          |                             | API News |
| text            | Publication text body.                                                           |    Yes   |    No     |         String          |                             | API News |
| published       | Publication date.                                                                        |    Yes   |    Yes    |          Date          |        ISO 8601-UTC         | API News |
| crawled         | Indexing date. The time zone is GMT +1                                                  |    Yes   |    Yes    |         Integer          | UNIX Timestamp milliseconds | API News |
| url             | Web address of the publication                                                              |    No    |    No     |         String          |                             | API News |
| author          | Author of the publication                                                                      |    Yes   |    No     |         String          |                             | API News |
| language        | Language of the publication                                                                     |    Yes   |    No     |         String          |          ISO 639-1          | API News |
| domain          | Web domain where the publication was found.                                           |    Yes   |    No     |         String          |                             | API News |
| site            | Website where the publication was found.                                             |    Yes   |    No     |         String          |                             | API News |
| site_type       | Website type according to the type of content published (news, blogs, discussions and general) |    Yes   |    No     |         String          |                             | API News |
| site_language   | Website language.                                                                        |    Yes   |    No     |         String          |          ISO 639-1          | API News |
| site_country    | Website country.                                                                          |    Yes   |    No     |         String          |         ISO 3166-2          | API News |
| site_region     | Website region                                                                         |    Yes   |    No     |         String          |        ISO 3166-2:ES        | API News |
| site_section    | Section of the website where the publication was found.                                 |    No    |    No     |         String          |                             | API News |
| section         | Section in which the publication was found                                            |    No    |    No     |         String          |                             | API News |
| value           | Estimated economic value                                                                     |    No    |    No     | Floating point number |                             | API News |
| rank            | Domain ranking                                                                          |    No    |    No     |         Integer          |                             | API News |
| unique_visitors | Number of estimated unique visitors                                                        |    No    |    No     |         Integer          |                             | API News |
| **url_image**     | URL of the highlighted image of the publication (Addon)                                      |    No    |    No     |         String          |                             | Addon   |   

## Request Data

| Data        | Description                                                             |  Type  | Service |
| :----------- | :---------------------------------------------------------------------- | :----: | :-------: |
| requestLeft  | Total pending queries in the subscription                        | Integer | API News |
| totalResults | Total results found for the query                         | Integer | API News |
| restResults  | Total results found pending delivery                   | Integer | API News |
| next         | URL to continue pagination and obtain all results | String | API News |

## Examples of JSON response formats:

### Basic response:

This is a basic example, not a literal JSON string:

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

### Response with `url_image` Addon:

This is a basic example, not a literal JSON string:

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
"text": "La deportiva, que obtuvo el bronce en Tokio, no consiguió medalla olímpica en los Juegos de París 2024 y quedó en una sexta posición Imagen de archivo de la triplista española Ana Peleteiro en los Juegos Olímpicos de París 2024, tras uno de sus saltos (REUTERS/Dylan Martinez) Ana Peleteiro vio truncado su deseo de conseguir su segundo medalla olímpica en París 2024. La deportista española, especialista en la prueba de triple salto, ha hablado sobre lo que pasó ese 3 de agosto con Vicky Berrocal en el podcast de Podium A solas con: “Me daba miedo lesionarme”. La triplista no se lesionó, pero se quedó sin medalla al obtener un sexto puesto. Peleteiro se estrenó en la competición olímpica en Tokio 2020, en la que consiguió una medalla de bronce con un salto de 14,87 metros, convirtiendo la marca en el récord de España. París podría haber sido la oportunidad para hacerse con una nueva medalla o incluso batir su propio récord. Sin embargo, la lluvia se lo impidió. La tarde del 3 de agosto el cielo del Stade de Francia era oscuro y húmedo. Peleteiro hizo un primer salto de 14,55 metros, “la mejor apertura de competición de mi vida”, expresa la atleta. En el segundo se quedó corta con una marca de 13,73 metros al apoyarse mal en el step. Para su tercer salto, la lluvia comenzó a caer con fuerza, mojando la pista en la que las deportivas se jugaban la competición. Todas las deportistas, a excepción de Ana Peleteiro y la cubana Povea, hicieron menos metros en sus siguientes saltos a causa del clima, but the 14.59 meters that he got in his fourth attempt did not allow him to get on the podium. “I am an athlete who jumps more at the end of the competition. If you look at my resume in all the championships, my best jumps are always in the fourth or fifth attempt. As I warm up, I'm a diesel...". The Spanish athlete Ana Peleteiro in an archive image during the Paris 2024 Olympic Games (EFE/Julio Muñoz) The organization was busy drying the board for the rest of the competition, but the mind of the Galician woman kept turning over the possibility of suffering an injury: “If I break an Achilles tendon or a hamstring here because I slip on the board, which is now very slippery and has happened to a lot of people...". With that thought, and given the fact that the rain was not stopping, Peleteiro couldn't focus entirely on the competition and didn't exceed the 14.67 meters with which the American Jasmine Moore finished third. In her talk with Vicky Berrocal she has spoken about how, at that moment, she thought about her two-year-old daughter and that, if that injury occurred, she would temporarily leave the sport: "I see myself at 28, with a daughter and an injury that keeps me away for two years, and maybe I'll temporarily leave athletics, have another child and my priorities will change." The athlete has explained that she has never prioritized sport as the most important thing in her life, which has allowed her to make a change and move to the town where she was born, Ribeira. At the end of the season, she announced that she was leaving Iván Pedroso's group, who had been training her in Guadalajara since 2016. She is now under the orders of her husband, Benjamin Compaoré, who is also a triple jump athlete. Ana Peleteiro, although she did not meet her own expectations in Paris 2024, will have a new opportunity to win her second Olympic medal at the Los Angeles 2028 Games. Ana Peleteiro, Olympic triple jump athlete.",
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

# Contact
If you have any questions, need assistance, need to contract or expand your services, please contact us.

**SAT (Technical Support):**
* [SAT Email](mailto:support@trawlingweb.com)
* [Official Documentation](https://docs.trawlingweb.com)

**SAC (Administrative Support):**
* [SAC Email](mailto:gestion@trawlingweb.com)

**Sales (Sales Support):**
* [Sales Email](mailto:marketing@trawlingweb.com)


