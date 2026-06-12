# API Reddit - Método GET /workers

Permite obtener los Workers configurados por el usuario y los datos de los mismos.

# Parámetros GET

Veamos la estructura de la consulta de ejemplo:

```
https://reddit.trawlingweb.com/workers/?token={APIKEY}
```

## Parámetros PATH:

| Elemento  | Descripción                                  |
| :-------- | :------------------------------------------- |
| protocolo | Puede ser tanto **http** como **https**      |
| dominio   | Dirección de la API reddit.trawlingweb.com   |
| metodo    | workers                                      |

## Parámetros QUERY:

| Parámetro | Descripción                                             | Default           | Ejemplo         |
| :-------- | :------------------------------------------------------ | :---------------- | :-------------- |
| token     | APIKEY de acceso del cliente al sistema de TrawlingWeb. | Valor obligatorio | ?token={APIKEY} |

# Respuesta de salida - RESPONSE

Una vez lanzada una petición a la API de Reddit ésta devolverá una respuesta estructurada de la siguiente forma:

## Datos de cada Worker

| Campo       | Descripción                                              | Buscable | Ordenable |  Tipo  |   Formato    |
| ----------- | -------------------------------------------------------- | :------: | :-------: | :----: | :----------: |
| id          | Código de identificación del Worker                      |    No    |    No     | Cadena |              |
| type        | Tipo de Worker (reddit)                                  |    No    |    No     | Cadena |              |
| subtype     | Subtipo (si aplica)                                       |    No    |    No     | Cadena |              |
| description | Descripción establecida por el usuario                   |    No    |    No     | Cadena |              |
| words       | Palabras de búsqueda (array)                             |    No    |    No     | Array  |              |
| created_at  | Fecha de creación del Worker                             |    No    |    No     | Fecha  | ISO 8601-UTC |
| status      | Estatus de actividad del Worker ( 1 running , 0 stopped )|    No    |    No     | Entero |              |

## Datos generales

| Campo       | Descripción                   | Buscable | Ordenable |  Tipo  | Formato |
| ----------- | ----------------------------- | :------: | :-------: | :----: | :-----: |
| workersLeft | Número de Workers disponibles |    No    |    No     | Entero |         |
| limit       | Número de Workers máximos     |    No    |    No     | Entero |         |

## Ejemplo de respuesta en formato json:

```json
"response" : {
    "workers" : [{
            "id" : "...",
            "type" : "reddit",
            "subtype" : "...",
            "description" : "...",
            "words" : ["cocacola", "u/cocacola"],
            "created_at" : "...",
            "status" : 1
    }],
    "workersLeft" : "...",
    "limit" : "..."
}
```
