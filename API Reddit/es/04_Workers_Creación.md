# API Reddit - Método POST /create

Permite crear nuevos Workers con sus palabras.

# ¿Qué es un Worker?

Un Worker en TrawlingWeb es una entidad configurada por el usuario para realizar búsquedas específicas sobre los posts y comentarios capturados de Reddit utilizando Palabras Clave. Estas Palabras Clave son términos de búsqueda configurados dentro del Worker y se basan en los créditos contratados (1 crédito = 1 Palabra Clave).

## Creación y Configuración de Workers

El usuario puede crear y definir los términos de búsqueda para cada Worker directamente en el dashboard ([https://dashboard.trawlingweb.com/workers](https://dashboard.trawlingweb.com/workers)) o utilizando el método proporcionado por la API. Una vez creado un Worker, este comienza a filtrar el flujo de posts y comentarios capturados según sus palabras clave (los resultados empiezan a estar disponibles de forma prácticamente inmediata).

## Funcionalidad de los Workers

* **Palabras clave**: Los Workers funcionan como una lista de palabras clave. Usan las Palabras Clave configuradas para filtrar el flujo de posts y comentarios capturados de Reddit.
* **Proceso de búsqueda**: Los Workers aplican las palabras clave sobre los campos `text`, `user_name`, `user_screen_name` y `subreddit` de cada elemento.
* **Proceso de entrega**: Cada vez que el cliente llama al Worker, este utiliza la lista de palabras clave para lanzar la búsqueda contra la base de datos de posts y comentarios capturados por TrawlingWeb y recuperar solo aquellos resultados que tienen relación con la lista de palabras clave (combinables con filtros booleanos vía `q=`).

Implementar y gestionar Workers de manera eficiente permite a los usuarios maximizar la relevancia y precisión de los datos procesados, adaptándose a las necesidades específicas de sus análisis y monitoreo en Reddit.


# Parámetros POST

Veamos la estructura de la consulta de ejemplo:

```
https://reddit.trawlingweb.com/create/?token={APIKEY}
```

## Parámetros PATH:

| Elemento  | Descripción                                  |
| :-------- | :------------------------------------------- |
| protocolo | Puede ser tanto **http** como **https**      |
| dominio   | Dirección de la API reddit.trawlingweb.com   |
| metodo    | create                                       |

## Parámetros QUERY:

| Parámetro | Descripción                                              | Default           | Ejemplo         |
| :-------- | :------------------------------------------------------- | :---------------- | :-------------- |
| token     | APIKEY de acceso del cliente al sistema de TrawlingWeb. | Valor obligatorio | ?token={APIKEY} |

## Parámetros BODY:

| Parámetro   | Descripción                            | Default           | Límites                                                   |
| :---------- | :------------------------------------- | :---------------- | :-------------------------------------------------------- |
| description | Descripción que ha de tener el Worker. | Valor obligatorio | Cadena no superior a 200 caracteres                       |
| words       | Palabras de búsqueda.                  | Valor obligatorio | El número de palabras no ha de superar el límite acordado |

### Estructura del parámetro words

El parámetro `words` debe enviarse como un **array JSON** de cadenas de texto, donde cada elemento del array representa una Palabra Clave. Cada Palabra Clave puede ser un término simple, una frase entre comillas o una mención (u/usuario).

### Ejemplo de body en formato JSON:

```json
{
    "description": "Worker de ejemplo para monitoreo de marca",
    "words": [
        "cocacola",
        "\"coca cola\"",
        "u/cocacola"
    ]
}
```

En este ejemplo, el Worker se crea con 3 Palabras Clave:
1. Un término simple: "cocacola"
2. Una frase exacta: "coca cola"
3. Una mención: "u/cocacola"

Cada elemento del array `words` consume 1 crédito (1 crédito = 1 Palabra Clave).

# Respuesta de salida - RESPONSE

Una vez lanzada una petición a la API de Reddit ésta devolverá una respuesta estructurada de la siguiente forma:

## Status 200 - Datos del retorno

| Campo  | Descripción                          |  Tipo  |
| ------ | ------------------------------------ | :----: |
| worker | Identificador del Worker creado.     | Cadena |
| msg    | Descripción indicando acción exitosa | Cadena |

## Ejemplo de respuesta en formato json:

```json
"response" : {
    "worker" : "...",
    "msg" : "created"
}
```

## Status 400 - Datos del retorno

| Campo | Descripción           |  Tipo  |
| ----- | --------------------- | :----: |
| error | Descripción del error | Cadena |

## Ejemplo de respuesta en formato json:

```json
"response" : {
    "error" : "..."
}
```

# Mejores búsquedas con la sintaxis de Reddit

Reddit es principalmente texto plano dentro de subreddits temáticos. La sintaxis efectiva para definir palabras clave se centra en términos exactos, frases entre comillas, menciones (u/usuario) y filtros por subreddit. Esta sintaxis permite filtrar resultados por términos, frases, autor, subreddit y rangos temporales. Al definir palabras clave para un Worker, esta sintaxis maximiza la eficiencia y relevancia de los datos procesados.

Aquí tienes un listado de los elementos que puedes combinar con tus palabras clave al crearlas dentro de un worker:

| Tipo              | Descripción                                                                          | Ejemplo keyword                | Resultado                                                                           |
| ----------------- | :----------------------------------------------------------------------------------- | :----------------------------- | ----------------------------------------------------------------------------------- |
| Término exacto    | Palabra simple sin signos especiales                                                  | cocacola                       | devolverá posts/comentarios que contienen la palabra **cocacola**                   |
| Frase exacta      | Frase de varias palabras encerrada entre comillas dobles                              | "coca cola"                    | devolverá posts/comentarios que contienen la frase exacta **coca cola**             |
| Mención (u/)      | Usuarios referenciados con u/                                                         | u/cocacola                     | devolverá posts/comentarios en los que se ha etiquetado o autor coincide con u/cocacola |

> Para filtrar por subreddit, usa `subreddit:nombre` dentro del parámetro `q=` en la llamada `/posts/`. Ver sección de sintaxis booleana.

## Caracteres reservados en palabras de búsqueda

> Los caracteres reservados son: + - = & | > < ! ¡ () {} [] ^ " ~ \* ¿ ?: \ / ' -

# Contacto
Si tienes alguna pregunta, necesitas asistencia, contratar o ampliar tus servicios por favor contacta con nosotros.

**SAT (Soporte Técnico):**
* [Correo SAT](mailto:support@trawlingweb.com)
* [Documentación Oficial](https://github.com/trawlingweb/APIservicies/tree/main/API%20Reddit)

**SAC (Soporte administrativo):**
* [Correo SAC](mailto:gestion@trawlingweb.com)

**Sales (Soporte ventas):**
* [Correo Ventas](mailto:sales@trawlingweb.com)
