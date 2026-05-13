# API PRINT MEDIA – Buenas prácticas y consejos

Para usar correctamente la API de **Print Media** (prensa escrita/medios impresos), sigue las recomendaciones que encontrarás a continuación. Empieza generando tu llamada en el Playground de prensa escrita:
[https://dashboard.trawlingweb.com/playground/press-written](https://dashboard.trawlingweb.com/playground/press-written)

---

## Ejemplo de llamada mínima

```text
https://api.trawlingweb.com/press-written?
   token=TU_TOKEN
 & q=casa
```

- **Endpoint**: `https://api.trawlingweb.com/press-written`
- **token**: tu clave privada de acceso
- **q**: consulta booleana o filtro Lucene (p.ej. `casa`)

Desde esta base puedes añadir cualquier otro parámetro (`from`, `to`, `site`, `sort`, `order`, `size`, `format`, …) para personalizar tu petición.

---

## Ejemplo de salida

Cada respuesta incluye metadatos de paginación:

```text
requestLeft    9999999
totalResults   295404987
restResults    295404887
next           "https://api.trawlingweb.com/press-written?token=TU_TOKEN&q=casa&ts=1517443760316&tsi=1524818189854"
```

- `requestLeft`: consultas restantes
- `totalResults`: total de artículos coincidentes
- `restResults`: resultados pendientes de entrega
- `next`: URL para la siguiente página de resultados

---

## Uso de las fechas `published` y `crawled`

Cada artículo incluye dos fechas:

- **published**: cuándo se publicó originalmente.
- **crawled**: cuándo TrawlingWeb lo indexó.

> **Atención**: al incorporar nuevas secciones o cambiar formatos, podrías “re-indexar” artículos antiguos. Para evitar ruido:
>
> - Filtra por rangos de `published` recientes (`from`/`to`).
> - Usa reglas de relevancia que comparen `published` vs `crawled`.
> - Configura alertas si detectas `published` muy antiguos.

---

## Paginación

La API entrega como máximo **100 resultados** por llamada. Cuando haya más, usa la URL en `next` para seguir paginando.

- Por defecto `size=100`.
- Para menos resultados: `size=n` (1 ≤ n ≤ 100).

Cada respuesta actualiza `next` con nuevos `ts` y `tsi` (timestamps en ms) para continuar desde el punto correcto.

---

## Modos de paginación

### Caso 1: Agrupar por indexación (default)

```
…?token=TU_TOKEN
 & q=obama
 & sort=crawled
 & order=asc
```

- Ordena por fecha de indexación (`crawled`), de más antiguo a más reciente.
- Máx. 100 resultados → usa `next` para continuar.

### Caso 2: Agrupar por publicación

```
…?token=TU_TOKEN
 & q=obama
 & sort=published
 & order=desc
```

- Ordena por fecha de publicación (`published`), de más reciente a más antiguo.

### Caso 3: Resultados reducidos

```
…?token=TU_TOKEN
 & q=obama
 & sort=published
 & order=desc
 & size=4
```

- Máx. 4 artículos por llamada.
- Para cada página, `next` respeta `size=4`.

---

## Reglas recomendadas

1. **Filtrar rangos de fecha**

   - Ignora `published` anteriores a X días.

2. **Detectar re-indexaciones**

   - Compara `crawled` vs `published` y descarta si la diferencia supera un umbral.

3. **Monitorear fuentes**

   - Ajusta filtros si un medio cambia su estructura o URLs.

4. **Alertas**

   - Notifica re-indexaciones masivas para revisión manual.

---

## Mantenimiento de fuentes

- Revisamos y expandimos periódicamente las secciones de cada medio.
- Al añadir un medio, indexamos históricamente todas sus páginas (usamos `crawled` vs `published`).
- Indexamos también contenido no cronológico (rankings, relacionados).

---

## Filosofía de entrega

TrawlingWeb siempre entrega **todas** las noticias indexadas. Queda en manos del cliente:

- **Descartar** lo irrelevante con sus propios filtros.
- **Procesar** según sus reglas de negocio.

---

# Contacto

Para dudas, soporte o ampliación de plan:

- **Soporte Técnico (SAT):** [support@trawlingweb.com](mailto:support@trawlingweb.com)
- **Soporte Administrativo (SAC):** [gestion@trawlingweb.com](mailto:gestion@trawlingweb.com)
- **Ventas (Sales):** [marketing@trawlingweb.com](mailto:marketing@trawlingweb.com)
