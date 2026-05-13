# API PRINT MEDIA – Parámetros de Filtrado

Durante el proceso de indexación y auditoría de fuentes de **Print Media** (prensa escrita/medios impresos), TrawlingWeb asigna a cada artículo una serie de **filtros** (metadatos estructurados) que te permiten afinar las consultas y obtener solo los registros que te interesan. A continuación tienes la referencia completa:

---

## Filtros Disponibles

| Filtro          | Descripción                                                                       |
| :-------------- | :-------------------------------------------------------------------------------- |
| `site`          | Nombre del medio impreso (p.ej. “Expreso”, “El Comercio”, “La Razón”).            |
| `domain`        | Dominio web asociado al medio (p.ej. `diario-expreso.com`).                       |
| `title`         | Palabras o expresiones que deben (o no deben) aparecer en el título del artículo. |
| `text`          | Palabras o expresiones que deben (o no deben) aparecer en el cuerpo del artículo. |
| `language`      | Idioma del artículo. Códigos según ISO 639-1 (p.ej. `es`, `en`, `fr`).            |
| `site_language` | Idioma oficial del medio impreso. Códigos ISO 639-1.                              |
| `site_country`  | País del medio impreso. Códigos ISO 3166-1 alpha-2 (p.ej. `ec`, `es`, `co`).      |
| `site_region`   | Región geográfica del medio impreso. Basada en ISO 3166-2.                        |
| `author`        | Nombre del autor o periodista (p.ej. `MARIELA ROSERO CH.`).                       |
| `published`     | Fecha de publicación del artículo. Timestamp Unix en milisegundos.                |
| `crawled`       | Fecha de rastreo/indexación. Timestamp Unix en milisegundos.                      |
| `site_type`     | Tipo de medio impreso (p.ej. `Newspaper`, `Magazine`).                            |

---

## Sintaxis de la expresión de filtro

Para combinar varios filtros y operadores booleanos (AND, OR, NOT), utiliza la clave `q=` de esta forma:

```
q="(filtro1:valor1) OPERADOR (filtro2:valor2) OPERADOR ... (filtroN:valorN)"
```

> **Importante**: en la URL real debes eliminar los espacios alrededor de los dos puntos y operadores.

---

## Caracteres reservados y escapado

Si tu filtro debe incluir alguno de los siguientes caracteres (que Lucene interpreta como operadores), escápalos con `\`:

```
+ - && || ! ( ) { } [ ] ^ " ~ * ? : \ /
```

Por ejemplo, para filtrar por URL de imagen:

```
q="url_image:https\:\/\/static\.eldiario\.es\/clip\/bd46d652*"
```

---

## Ejemplos de uso de `q=`

| Ejemplo                                                                         | Explicación                                                                                                   |
| :------------------------------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------ |
| `(site:expreso.com OR site:comercio.com)`                                       | Solo artículos de “expreso.com” o “comercio.com”.                                                             |
| `NOT (site:lavanguardia.com AND site:elpais.com)`                               | Todos los artículos excepto los de “lavanguardia.com” y “elpais.com”.                                         |
| `((title:Corte AND (text:sentencias OR text:Constitucional)) NOT title:tibios)` | Artículos cuyo título contenga “Corte” y, en el cuerpo, “sentencias” o “Constitucional”, excluyendo “tibios”. |
| `(language:es OR language:en)`                                                  | Solo artículos en español o inglés.                                                                           |
| `site_language:es AND site_country:ec`                                          | Medios cuyo idioma sea español y país Ecuador.                                                                |
| `author:Romero`                                                                 | Artículos firmados por cualquier autor que contenga “Romero”.                                                 |
| `site_type:Magazine`                                                            | Solo artículos de medios clasificados como “Magazine”.                                                        |

---

Con estos filtros y la lógica booleana de Lucene podrás recuperar **exactamente** los artículos de prensa escrita que te interesan, sin procesar datos irrelevantes.

---

# Contacto

¿Dudas o necesitas más asistencia?

**Soporte Técnico (SAT):** [support@trawlingweb.com](mailto:support@trawlingweb.com)
**Soporte Administrativo (SAC):** [gestion@trawlingweb.com](mailto:gestion@trawlingweb.com)
**Ventas (Sales):** [marketing@trawlingweb.com](mailto:marketing@trawlingweb.com)
