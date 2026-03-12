# API FeedScale - Método GET /posts

Este método permite obtener resultados indexados de posts de FeedScale desde BigQuery. Se pueden usar delimitadores temporales para acotar el contenido devuelto.

## Parámetros GET

La llamada a la API se construye a partir de la estructura básica:

```
https://feedscale.trawlingweb.com/posts?token={APIKEY}
```

### Parámetros QUERY

| Parámetro | Descripción | Default | Ejemplo |
| :-------- | :---------- | :------ | :------ |
| token | APIKEY para validar y acceder al sistema. Cada usuario tiene su propia APIKEY individual e intransferible. | Valor obligatorio | `?token=1234` |
| ts | Delimitador temporal inicial (tiempo pasado). Formato Unix Time en milisegundos. Los resultados se ordenan del pasado al presente (ASC). | Delimita a 1 mes en el pasado a partir de la petición | `&ts=1518472804000` |
| tsi | Delimitador temporal final (tiempo presente). Formato Unix Time en milisegundos. | Delimita con la fecha de petición | `&tsi=1524818189854` |
| size | Número de resultados por página | 500 (máximo: 500) | `&size=100` |

**Nota**: También se acepta `apiKey` como alternativa a `token`, y `TS`/`TSI` en mayúsculas para compatibilidad.

---

## Paginación

Cada solicitud a la API puede devolver un máximo de **500 posts** coincidentes con su consulta. Sin embargo, pueden haber muchos más resultados que coincidan con tus parámetros de filtro. Para consumir todos los datos debes seguir realizando llamadas a la URL indicada en el parámetro **next** de la salida de cada solicitud.

**Orden de resultados**: Los resultados se ordenan en orden ascendente (ASC), del pasado (`ts`) al presente (`tsi`). Los posts más antiguos aparecen primero, y los más recientes al final de cada página.

### Ejemplo de Salida con Paginación

```json
{
  "response": {
    "data": [...],
    "totalResults": 7940,
    "restResults": 7435,
    "next": "https://feedscale.trawlingweb.com/posts?token=1234&ts=1766312910631&tsi=1768866612000&size=500"
  }
}
```

### Campos de Paginación

| Campo | Descripción |
| ----- | ----------- |
| totalResults | Número total de resultados que coinciden con la consulta |
| restResults | Número de resultados restantes por consumir |
| next | URL para obtener la siguiente página de resultados. `null` cuando no hay más resultados |

### Modificar Número de Resultados por Página

Por defecto, la API devuelve 500 resultados por solicitud. Si necesitas recibir menos resultados por llamada, puedes ajustar este número utilizando el parámetro `size=n`.

**Ejemplos:**
- `size=100` - Devolverá 100 resultados por página
- `size=50` - Devolverá 50 resultados por página
- Sin `size` - Devolverá 500 resultados (máximo)

---

## Ejemplos de Llamadas

### Consulta Básica (Último mes, 500 resultados por página)

```
https://feedscale.trawlingweb.com/posts?token=1234
```

### Con Límite de Resultados

```
https://feedscale.trawlingweb.com/posts?token=1234&size=100
```

### Últimas 24 Horas con Paginación

```
https://feedscale.trawlingweb.com/posts?token=1234&ts=1768818277820&tsi=1768904677820&size=100
```

---

## Cómo Calcular Timestamps

Los timestamps deben estar en **Unix Time en milisegundos**.

### JavaScript

```javascript
const ahora = Date.now();

// Últimas 24 horas
const hace24Horas = ahora - (24 * 60 * 60 * 1000);

// Últimos 7 días
const hace7Dias = ahora - (7 * 24 * 60 * 60 * 1000);

// Último mes (30 días)
const hace30Dias = ahora - (30 * 24 * 60 * 60 * 1000);

// URL de ejemplo con paginación
const url = `https://feedscale.trawlingweb.com/posts?token=1234&ts=${hace24Horas}&tsi=${ahora}&size=100`;
```

### Python

```python
import time

ahora = int(time.time() * 1000)  # milisegundos
hace24horas = ahora - (24 * 60 * 60 * 1000)

url = f"https://feedscale.trawlingweb.com/posts?token=1234&ts={hace24horas}&tsi={ahora}&size=100"
```

### Tabla de Conversión

| Período | Milisegundos |
|---------|--------------|
| 1 hora | 3,600,000 |
| 24 horas | 86,400,000 |
| 7 días | 604,800,000 |
| 30 días | 2,592,000,000 |

---

## Consumir Todos los Resultados (Ejemplo)

### JavaScript

```javascript
async function consumirTodosLosResultados(urlInicial) {
  let url = urlInicial;
  let todosLosResultados = [];

  while (url) {
    const response = await fetch(url);
    const data = await response.json();
    
    todosLosResultados = todosLosResultados.concat(data.response.data);
    console.log(`Obtenidos: ${todosLosResultados.length} / ${data.response.totalResults}`);
    
    url = data.response.next; // Siguiente página o null si terminó
  }

  console.log(`Total obtenido: ${todosLosResultados.length}`);
  return todosLosResultados;
}

// Uso
const url = 'https://feedscale.trawlingweb.com/posts?token=1234&size=500';
consumirTodosLosResultados(url);
```

### Python

```python
import requests

def consumir_todos_los_resultados(url_inicial):
    url = url_inicial
    todos_los_resultados = []

    while url:
        response = requests.get(url)
        data = response.json()
        
        todos_los_resultados.extend(data['response']['data'])
        print(f"Obtenidos: {len(todos_los_resultados)} / {data['response']['totalResults']}")
        
        url = data['response']['next']  # Siguiente página o None si terminó

    print(f"Total obtenido: {len(todos_los_resultados)}")
    return todos_los_resultados

# Uso
url = 'https://feedscale.trawlingweb.com/posts?token=1234&size=500'
resultados = consumir_todos_los_resultados(url)
```

---

## Respuesta de Salida - RESPONSE

### Estructura de la Respuesta

```json
{
  "response": {
    "data": [
      {
        "id": 123,
        "c_noticia": 456,
        "published": "2025-12-21 10:00:00",
        "autor": "Usuario",
        "marca": "Ueno",
        "origen": "twitter",
        "audiencia": 1000,
        "likes": 50,
        "retweet": 10,
        "comentarios": 5,
        "text": "Texto del post...",
        "url": "https://x.com/usuario/status/123",
        "tono": "Positivo"
      }
    ],
    "totalResults": 7940,
    "restResults": 7440,
    "next": "https://feedscale.trawlingweb.com/posts?token=1234&ts=...&tsi=...&size=500"
  }
}
```

### Datos de la Publicación

| Campo | Descripción | Tipo |
| ----- | ----------- | ---- |
| id | Código de identificación asignado a cada publicación | Entero |
| c_noticia | Código de la noticia | Entero |
| published | Fecha publicado el post (formato: YYYY-MM-DD HH:mm:ss) | Cadena |
| autor | Nombre del autor | Cadena |
| marca | Marca relacionada | Cadena |
| origen | Origen del post (twitter, instagram, facebook, etc.) | Cadena |
| audiencia | Audiencia estimada | Entero |
| likes | Número de likes | Entero |
| retweet | Número de retweets | Entero |
| comentarios | Número de comentarios | Entero |
| reproducciones | Número de reproducciones | Entero |
| interacciones | Total de interacciones | Entero |
| sentimiento | Valor de sentimiento | Entero |
| tono | Tono del mensaje (Positivo, Negativo, Neutro) | Cadena |
| lang | Idioma detectado | Cadena |
| title | Título del post | Cadena |
| url | URL de la publicación | Cadena |
| text | Texto del post | Cadena |

---

## Códigos de Estado HTTP

| Código | Descripción |
| ------ | ----------- |
| 200 | ¡Éxito! |
| 400 | Error de sintaxis o parámetros inválidos |
| 401 | Usuario no autorizado o sin token |
| 403 | API Key inválida o no autorizada |
| 500 | No se pudo ejecutar la consulta |

---

## Health Check

Para verificar que el servidor está funcionando:

```
https://feedscale.trawlingweb.com/health
```

Respuesta:
```json
{
  "status": "ok",
  "timestamp": "2026-01-20T10:00:00.000Z",
  "service": "FeedScale API"
}
```

---

## Ejemplos con cURL

```bash
# Básico (500 resultados)
curl "https://feedscale.trawlingweb.com/posts?token=1234"

# Con límite de 100 resultados por página
curl "https://feedscale.trawlingweb.com/posts?token=1234&size=100"

# Últimas 24 horas con paginación
AHORA=$(date +%s)000
HACE24H=$((AHORA - 86400000))
curl "https://feedscale.trawlingweb.com/posts?token=1234&ts=${HACE24H}&tsi=${AHORA}&size=100"
```
