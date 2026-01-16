# API Twitter - Método POST /create

Permite crear nuevos Workers con sus palabras.

# ¿Qué es un Worker?

Un Worker en TrawlingWeb es una entidad configurada por el usuario para realizar búsquedas específicas en redes sociales utilizando Palabras Clave. Estas Palabras Clave son términos de búsqueda configurados dentro del Worker y se basan en los créditos contratados (1 crédito = 1 Palabra Clave).

## Creación y Configuración de Workers

El usuario puede crear y definir los términos de búsqueda para cada Worker directamente en el dashboard ([https://dashboard.trawlingweb.com/workers](https://dashboard.trawlingweb.com/workers)) o utilizando el método proporcionado por la API. Una vez creado un Worker, este comienza su despliegue para iniciar su labor de configuración, que puede tardar hasta una hora.

## Funcionalidad de los Workers

- **Palabras clave**: Los Workers funcionan como una lista de palabras clave. Usan las Palabras Clave configuradas para realizar búsquedas en redes sociales.
- **Proceso de búsqueda**: Los Workers entregan las palabras clave a las arañas de TrawlingWeb para que ejecuten sus búsquedas en la red social.
- **Proceso de entrega**: Cada vez que el cliente llama al Worker, este utiliza la lista de palabras clave para lanzar la búsqueda contra la base de datos de resultados obtenidos por TrawlingWeb y recuperar solo aquellos resultados que tienen relación con la lista de palabras clave.

Implementar y gestionar Workers de manera eficiente permite a los usuarios maximizar la relevancia y precisión de los datos capturados, adaptándose a las necesidades específicas de sus análisis y monitoreo en redes sociales.

# Parámetros POST

Veamos la estructura de la consulta de ejemplo:

```
https://twitter.trawlingweb.com/create/?token={APIKEY}
```

## Parámetros PATH:

| Elemento  | Descripción                                 |
| :-------- | :------------------------------------------ |
| protocolo | Puede ser tanto **http** como **https**     |
| dominio   | Dirección de la API twitter.trawlingweb.com |
| metodo    | create                                      |

## Parámetros QUERY:

| Parámetro | Descripción                                             | Default           | Ejemplo         |
| :-------- | :------------------------------------------------------ | :---------------- | :-------------- |
| token     | APIKEY de acceso del cliente al sistema de TrawlingWeb. | Valor obligatorio | ?token={APIKEY} |

## Parámetros BODY:

| Parámetro   | Descripción                            | Default           | Límites                                                   |
| :---------- | :------------------------------------- | :---------------- | :-------------------------------------------------------- |
| description | Descripción que ha de tener el Worker. | Valor obligatorio | Cadena no superior a 200 carácteres                       |
| words       | Palabras de búsqueda.                  | Valor obligatorio | El número de parablas no ha de superar el límite acordado |

### Estructura del parámetro words

El parámetro `words` debe enviarse como un **array JSON** de cadenas de texto, donde cada elemento del array representa una Palabra Clave. Cada Palabra Clave puede contener sintaxis avanzada de Twitter (hashtags, menciones, operadores booleanos, filtros, etc.).

**Recomendación importante para búsquedas con `from:`**: Cuando necesites buscar tweets de múltiples cuentas, puedes encadenar hasta un máximo de 10 cuentas usando el operador OR dentro de una misma expresión. Esto permite optimizar el uso de créditos al agrupar múltiples cuentas en una sola Palabra Clave.

### Ejemplo de body en formato JSON:

```json
{
  "description": "Worker de ejemplo para monitoreo de marcas",
  "words": [
    "from:cocacola OR from:pepsi OR from:trawlingweb",
    "cocacola",
    "#pepsi",
    "cocacola lang:fr",
    "itau geocode:-25.2867,-57.647,250km OR ueno geocode:-25.2867,-57.647,250km OR basa geocode:-25.2867,-57.647,250km"
  ]
}
```

En este ejemplo, el Worker se crea con 5 Palabras Clave:

1. Una búsqueda compleja con múltiples cuentas usando el operador OR (máximo 10 cuentas por expresión)
2. Una palabra simple: "cocacola"
3. Un hashtag: "#pepsi"
4. Una palabra con filtro de idioma: "cocacola lang:fr"
5. Una búsqueda geográfica encadenada con múltiples términos usando geocode y OR

Cada elemento del array `words` consume 1 crédito (1 crédito = 1 Palabra Clave).

# Respuesta de salida - RESPONSE

Una vez lanzada una petición al API de Twitter éste devolverá una respuesta estructurada de la siguiente forma:

## Status 200 - Datos de la retorno

| Campo  | Descripción                          |  Tipo  |
| ------ | ------------------------------------ | :----: |
| worker | Identificador del Worker creado.     | Cadena |
| msg    | Descripción indicando acción exitosa | Cadena |

## Ejemplo de respuesta en formato json:

```json
"response" : {
    "worker" : "...",
    "msg" : "..."
}
```

## Status 400 - Datos de la retorno

| Campo | Descripción           |  Tipo  |
| ----- | --------------------- | :----: |
| error | Descripción del error | Cadena |

## Ejemplo de respuesta en formato json:

```json
"response" : {
    "error" : "..."
}
```

# Mejores búsquedas con la sintaxy de Twitter

Twitter utiliza su propia sintaxis avanzada para ejecutar búsquedas específicas y detalladas dentro de su plataforma. Esta sintaxis permite filtrar resultados por palabras clave, hashtags, menciones, ubicaciones y fechas, entre otros parámetros. Además, al definir palabras clave para un Worker, es posible utilizar esta misma sintaxis para lanzar consultas precisas contra el buscador de Twitter. Esto maximiza la eficiencia y relevancia de los datos capturados por cada Worker, facilitando una monitorización y análisis más efectivos de las conversaciones en Twitter.

Aquí tienes un listado de los elementos que puedes combinar con tus palabras clave al crearlas dentro de un worker:

| Tipo                                             | Descripción                                                                                                                                                                               | Ejemplo keyword                     | Resultado                                                                                                                          |
| ------------------------------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| Hashtag                                          | Términos referenciados con la almohadilla #                                                                                                                                               | #pepsi                              | devolvera posts que contienen hashtag (#) pepsi                                                                                    |
| Arroba                                           | Usuarios referenciados con la arroba @                                                                                                                                                    | @cocacola                           | devolevra postsen los qeu se haetiquetado/mencionado (@) cocacola                                                                  |
| Cadena simple                                    | Palabra con términos alfanuméricos sin caracteres especiales                                                                                                                              | Studio54                            | devolverá post qeu contienen la palabra "Studio54"                                                                                 |
| Cadena complejas                                 | Palabras con términos alfanuméricos sin caracteres especiales separadas por espacios                                                                                                      | Cocoa Cola 2019                     | devolverá cualquier post que contenga alguna o todas estas las palabras del ejemplo                                                |
| Búsqueda exacta                                  | Palabras o frases específicas entre comillas                                                                                                                                              | "cocacola con hielo"                | devolverá posts que contienen exactamente la frase "cocacola con hielo"                                                            |
| Búsqueda con OR                                  | Palabras múltiples separadas por OR para ampliar resultados                                                                                                                               | Cocacola OR Pepsi                   | devolverá posts que contienen "Cocacola" o "Pepsi" (o ambos)                                                                       |
| Sin palabras (NOT)                               | Excluye palabras específicas de la búsqueda                                                                                                                                               | Cocacola -pepsi                     | devolverá posts que contienen "Cocacola" pero excluye aquellos que contienen "pepsi"                                               |
| Hashtag específico                               | Búsqueda de hashtags específicos                                                                                                                                                          | #openai                             | devolverá posts que contienen el hashtag (#) openai                                                                                |
| Desde una cuenta                                 | Búsqueda de tweets enviados por una cuenta específica. Se pueden encadenar hasta 10 cuentas con OR dentro de una misma expresión                                                          | from:cocacola                       | devolverá posts publicados por la cuenta @cocacola. Ejemplo con múltiples: `from:cuenta1 OR from:cuenta2 OR ... OR from:cuenta10`  |
| Desde una cuenta pero que habla de algo concreto | Búsqueda de tweets enviados por una cuenta específica. Cuando el emisor de la cuenta menciona la palabra. En este caso no se deben encadenar cuentas con OR dentro de una misma expresión | from:cocacola supermercados         | devolverá posts publicados por la cuenta @cocacola solamente cuando esta use la palabra "supermercados".                           |
| A una cuenta                                     | Búsqueda de tweets enviados a una cuenta específica                                                                                                                                       | to:pepsi                            | devolverá posts dirigidos a la cuenta @pepsi                                                                                       |
| Mención de cuenta                                | Búsqueda de tweets que mencionan una cuenta específica                                                                                                                                    | @cocacola                           | devolverá posts en los que se ha etiquetado/mencionado (@) cocacola                                                                |
| Geocodificación (Más preciso)                    | Búsqueda de tweets dentro de un radio específico usando coordenadas GPS exactas. Es el método más preciso para búsquedas geográficas                                                      | itau geocode:-25.2867,-57.647,250km | devolverá posts que contienen "itau" enviados dentro de un radio de 250km desde las coordenadas especificadas (Asunción, Paraguay) |
| Desde fecha                                      | Búsqueda de tweets enviados desde una fecha específica                                                                                                                                    | cocacola since:2022-02-17           | devolverá posts que contienen "cocacola" publicados desde el 17 de febrero de 2022                                                 |
| Hasta fecha                                      | Búsqueda de tweets enviados hasta una fecha específica                                                                                                                                    | pepsi until:2022-02-17              | devolverá posts que contienen "pepsi" publicados hasta el 17 de febrero de 2022                                                    |
| Pregunta                                         | Búsqueda de tweets que contienen preguntas                                                                                                                                                | pepsi ?                             | devolverá posts que contienen "pepsi" y que son preguntas                                                                          |
| Con enlaces                                      | Búsqueda de tweets que contienen enlaces                                                                                                                                                  | cocacola filter:links               | devolverá posts que contienen "cocacola" y que incluyen enlaces                                                                    |
| Fuente específica                                | Búsqueda de tweets publicados desde una fuente específica                                                                                                                                 | pepsi source:twitterfeed            | devolverá posts que contienen "pepsi" publicados desde la fuente twitterfeed                                                       |
| palabra con idioma específico                    | Búsqueda de tweets publicados en un idioma específico. Ha de ser en ISO Alpha II                                                                                                          | pepsi lang:fr                       | devolverá posts que contienen "pepsi" publicados en francés (ISO Alpha II: fr)                                                     |

### Notas importantes sobre búsquedas geográficas

**Geocodificación (`geocode:`)**: X (Twitter) no admite el comando `country:` ni una sintaxis directa por código de país (como `country:es`). El método más preciso para filtrar resultados por ubicación geográfica es usar `geocode:` con coordenadas GPS exactas.

**Sintaxis de geocode:**

- Formato: `geocode:latitud,longitud,radio`
- Ejemplo: `itau geocode:-25.2867,-57.647,250km` busca menciones de "itau" dentro de un radio de 250km desde Asunción, Paraguay.
- Las coordenadas deben estar en formato decimal (latitud,longitud).
- El radio puede especificarse en kilómetros (`km`) o millas (`mi`).

**Encadenar múltiples búsquedas con OR:**
Puedes combinar múltiples términos de búsqueda con geocodificación usando el operador OR dentro de una misma Palabra Clave. Esto permite optimizar el uso de créditos al agrupar búsquedas relacionadas en una sola Palabra Clave:

```json
{
  "description": "Worker para búsqueda geográfica de múltiples términos en Paraguay",
  "words": [
    "itau geocode:-25.2867,-57.647,250km OR ueno geocode:-25.2867,-57.647,250km OR basa geocode:-25.2867,-57.647,250km"
  ]
}
```

Este ejemplo busca menciones de "itau", "ueno" o "basa" dentro de un radio de 250km desde Asunción, Paraguay, utilizando solo 1 crédito.

**Comparación de métodos geográficos:**

- `geocode:` - Más preciso, requiere coordenadas GPS exactas. Recomendado para búsquedas profesionales.
- `near:` + `within:` - Menos preciso, funciona con nombres de ciudades pero puede ser menos exacto.
- `lang:` - Filtra por idioma del tweet, no por ubicación física. Útil cuando el objetivo es filtrar por idioma en lugar de ubicación.

**Nota importante**: Los filtros geográficos solo funcionan con tweets de usuarios que tienen activada la ubicación en sus publicaciones o en su perfil de forma pública.

### Tabla de coordenadas de capitales para búsquedas geográficas

A continuación se presenta una tabla con las coordenadas GPS de las principales capitales de Latinoamérica y Europa, junto con ejemplos de búsqueda usando `geocode:` y el radio recomendado para abarcar la mayor parte del territorio de cada país:

#### Capitales de Latinoamérica

| País                 | Capital             | Coordenadas (lat,lon) | Radio recomendado | Ejemplo de búsqueda                     |
| :------------------- | :------------------ | :-------------------- | :---------------- | :-------------------------------------- |
| Argentina            | Buenos Aires        | -34.6037,-58.3816     | 800km             | `casa geocode:-34.6037,-58.3816,800km`  |
| Bolivia              | La Paz              | -16.5000,-68.1500     | 600km             | `casa geocode:-16.5000,-68.1500,600km`  |
| Brasil               | Brasilia            | -15.7942,-47.8822     | 1200km            | `casa geocode:-15.7942,-47.8822,1200km` |
| Chile                | Santiago            | -33.4489,-70.6693     | 800km             | `casa geocode:-33.4489,-70.6693,800km`  |
| Colombia             | Bogotá              | 4.7110,-74.0721       | 600km             | `casa geocode:4.7110,-74.0721,600km`    |
| Costa Rica           | San José            | 9.9281,-84.0907       | 200km             | `casa geocode:9.9281,-84.0907,200km`    |
| Cuba                 | La Habana           | 23.1136,-82.3666      | 400km             | `casa geocode:23.1136,-82.3666,400km`   |
| Ecuador              | Quito               | -0.1807,-78.4678      | 300km             | `casa geocode:-0.1807,-78.4678,300km`   |
| El Salvador          | San Salvador        | 13.6929,-89.2182      | 150km             | `casa geocode:13.6929,-89.2182,150km`   |
| Guatemala            | Ciudad de Guatemala | 14.6349,-90.5069      | 250km             | `casa geocode:14.6349,-90.5069,250km`   |
| Honduras             | Tegucigalpa         | 14.0723,-87.1921      | 250km             | `casa geocode:14.0723,-87.1921,250km`   |
| México               | Ciudad de México    | 19.4326,-99.1332      | 800km             | `casa geocode:19.4326,-99.1332,800km`   |
| Nicaragua            | Managua             | 12.1364,-86.2514      | 300km             | `casa geocode:12.1364,-86.2514,300km`   |
| Panamá               | Ciudad de Panamá    | 8.9824,-79.5199       | 200km             | `casa geocode:8.9824,-79.5199,200km`    |
| Paraguay             | Asunción            | -25.2867,-57.647      | 250km             | `casa geocode:-25.2867,-57.647,250km`   |
| Perú                 | Lima                | -12.0464,-77.0428     | 600km             | `casa geocode:-12.0464,-77.0428,600km`  |
| República Dominicana | Santo Domingo       | 18.4861,-69.9312      | 300km             | `casa geocode:18.4861,-69.9312,300km`   |
| Uruguay              | Montevideo          | -34.9011,-56.1645     | 300km             | `casa geocode:-34.9011,-56.1645,300km`  |
| Venezuela            | Caracas             | 10.4806,-66.9036      | 500km             | `casa geocode:10.4806,-66.9036,500km`   |

#### Capitales de Europa

| País            | Capital    | Coordenadas (lat,lon) | Radio recomendado | Ejemplo de búsqueda                  |
| :-------------- | :--------- | :-------------------- | :---------------- | :----------------------------------- |
| Alemania        | Berlín     | 52.5200,13.4050       | 500km             | `casa geocode:52.5200,13.4050,500km` |
| Austria         | Viena      | 48.2082,16.3738       | 300km             | `casa geocode:48.2082,16.3738,300km` |
| Bélgica         | Bruselas   | 50.8503,4.3517        | 150km             | `casa geocode:50.8503,4.3517,150km`  |
| Dinamarca       | Copenhague | 55.6761,12.5683       | 300km             | `casa geocode:55.6761,12.5683,300km` |
| España          | Madrid     | 40.4168,-3.7038       | 500km             | `casa geocode:40.4168,-3.7038,500km` |
| Finlandia       | Helsinki   | 60.1699,24.9384       | 400km             | `casa geocode:60.1699,24.9384,400km` |
| Francia         | París      | 48.8566,2.3522        | 500km             | `casa geocode:48.8566,2.3522,500km`  |
| Grecia          | Atenas     | 37.9838,23.7275       | 300km             | `casa geocode:37.9838,23.7275,300km` |
| Hungría         | Budapest   | 47.4979,19.0402       | 250km             | `casa geocode:47.4979,19.0402,250km` |
| Irlanda         | Dublín     | 53.3498,-6.2603       | 200km             | `casa geocode:53.3498,-6.2603,200km` |
| Italia          | Roma       | 41.9028,12.4964       | 500km             | `casa geocode:41.9028,12.4964,500km` |
| Noruega         | Oslo       | 59.9139,10.7522       | 500km             | `casa geocode:59.9139,10.7522,500km` |
| Países Bajos    | Ámsterdam  | 52.3676,4.9041        | 200km             | `casa geocode:52.3676,4.9041,200km`  |
| Polonia         | Varsovia   | 52.2297,21.0122       | 400km             | `casa geocode:52.2297,21.0122,400km` |
| Portugal        | Lisboa     | 38.7223,-9.1393       | 300km             | `casa geocode:38.7223,-9.1393,300km` |
| Reino Unido     | Londres    | 51.5074,-0.1278       | 400km             | `casa geocode:51.5074,-0.1278,400km` |
| República Checa | Praga      | 50.0755,14.4378       | 300km             | `casa geocode:50.0755,14.4378,300km` |
| Rumanía         | Bucarest   | 44.4268,26.1025       | 400km             | `casa geocode:44.4268,26.1025,400km` |
| Suecia          | Estocolmo  | 59.3293,18.0686       | 600km             | `casa geocode:59.3293,18.0686,600km` |
| Suiza           | Berna      | 46.9481,7.4474        | 200km             | `casa geocode:46.9481,7.4474,200km`  |

**Nota**: Los radios recomendados están calculados para abarcar la mayor parte del territorio de cada país. Puedes ajustar el radio según tus necesidades específicas de búsqueda.

## Caracteres reservados en palabras de búsqueda

> Los caracteres reservados son: + - = & | > < ! ¡ () {} [] ^ " ~ \* ¿ ?: \ / ' -

# Contacto

Si tienes alguna pregunta, necesitas asistencia, contratar o ampliar tus servicios por favor contacta con nosotros.

**SAT (Soporte Técnico):**

- [Correo SAT](mailto:support@trawlingweb.com)
- [Documentación Oficial](https://docs.trawlingweb.com)

**SAC (Soporte administrativo):**

- [Correo SAC](mailto:gestion@trawlingweb.com)

**Sales (Soporte ventas):**

- [Correo Ventas](mailto:sales@trawlingweb.com)
