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
├── API Telegram/
├── API Reddit/
├── API news Digital/
├── API NewsPapper PrintMedia/
├── API legal/
├── APIs FeedScale GeriAI/
├── CHANGELOG.md
├── changelogs/                          ← fragmentos individuales
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
- **Campos de usuario `user_name` / `user_screen_name`**: `user_screen_name` es el handle (`@handle`, identificador único) y `user_name` el nombre visible. En Reddit ambos llevan el handle porque la plataforma no expone display name. Documentarlo igual en todas las APIs.

### Cambios en sintaxis de keywords

Cuando se cambie la sintaxis de keywords de una API:

1. Actualizar la documentación de esa API en este repo.
2. Actualizar `wiki/docs/feedscale_workers_keywords_syntax.md` (canónico).
3. Actualizar `validateWordsForApi()` en `feedscale_console_app`.
4. Avisar a Toti — algunas APIs (Twitter query-only, p.ej.) requieren config manual en las arañas.

> **Nota (desde 2026-06-22)**: un worker con sintaxis Lucene inválida **ya no bloquea** los endpoints `/counts`, `/posts/:worker_id` y `/count/:worker_id` en las 6 APIs sociales. El error se aísla por iteración, se reporta a Mochi y queda en `logs/bad_workers.log`. Sigue bloqueando en `getResultsSearch` (`/posts/?q=`) y en `/create`. Al documentar límites de sintaxis, no prometer que una keyword mala "tumba la API": ya no es cierto para esos tres endpoints. Detalle en `wiki/AI_CODE_INSTRUCTIONS.md` §11 (FeedScale Workers Keywords).

### Coordinación cross-repo (obligatorio desde 2026-08-18)

Un cambio de sintaxis o de contrato de una API toca **tres repos** (este, `wiki`, `feedscale_console_app`) y normalmente más de un dev. En ese caso el gameplan **no vive solo en el repo**: se abre una **Issue de coordinación en `trawlingweb/wiki`** y se enlaza el gameplan por URL raw. El **assignee indica quién debe actuar** — cada dev revisa lo suyo con `gh issue list --assignee @me`, y responder obliga a reasignar en el mismo paso. Protocolo completo: `wiki/AI_CODE_INSTRUCTIONS.md` §32. Requiere `gh auth refresh -s project` una vez por dev.

---

## Despliegue

**Este repo no se despliega a ninguna VM.** El "deploy" es el propio push a GitHub: el contenido se sirve como documentación pública desde el repositorio.

### Git Flow (obligatorio)

- Trabajar siempre en branch `vN` para cambios significativos (nueva API, refactor de carpeta, cambio de sintaxis).
- Cambios triviales (typos, formato) pueden ir directo a `main`.
- Merge a main con `--no-ff` cuando esté validado.
- **NUNCA borrar branches mergeadas** — se conservan como histórico y safety net de rollback.
- Consultar `git branch -r` para determinar el siguiente `vN`.
- Protocolo completo: `wiki/AI_CODE_INSTRUCTIONS.md` §9.6.

### Encadenamiento con la wiki tras commit/deploy (obligatorio)

Tras un commit significativo o un push a `main`, **sin preguntar**: fragmento en `changelogs/` de este repo, entrada en `CHANGELOG.md`, fragmento en `wiki/changelogs/` con identificador de autor (`claude-oscar`, `cursor-xavi`…), actualización de `wiki/docs/feedscale_apiservicies.md` si cambió el alcance, y `node scripts/consolidar_fragmentos.js` desde el repo de wiki. Detalle: `wiki/AI_CODE_INSTRUCTIONS.md` §9.3.

### Prerequisitos de deploy — acceso a las VMs de Google

> Fuente canónica: `wiki/docs/acceso_vms_google_gcloud.md`. Aquí solo lo que hace falta saber.

Este repo no despliega a VM, pero **sus consumidores sí** (`feedscale_console_app` y las 6 APIs sociales corren en `mochi-vm` / `crawlers-vm`). Un cambio de sintaxis documentado aquí suele arrastrar un deploy allí, y ese deploy falla por dos motivos que se confunden constantemente:

**1. Credencial: usa tu service account nominal, NUNCA tu cuenta personal.**

```bash
gcloud auth activate-service-account --key-file=~/.ssh/<nombre>-dev.json
gcloud config set project dataagencies
gcloud auth list   # el * debe estar en <nombre>-dev@…gserviceaccount.com
```

Las cuentas `@trawlingweb.app` caducan por una política de sesión (~16 h) que impone la organización **anpro21.com** — no el Admin console de trawlingweb.com, que dice "nunca reautenticar" y no es la autoridad aquí. En modo no interactivo (Claude Code, scripts, CI) mueren con `Reauthentication failed. cannot prompt during non-interactive execution`. Las service accounts están exentas. Si no tienes la tuya, pídesela a Oscar — **no** pidas prestada la de otro.

**2. `--tunnel-through-iap` es obligatorio y explícito** en todo `gcloud compute ssh` / `scp`. El puerto 22 de ambas VMs está cerrado a internet, y gcloud solo autodetecta IAP cuando la VM no tiene IP externa — las dos la tienen (Caddy). Sin el flag: `FATAL ERROR: Network error: Connection timed out`.

Diagnóstico por mensaje de error — no improvises:

| Error | Causa | Qué hacer |
|---|---|---|
| `Connection timed out` | Falta `--tunnel-through-iap` | Añadir el flag y reintentar |
| `Reauthentication required` / `failed` | Cuenta personal caducada | No reintentar en bucle: activar la SA nominal |
| `PERMISSION_DENIED … getAccessToken` | Falta `serviceAccountTokenCreator` | Grant de admin: pedirlo |
| `Could not add SSH key to instance metadata` | Falta `actAs` sobre la SA de la VM | Grant de admin |

**Prohibiciones absolutas**:

- NUNCA copiar, mover ni compartir un `*.json` de service account (ni `dashai-infra.json`). Si un dev no puede desplegar, **se le crea su propia SA**.
- NUNCA escribir claves ni tokens en `wiki/docs/` — esa carpeta la indexa el bot de Telegram y la reenvía al canal. Secretos de infraestructura → `wiki/MAQUINAS.md`.
- `--impersonate-service-account` sirve en interactivo, pero **no elimina la reauth**: no vale para deploys automatizados.
- Tailscale just-in-time (§28) **no aplica** a estas VMs: GCP se accede por túnel IAP, no por el tailnet corporativo.

---

## Tareas y Kanban

Las tareas de este repo se registran en el Kanban de SAT Console (`satKanbanTasks`, campo `repo = feedscale_APIservicies`). La IA consulta las tareas del repo al arrancar sesión, crea en estado `todo` las `- [ ]` detectadas en `docs/project/ROADMAP.md` y mantiene ROADMAP y Kanban como espejo. Asignado por defecto: el `git config user.email` del repo. Detalle: `wiki/AI_CODE_INSTRUCTIONS.md` §23.

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
- Ficha del repo en la wiki: `wiki/docs/feedscale_apiservicies.md`.
- Acceso a VMs de Google: `wiki/docs/acceso_vms_google_gcloud.md`.
- Validador en consola: `feedscale_console_app/src/routes/consumers.js` (`validateWordsForApi`).
- Playground tips: `feedscale_console_app/public/js/playground.js`.
- CLAUDE.md (raíz) — contexto del proyecto para IA.
- ROADMAP: `docs/project/ROADMAP.md`.
- Seguridad: `docs/shell/SECURITY_PROTOCOL.md`.
- CHANGELOG: `CHANGELOG.md`.

<!-- AI_CODE_INSTRUCTIONS-sync: 2026-08-18 -->

---

<!-- TW-NORMAS:BEGIN (gestionado por trawlingweb/wiki) -->
## Normas Trawlingweb (bloque gestionado)

> Este bloque lo mantiene `scripts/actualizar_handbooks.py` del repo `trawlingweb/wiki` y se
> sincroniza a todos los `DEVELOPER_HANDBOOK.md` de la organización. **No lo edites aquí**:
> cambia `docs/plantillas/handbook_normas_trawlingweb.md` en la wiki.

- **Fuente de verdad**: [`AI_CODE_INSTRUCTIONS.md`](https://github.com/trawlingweb/wiki/blob/main/AI_CODE_INSTRUCTIONS.md) de la wiki. Se trabaja siempre con un workspace que incluya el repo `wiki`.
- **Las Issues viven en `trawlingweb/wiki`** (una sola bandeja), no en este repo (§32). El assignee dice quién debe actuar y pasar la pelota es obligatorio (§32.5, §32.7).
- **Ninguna Issue sin Project y ningún Project sin repo enlazado (§32.14, innegociable)**. Antes de crear una Issue, elige o crea su Project (copia de la plantilla #8) y enlaza este repo con `gh project link <N> --owner trawlingweb --repo trawlingweb/<este-repo>`. Auditoría: `scripts/auditar_projects.sh` en la wiki.
- **Un Project = un gameplan** (§32.9). Al cerrar la Issue, mueve también su tarjeta a «Hecho» en el Project (§32.13).
- **Documentación obligatoria del repo** (§9): `README.md`, `CLAUDE.md`, `CHANGELOG.md` + `changelogs/` y este handbook. Los cambios de setup, infra o despliegue se anotan aquí.
- **Sin secretos en el repo**: los valores viven fuera (`.env` de la máquina, gestor de secretos); aquí solo el nombre de la variable.
<!-- TW-NORMAS:END -->
