# API Reddit - Método GET /delete

Si un Worker ya no te sirve, puedes borrarlo y dejar espacio para crear uno nuevo.

# Parámetros GET

Veamos la estructura de la consulta de ejemplo:

```
https://reddit.trawlingweb.com/delete/xxxxxxxxxxxxx?token={APIKEY}
```

> Nota: el endpoint también admite el método HTTP **DELETE** con la misma estructura.

## Parámetros PATH:

| Elemento  | Descripción                                  |
| :-------- | :------------------------------------------- |
| protocolo | Puede ser tanto **http** como **https**      |
| dominio   | Dirección de la API reddit.trawlingweb.com   |
| método    | delete                                       |
| id        | identificador del Worker a borrar            |

## Parámetros QUERY:

| Parámetro | Descripción                                              | Default           | Ejemplo         |
| :-------- | :------------------------------------------------------- | :---------------- | :-------------- |
| token     | APIKEY de acceso del cliente al sistema de TrawlingWeb . | Valor obligatorio | ?token={APIKEY} |

# Respuesta de salida - RESPONSE

Una vez lanzada una petición a la API de Reddit ésta devolverá una respuesta estructurada de la siguiente forma:

## Status 200 - Datos del retorno

| Campo  | Descripción                          |  Tipo  |
| ------ | ------------------------------------ | :----: |
| worker | Identificador del Worker borrado.    | Cadena |
| msg    | Descripción indicando acción exitosa | Cadena |

## Ejemplo de respuesta en formato json:

```json
"response" : {
    "worker" : "...",
    "msg" : "deleted"
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

# Características de los Workers

Los datos capturados se almacenan en índices mensuales `reddit_YYYY_MM` con la retención acordada en el plan del cliente (típicamente los últimos meses consultables vía `ts`/`tsi`).

El usuario puede eliminar un Worker concreto. Esta eliminación implica la destrucción de la configuración del mismo. Los datos históricos asociados al Worker dejan de ser consultables a través de él una vez eliminado.

Al eliminar un Worker, el contador de Workers disponibles del consumer se incrementa de nuevo (siempre que no se supere el `counter_limit` del plan).
