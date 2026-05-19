# CLAUDE.md — feedscale_APIservicies

## Descripción

Repositorio de **documentación** de las APIs de FeedScale. No contiene código ejecutable. Es la referencia técnica de los endpoints y sintaxis de keywords por red social.

## Contenido

Guías por API:
- `API Twitter/` — sintaxis booleana, endpoints, límites
- `API instagram/` — endpoints y parámetros
- `API facebook/` — endpoints y parámetros
- `API TikTok/` — endpoints y parámetros
- `API youtube/` — endpoints y parámetros
- `API news Digital/` — APIs de noticias digitales
- `API NewsPapper PrintMedia/` — prensa impresa
- `API legal/` — APIs legales
- `APIs FeedScale GeriAI/` — integración con GeriAI

## Referencia cruzada

- Sintaxis de keywords: `wiki/docs/feedscale_workers_keywords_syntax.md`
- Validación en código: `feedscale_console_app/src/routes/consumers.js` → `validateWordsForApi()`

---

## Estándares Trawlingweb

Este repo sigue los estándares globales documentados en `wiki/AI_CODE_INSTRUCTIONS.md`. Trabajar siempre con un workspace que incluya el repo `wiki`.

**Al cerrar sesión o tras un deploy significativo**, preguntar al usuario:
1. ¿Hay cambios estructurales que actualizar en este `CLAUDE.md`? (nueva arquitectura, nueva convención, nuevo módulo clave)
2. ¿Hay decisiones o aprendizajes de la sesión que guardar en memoria?
