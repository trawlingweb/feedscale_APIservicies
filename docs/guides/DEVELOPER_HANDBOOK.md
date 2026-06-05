# Developer Handbook — feedscale_APIservicies

Guía para mantener y extender la documentación oficial de las APIs de FeedScale.

---

## Descripción del Proyecto

Repositorio de **documentación pública** de las APIs de FeedScale (TrawlingWeb). No contiene código ejecutable: es la referencia técnica que consumen clientes, equipo Sales y la propia consola `feedscale_console_app` para mostrar tips, sintaxis de keywords y endpoints.

Su contenido se publica en GitHub como referencia abierta y se enlaza desde:

- `feedscale_console_app/public/js/playground.js` (tips y URL builder)
- `feedscale_console_app/src/routes/consumers.js` → `validateWordsForApi()` (sintaxis de keywords)
- `wiki/docs/feedscale_workers_keywords_syntax.md` (documento canónico de sintaxis)

---

## Stack Tecnológico

- **Formato**: Markdown puro — sin build, sin generadores estáticos.
- **Estructura**: una carpeta por API (`API Twitter/`, `API instagram/`, `API facebook/`…) con `README.md` dentro de cada una.
- **Recursos transversales**: guías de inicio en la raíz (`00_Guia_Basica_Booleanos.md`, `00_Guia_Creacion_Workers_y_Filtros_POST.md`).

---

## Setup Local

### Requisitos previos

- Git.
- Cualquier editor con preview de Markdown (VS Code recomendado).

### Instalación

```bash
git clone git@github.com:trawlingweb/feedscale_APIservicies.git
cd feedscale_APIservicies
```

No hay dependencias ni `npm install`.

### Variables de entorno

No aplica.

### VS Code — Settings recomendados (Windows)

```json
"terminal.integrated.enablePersistentSessions": true,
"terminal.integrated.persistentSessionReviveProcess": "onExitAndWindowClose",
"window.restoreWindows": "all"
```

---

## Arquitectura

```
feedscale_APIservicies/
├── 00_Guia_Basica_Booleanos.md         ← sintaxis booleana común a todas las APIs
├── 00_Guia_Creacion_Workers_y_Filtros_POST.md
├── API Twitter/                         ← una carpeta por red social / API
├── API instagram/
├── API facebook/
├── API TikTok/
├── API youtube/
├── API news Digital/
├── API NewsPapper PrintMedia/
├── API legal/
├── APIs FeedScale GeriAI/
├── CLAUDE.md
├── README.md                            ← landing público bilingüe ES/EN
└── docs/
    ├── archive/
    ├── guides/                          ← este handbook
    │   └── DEVELOPER_HANDBOOK.md
    ├── project/
    │   └── ROADMAP.md
    └── shell/
        └── SECURITY_PROTOCOL.md
```

---

## Convenciones del Proyecto

- **Una carpeta por API** con `README.md` dentro. Nunca mezclar varias APIs en un mismo documento.
- **Nombres con espacios** en las carpetas (`API Twitter/`) — convención histórica que respetan los enlaces del README. Si se renombrara, romperían los enlaces externos publicados a clientes.
- **Bilingüe ES/EN** en el `README.md` raíz. El resto de docs pueden ser solo ES si así estaban.
- **No hay landing page en la raíz de cada API** que no sea `README.md` — GitHub lo renderiza automáticamente al entrar a la carpeta.
- **Toda mención a sintaxis de keywords** debe coincidir con `validateWordsForApi()` en `feedscale_console_app/src/routes/consumers.js`. Si una difiere, se rompe la validación frontend o el cliente recibe error 400.

### Cambios en sintaxis de keywords

Cuando se cambie la sintaxis de keywords de una API:

1. Actualizar la documentación de esa API en este repo.
2. Actualizar `wiki/docs/feedscale_workers_keywords_syntax.md` (canónico).
3. Actualizar `validateWordsForApi()` en `feedscale_console_app`.
4. Avisar a Toti — algunas APIs (Twitter query-only, p.ej.) requieren config manual en las arañas.

---

## Despliegue

No aplica. El repo se "despliega" simplemente pusheando a GitHub, donde se sirve como documentación pública en la web.

### Git Flow (obligatorio)

- Trabajar siempre en branch `vN` para cambios significativos (nueva API, refactor de carpeta, cambio de sintaxis).
- Cambios triviales (typos, formato) pueden ir directo a `main`.
- Merge a main con `--no-ff` cuando esté validado.
- **NUNCA borrar branches mergeadas** — se conservan como histórico.
- Consultar `git branch -r` para determinar el siguiente `vN`.
- Protocolo completo: `wiki/AI_CODE_INSTRUCTIONS.md` §9.6.

---

## Modelo IA Recomendado

- **Complejidad del repo**: Baja (sólo Markdown, sin código).
- **Modelo de inicio recomendado**: Haiku.
- **Cuándo escalar a Sonnet**: redactar nueva API completa con ejemplos, traducciones ES→EN, o reescritura amplia de una guía.
- **Cuándo escalar a Opus**: no aplica — un cambio que justifique Opus aquí probablemente debería ir en `feedscale_console_app` o `wiki`.
- **Lenguaje principal**: Markdown.

---

## Documentación Relacionada

- Sintaxis canónica de keywords: `wiki/docs/feedscale_workers_keywords_syntax.md`.
- Validador en consola: `feedscale_console_app/src/routes/consumers.js` (`validateWordsForApi`).
- Playground tips: `feedscale_console_app/public/js/playground.js`.
- CLAUDE.md (raíz) — contexto del proyecto para IA.
- ROADMAP: `docs/project/ROADMAP.md`.
- Seguridad: `docs/shell/SECURITY_PROTOCOL.md`.
- CHANGELOG: `CHANGELOG.md`.
