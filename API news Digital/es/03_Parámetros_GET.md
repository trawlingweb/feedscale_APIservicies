# API NEWS & BLOGS - Parámetros GET

### Introducción

En esta sección, se presenta una guía detallada sobre cómo construir y ejecutar consultas utilizando la API News & Blogs de TrawlingWeb. Esta API permite a los usuarios acceder a una amplia base de datos de información indexada, filtrando y recuperando información específica mediante el uso de parámetros GET.

A continuación, se explican los métodos estándar para realizar consultas, desglosando cada componente de la URL de ejemplo. También se proporciona una tabla con una descripción exhaustiva de cada parámetro, su uso, valores predeterminados y ejemplos prácticos. Esta información es esencial para los desarrolladores y usuarios que buscan maximizar la eficiencia y precisión de sus consultas a la API.

## Métodos Standard

Veamos la estructura de la consulta de ejemplo:

```
https://api.trawlingweb.com/?token={APIKEY}&q="messi"%20AND%20"Barcelona"&ts=1518472804000&size=100
```

## Aquí podemos identificar:

| Elemento   | Descripción                             |
| :--------- | :-------------------------------------- |
| protocolo  | Puede ser tanto **http** como **https** |
| dominio    | Dirección de la API api.trawlingweb.com |
| parámetros | Parámetros de la consulta               |

## Elementos que especifican la información que se desea y la forma en que se quiere recibir:

| Parámetro | Descripción                                                                                                                                                                                                                                                                                 | Default                                                 | Ejemplo                      |
| :-------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :------------------------------------------------------ | :--------------------------- |
| token     | APIKEY de acceso del cliente al sistema de TrawlingWeb.                                                                                                                                                                                                                                     | Valor obligatorio                                       | ?token={APIKEY}              |
| country_pref| Preferencia de país del cliente (ISO 3166-1 alpha-2, ej: `es`). **Obligatorio para contratos FeedScale Pay-per-Use**. Su omisión penaliza multiplicando x2.5 el coste de la request y conlleva riesgo de bloqueo de acceso.                                                              | Obligatorio (Pay-per-Use)                               | &country_pref=es             |
| q         | Expresión construida con filtros y expresiones clave de búsqueda. Permite sintaxis Lucene con búsqueda exacta entre comillas dobles ("") y operadores booleanos (AND, OR, NOT). [Consulta la Guía Básica de Operadores Booleanos](../../00_Guia_Basica_Booleanos.md) para más detalles y ejemplos. | Por defecto devuelve todas las publicaciones            | &q="domain=lavanguardia.com" |
| ts        | Se trata del delimitador temporal inicial. Formato Unix Time en milisegundos                                                                                                                                                                                                                | Delimita a 3 meses en el pasado a partir de la petición | &ts=1518472804000            |
| tsi       | Se trata del delimitador temporal final. Formato Unix Time en milisegundos                                                                                                                                                                                                                  | Delimita con la fecha de petición                       | &tsi=1524818189854           |
| size      | Cantidad de documentos que se desea recuperar por página. TrawlingWeb fracciona la entrega de datos en bloques de un máximo de 100 documentos. Cada bloque constituye una consulta efectiva. Así este parámetro permite configurar el tamaño de los bloques fijando su valor entre 1 y 100. | 100                                                     | &size=40                     |
| format    | Fija el formato de los archivos de respuesta. Los formatos disponibles són JSON y XML.                                                                                                                                                                                                      | json                                                    | &format=json                 |
| sort      | Orden con el qual se desea recibir los datos de las publicaciones. Estas se puden recibir ordenadas o bien por fecha de publicación (published) o bien por fecha de indexación (crawled).                                                                                                      | crawled                                                 | &sort=published              |
| order     | El orden puede ser _asc_ (ascendente) o _desc_ (descendente).                                                                                                                                                                                                                               | asc                                                     | &order=desc                  |

---

# Contacto

Si tienes alguna pregunta, necesitas asistencia, contratar o ampliar tus servicios por favor contacta con nosotros.

**SAT (Soporte Técnico):**

- [Correo SAT](mailto:support@trawlingweb.com)
- [Documentación Oficial](https://docs.trawlingweb.com)

**SAC (Soporte administrativo):**

- [Correo SAC](mailto:gestion@trawlingweb.com)

**Sales (Soporte ventas):**

- [Correo Ventas](mailto:sales@trawlingweb.com)
