# API Print media – Respuesta de salida

Al realizar una petición al API de Prensa Escrita, la respuesta (output) en formato JSON incluye dos bloques de información:

1. **Datos de noticia**
2. **Datos de petición**

---

## Datos de noticia

| Campo                        | Descripción                                                  | Buscable | Ordenable |          Tipo           |       Formato        |    Servicio     |
| ---------------------------- | ------------------------------------------------------------ | :------: | :-------: | :---------------------: | :------------------: | :-------------: |
| `id`                         | Identificador único asignado por TrawlingWeb a cada artículo |    No    |    No     |         Cadena          |                      | API Print media |
| `id_page`                    | Código de página dentro del medio                            |    No    |    No     |         Cadena          |                      | API Print media |
| `published`                  | Fecha de publicación                                         |    Sí    |    Sí     |          Fecha          |     ISO 8601-UTC     | API Print media |
| `crawled`                    | Fecha y hora de rastreo (timestamp en ms)                    |    Sí    |    Sí     |         Entero          | UNIX Timestamp (ms)  | API Print media |
| `updated`                    | Última fecha de actualización del registro                   |    Sí    |    Sí     |          Fecha          |     ISO 8601-UTC     | API Print media |
| `site`                       | Nombre del medio (ej. “Expreso”)                             |    Sí    |    No     |         Cadena          |                      | API Print media |
| `site_language`              | Idioma del medio                                             |    Sí    |    No     |         Cadena          |      ISO 639-1       | API Print media |
| `site_country`               | País del medio                                               |    Sí    |    No     |         Cadena          | ISO 3166-1 (alpha-2) | API Print media |
| `site_type`                  | Tipo de sitio (p.ej. “Newspaper”)                            |    Sí    |    No     |         Cadena          |                      | API Print media |
| `site_tier`                  | Categoría de alcance del medio (p.ej. “1”, “2”)              |    No    |    No     |         Cadena          |                      | API Print media |
| `site_owner`                 | Propietario del medio                                        |    No    |    No     |         Cadena          |                      | API Print media |
| `site_topic`                 | Tema principal del medio (p.ej. “News”)                      |    Sí    |    No     |         Cadena          |                      | API Print media |
| `site_region1` / `region2/3` | Regiones geográficas que cubre el medio                      |    No    |    No     |         Cadena          |                      | API Print media |
| `site_scope`                 | Alcance geográfico (p.ej. “Nacional”)                        |    No    |    No     |         Cadena          |                      | API Print media |
| `title`                      | Título del artículo                                          |    Sí    |    No     |         Cadena          |                      | API Print media |
| `opening`                    | Entradilla / subtítulo                                       |    No    |    No     |         Cadena          |                      | API Print media |
| `text`                       | Texto breve o extracto                                       |    Sí    |    No     |         Cadena          |                      | API Print media |
| `textFull`                   | Texto completo del artículo                                  |    No    |    No     |         Cadena          |                      | API Print media |
| `caption`                    | Pie de foto                                                  |    No    |    No     |         Cadena          |                      | API Print media |
| `note`                       | Notas o comentarios adicionales                              |    No    |    No     |         Cadena          |                      | API Print media |
| `title_vision_paragraphs`    | Párrafos del título con coordenadas de bounding box          |    No    |    No     |    Lista de objetos     |      JSON array      | API Print media |
| `opening_vision_paragraphs`  | Párrafos de la entradilla con bounding box                   |    No    |    No     |    Lista de objetos     |      JSON array      | API Print media |
| `note_vision_paragraphs`     | Párrafos de la nota con bounding box                         |    No    |    No     |    Lista de objetos     |      JSON array      | API Print media |
| `caption_vision_paragraphs`  | Párrafos del pie de foto con bounding box                    |    No    |    No     |    Lista de objetos     |      JSON array      | API Print media |
| `text_vision_paragraphs`     | Párrafos del texto completo con bounding box                 |    No    |    No     |    Lista de objetos     |      JSON array      | API Print media |
| `pages`                      | Número de página en la que aparece el artículo               |    No    |    No     |         Cadena          |                      | API Print media |
| `page`                       | Índice de página                                             |    No    |    No     |         Cadena          |                      | API Print media |
| `audience`                   | Audiencia estimada del medio                                 |    No    |    No     |         Entero          |                      | API Print media |
| `circulation`                | Tirada o ejemplares distribuidos                             |    No    |    No     |         Entero          |                      | API Print media |
| `value`                      | Valor económico estimado                                     |    No    |    No     | Número en coma flotante |                      | API Print media |
| `valuePage`                  | Valor por página                                             |    No    |    No     | Número en coma flotante |                      | API Print media |
| `meta_ocupation`             | Código de ocupación genérico                                 |    No    |    No     |         Cadena          |                      | API Print media |
| `meta_ocupation_fine`        | Código de ocupación detallado                                |    No    |    No     |         Cadena          |                      | API Print media |
| `width` / `height`           | Dimensiones de la página (en píxeles)                        |    No    |    No     |         Entero          |                      | API Print media |
| `nameFile`                   | Nombre del fichero de imagen / PDF                           |    No    |    No     |         Cadena          |                      | API Print media |
| `pathComplete`               | Ruta completa en el repositorio                              |    No    |    No     |         Cadena          |                      | API Print media |
| `boundingBoxMax`             | Coordenadas máximas de la página                             |    No    |    No     |         Objeto          |     JSON object      | API Print media |
| `status_foto`                | Indica si la página incluye foto (`true`/`false`)            |    No    |    No     |         Cadena          |                      | API Print media |
| `status_continue`            | Indica si el análisis TDM continúa en páginas siguientes     |    No    |    No     |         Cadena          |                      | API Print media |

---

## Datos de petición

| Dato           | Descripción                                                  |  Tipo  |    Servicio     |
| :------------- | :----------------------------------------------------------- | :----: | :-------------: |
| `requestLeft`  | Consultas restantes según tu plan                            | Entero | API Print media |
| `totalResults` | Total de artículos encontrados                               | Entero | API Print media |
| `restResults`  | Resultados pendientes de entrega                             | Entero | API Print media |
| `next`         | URL para paginar y obtener la siguiente página de resultados | Cadena | API Print media |

---

## Ejemplo de respuesta (JSON)

```json
{
  "response": {
    "data": [
      {
        "id": "ec_diario-expreso_2025-05-09_0002_44d099c73fdbd3eadf542df170b5beca",
        "id_page": "ec_diario-expreso_2025-05-09_0002",
        "published": "2025-05-09T21:55:04.098Z",
        "crawled": 1746815482346,
        "updated": "2025-05-09T21:55:04.304Z",
        "site": "Expreso",
        "site_language": "es",
        "site_country": "ec",
        "site_type": "Newspaper",
        "site_tier": "1",
        "site_owner": "Grupo Expreso / Granasa",
        "site_topic": "News",
        "site_region1": "Costa",
        "site_region2": "Guayas",
        "site_region3": "Guayaquil",
        "site_scope": "Nacional",
        "title": "La Corte mide sus pasos en ciertos temas y salta en otros",
        "opening": "Constitucionalistas revisan el accionar de jueces…",
        "text": "Constitucionalistas revisan el accionar de jueces…",
        "textFull": "Constitucionalistas revisan el accionar de jueces Les dicen “tibios”…",
        "caption": "",
        "note": "",
        "title_vision_paragraphs": [],
        "opening_vision_paragraphs": [],
        "note_vision_paragraphs": [],
        "caption_vision_paragraphs": [],
        "text_vision_paragraphs": [],
        "pages": "0002",
        "page": "0002",
        "audience": 240000,
        "circulation": 60000,
        "value": 2981,
        "valuePage": 6480,
        "meta_ocupation": "65",
        "meta_ocupation_fine": "46",
        "width": 1904,
        "height": 1701,
        "nameFile": "diario-expreso_page0002.png",
        "pathComplete": "/ec/2025/05/20250509/diario-expreso/",
        "boundingBoxMax": {
          "vertices": [
            { "x": 64, "y": 291 },
            { "x": 1968, "y": 291 },
            { "x": 1968, "y": 1992 },
            { "x": 64, "y": 1992 }
          ]
        },
        "status_foto": "false",
        "status_continue": "false",
        "author": "MARIELA ROSERO CH."
      }
    ],
    "requestLeft": 9999999,
    "totalResults": 1200000,
    "restResults": 1199998,
    "next": "https://api.trawlingweb.com/press-written?page=2&token=YOUR_TOKEN"
  }
}
```

---

Si necesitas ayuda o más información, no dudes en contactar con nosotros:

- **Soporte Técnico (SAT):** [support@trawlingweb.com](mailto:support@trawlingweb.com)
- **Soporte Administrativo (SAC):** [gestion@trawlingweb.com](mailto:gestion@trawlingweb.com)
- **Ventas:** [marketing@trawlingweb.com](mailto:marketing@trawlingweb.com)

---
