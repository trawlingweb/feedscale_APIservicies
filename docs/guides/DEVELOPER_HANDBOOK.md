# Developer Handbook — FeedScale API Services

## Descripcion del Proyecto

Repositorio de documentacion publica de las APIs de **FeedScale** (TrawlingWeb). Contiene guias, specs y ejemplos de uso para cada servicio API: News, Twitter, Facebook, Instagram, YouTube, TikTok y Legal. No contiene codigo de backend — es un repo orientado a clientes y documentacion tecnica.

## Stack Tecnologico

- **Tipo de repo**: Documentacion tecnica de APIs (no codigo)
- **Formato**: Markdown
- **Unico script**: `replace_tdm_words.py` (utilidad puntual de reemplazo de texto)
- **Servicios documentados**: API News, Twitter, Facebook, Instagram, YouTube, TikTok, Legal

## Estructura del Proyecto

```
feedscale_APIservicies/
├── README.md                              # Descripcion general (ES + ENG)
├── 00_Guia_Basica_Booleanos.md            # Guia de sintaxis booleana
├── 00_Guia_Creacion_Workers_y_Filtros_POST.md  # Guia de workers y filtros
├── API news Digital/                      # Docs API News Digital
├── API NewsPapper PrintMedia/             # Docs API Print Media
├── API Twitter/                           # Docs API Twitter
├── API facebook/                          # Docs API Facebook
├── API instagram/                         # Docs API Instagram
├── API youtube/                           # Docs API YouTube
├── API TikTok/                            # Docs API TikTok
├── API legal/                             # Docs API Legal
├── APIs FeedScale GeriAI/                 # Docs APIs con GeriAI
├── replace_tdm_words.py                   # Script utilidad
└── docs/
    ├── guides/
    │   └── DEVELOPER_HANDBOOK.md          # Este archivo
    ├── project/
    └── archive/
```

## Convenciones del Proyecto

- Cada API tiene su propia carpeta con documentacion independiente
- Las guias transversales (booleanos, workers) van en la raiz
- El README.md es bilingue (ES + ENG) porque es documentacion orientada a clientes internacionales

## Modelo IA Recomendado

- **Complejidad del repo**: Baja — documentacion en Markdown de specs de API, sin codigo ejecutable relevante
- **Modelo de inicio recomendado**: Sonnet
- **Cuando escalar a Opus**: No aplica en condiciones normales. Solo si se necesita redisenar la estructura completa de documentacion o crear nuevas specs de API desde cero analizando el backend real
- **Lenguaje principal**: Markdown (documentacion)

## Documentacion Relacionada

- Wiki: `wiki/docs/feedscale_workers_keywords_syntax.md` — sintaxis de keywords por API
- FeedScale Console: repo `feedscale_console_app`
- GeriAI Workers: repo `geriai_feedscale_workers`
