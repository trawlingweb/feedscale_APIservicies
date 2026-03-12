# API TWITTER - Mejores Prácticas y Consejos

Para utilizar la API de Twitter, es necesario llamar a una URL de punto final con tu token de acceso privado. Puedes generar la URL de tu llamada en nuestro Testeador Visual de la API, accesible en [https://dashboard.trawlingweb.com/playground](https://dashboard.trawlingweb.com/playground).

## Ejemplo de Llamada

La llamada a la API se construye a partir de la estructura básica:

```
http://twitter.trawlingweb.com/010101010101010101?token=0000000000000000000000000000&q=casa
```

Esta estructura incluye:
* **Subdominio del API de Twitter**: `http://twitter.trawlingweb.com/`
* **IDworker**: `010101010101010101`ejemplo numerico de una ID de worker necesario para el uso de palabras clave de recuperación almacenadas dentro de un worker y credas anteriormente.
* **Token de Acceso (API key)**: `token=0000000000000000000000000000` para validar el uso.
* **Consulta (Q)**: `q=casa` para ejecutar la consulta (que en este caso busca resultados que contengan la palabra casa).

Esta es la estructura mínima para acceder al API de Twitter, pero a partir de aquí pueden utilizarse los parámetros disponibles en esta documentación para precisar y optimizar las consultas según las necesidades del usuario.

## Ejemplo de Salida

A continuación se muestra un ejemplo de salida de una llamada a la API. Esta salida incluye información sobre los resultados restantes, el número total de resultados y la URL para obtener los siguientes resultados.

```
requestLeft 9999999
totalResults 295404987
restResults 295404887
next "http://twitter.trawlingweb.com/010101010101010101?token=0000000000000000000000000000
```


## Uso de las Fechas `published` y `crawled`

TrawlingWeb entrega dos fechas para cada tweet: `published` (fecha de creación) y `crawled` (fecha de captura). Esto es crucial ya que, al incorporar nuevas secciones, el sistema puede detectar como nuevos tweets que fueron publicados días o incluso meses atrás.

También puede suceder que Twitter modifique su sistema, lo que puede provocar la aparición de tweets antiguos debido a errores o estrategias de SEO. Para evitar o controlar estos sucesos, aconsejamos que los clientes implementen reglas de seguridad en sus sistemas.

### Consejos sobre reglas para garantizar el buen uso de las fechas:

* **Filtros de Fecha**: Establecer filtros para ignorar tweets con fechas de creación muy antiguas.
* **Reglas de Relevancia**: Crear criterios que determinen la relevancia de los tweets en función de su fecha de creación y la fecha de procesamiento.
* **Monitoreo de Cambios**: Supervisar los cambios en el sistema de Twitter para ajustar las reglas de indexación y procesamiento en consecuencia.
* **Alertas y Notificaciones**: Configurar alertas para detectar y notificar la aparición de tweets antiguos, permitiendo una revisión manual si es necesario.

Implementar estas medidas ayuda a nuestros clientes a mantener la integridad y relevancia de los datos procesados por TrawlingWeb.

## Paginación

Cada solicitud a la API de Twitter puede devolver un máximo de 500 tweets coincidentes con su consulta. Sin embargo, pueden haber muchos más resultados que coincidan con tus parámetros de filtro. Para consumir todos los datos debes seguir realizando llamadas a la URL indicada en el parámetro **next** de la salida de cada solicitud.

Dependiendo del criterio de clasificación y del orden deseado para los resultados, la URL "next" incluye los valores `&ts` y `&tsi`, los cuales se ajustan según la forma en que se ordenan los resultados. Tanto `&ts` como `&tsi` son marcas de tiempo (UnixMicrotime).

Por defecto, la API de Twitter devuelve 500 resultados por solicitud, aunque el total de tweets coincidentes pueda ser mayor. En la respuesta JSON aparecerá el parámetro `next`, que sirve para realizar una llamada adicional a la API y obtener la siguiente página de resultados. Este proceso se repite hasta que se consumen todos los resultados disponibles.

Además, es posible modificar la cantidad de resultados que se desea obtener por solicitud. Si necesitas recibir menos de 500 resultados por llamada a la API, puedes ajustar este número utilizando el parámetro `size=n`.

## Modos de Paginación

Casos y ejemplos de modos de funcionamiento de la paginación.

#### Caso 1: 
`&sort=published&order=asc` _(Modo por defecto que puede entregar hasta un máximo de 500 resultados)_

`ejemplo: https://twitter.trawlingweb.com/01010101010101010?token=0000000000000000000&q=obama&sort=published&order=asc&ts=1719784800000&tsi=1720130400000`

Explicación: 
* **Organización**: Los tweets se organizan por fecha de creación ***(sort=published)***
* **Ordenación**: Los tweets se ordenan de viejos a nuevos ***(order=asc)***.
* **Resultados**: Sin definir el `size=n`, el máximo siempre será 500.
* **Next**: El "next" dentro del JSON permite saltar a los siguientes resultados, que como máximo serán 500.

#### Caso 2: 
`&sort=published&order=desc` _(Modo por defecto que puede entregar hasta un máximo de 500 resultados)_

`ejemplo: https://twitter.trawlingweb.com/01010101010101010?token=0000000000000000000&q=obama&sort=published&order=desc&ts=1719784800000&tsi=1720130400000`

Explicación: 
* **Organización**: Los tweets se organizan por fecha de creación ***(sort=published)***
* **Ordenación**: Los tweets se ordenan de nuevos a viejos ***(order=desc)***.
* **Resultados**: Sin definir el `size=n`, el máximo siempre será 500.
* **Next**: El "next" dentro del JSON permite saltar a los siguientes resultados, que como máximo serán 500.

#### Caso 3: 
`&sort=published&order=desc&size=4` _(Modo por defecto que puede entregar hasta un máximo de 500 resultados)_

`ejemplo: https://twitter.trawlingweb.com/01010101010101010?token=0000000000000000000&q=obama&sort=published&order=desc&ts=1719784800000&tsi=1720130400000&size=4`

Explicación: 
* **Organización**: Los tweets se organizan por fecha de creación ***(sort=published)***
* **Ordenación**: Los tweets se ordenan de nuevos a viejos ***(order=desc)***.
* **Resultados**: Definiendo el `size=4`, el máximo siempre será 4 en cada paginación.
* **Next**: El "next" dentro del JSON permite saltar a los siguientes resultados, que como máximo serán los definidos en el `size=n`, que en este caso al ser `size=4` serán 4 resultados.

## Agrupación

El parámetro de agrupación se usa con la siguiente sintaxis: `sort=`. Este permite agrupar los tweets por dos tipos de criterios temporales:

- **published**: Agrupa por fecha de creación. La fecha que se usará en la llamada al API es la fecha en la que se creó el tweet. `sort=published`
- **Crawled**: Agrupa por fecha de captura. La fecha que se usará en la llamada al API es la fecha en la que se capturó el tweet. `sort=crawled`

### Ejemplo 1: Agrupar por fecha de creación

`ejemplo: https://twitter.trawlingweb.com/01010101010101010?token=0000000000000000000&q=obama&sort=published&order=desc&ts=1719784800000&tsi=1720130400000&size=4`

Explicación: 
* **Organización**: Los tweets se organizan por fecha de creación ***(sort=published)***
* **Ordenación**: Los tweets se ordenan de nuevos a viejos ***(order=desc)***.
* **Resultados**: Definiendo el `size=4`, el máximo siempre será 4 en cada paginación.
* **Next**: El "next" dentro del JSON permite saltar a los siguientes resultados, que como máximo serán los definidos en el `size=n`, que en este caso al ser `size=4` serán 4 resultados.

### Ejemplo 2: Agrupar por fecha de procesamiento

`ejemplo: https://twitter.trawlingweb.com/01010101010101010?token=0000000000000000000&q=obama&sort=crawled&order=desc&ts=1719784800000&tsi=1720130400000&size=4`

Explicación: 
* **Organización**: Los tweets se organizan por fecha de captura ***(sort=crawled)***
* **Ordenación**: Los tweets se ordenan de nuevos a viejos ***(order=desc)***.
* **Resultados**: Definiendo el `size=4`, el máximo siempre será 4 en cada paginación.
* **Next**: El "next" dentro del JSON permite saltar a los siguientes resultados, que como máximo serán los definidos en el `size=n`, que en este caso al ser `size=4` serán 4 resultados.

#### Tips: 
* Si queremos obtener resultados agrupados por fecha de creación, usaremos `sort=published`, y si queremos obtener resultados agrupados por fecha de captura, usaremos `sort=crawled`.
- Si no utilizamos el parámetro `sort=`, por defecto la agrupación será `published`.

## Ordenación

El parámetro de ordenación se usa con la siguiente sintaxis: `order=`. Este permite ordenar el criterio de agrupación de forma ascendente o descendente:

* **order=asc**: Ordena de forma ascendente la agrupación `sort`.
* **order=desc**: Ordena de forma descendente la agrupación `sort`.

### Ejemplos:

* Si queremos obtener resultados agrupados por fecha de creación en orden ascendente, usaremos `sort=published&order=asc`.
* Si queremos obtener resultados agrupados por fecha de creación en orden descendente, usaremos `sort=published&order=desc`.

## Número de Resultados

Como se mencionó en la sección anterior "Paginación," cada llamada a esta API devuelve por defecto un máximo de 500 resultados. Sin embargo, como se demostró en los ejemplos de paginación, este número máximo de resultados devueltos puede ajustarse según las necesidades de uso para las llamadas.

Para modificar el número máximo de resultados que devuelve la llamada a la API, utilice el parámetro `size=`.

## Ejemplos:
* No uso de `size=`: Devolverá como máximo 500 resultados si están disponibles.
* `size=1`: Devolverá solo un resultado en cada paginación, independientemente de si hay más resultados disponibles.
* `size=20`: Devolverá un máximo de 20 resultados en cada paginación, independientemente de si hay más resultados disponibles.

## Mantenimiento Periódico de Fuentes de Datos

El mantenimiento periódico de las fuentes de datos es constante y esencial en TrawlingWeb. Implica una reevaluación integral de cada fuente, lo que a menudo conlleva la incorporación de nuevas secciones para indexar contenido no recopilado anteriormente. Contar con las fechas de creación (`published`) y de captura (`crawled`) permite gestionar estas actualizaciones de manera eficiente.

Al agregar nuevas fuentes de datos a nuestra cobertura, frecuentemente incluimos su historial realizando una indexación inicial profunda de todas sus secciones. Nuevamente, las fechas de creación (`published`) y de captura (`crawled`) facilitan este proceso.

Ciertas secciones de Twitter, además del contenido cronológico, pueden mostrar contenido no cronológico (como tweets destacados o relacionados) que también indexamos.

### Consideraciones

* **Frecuencia de Indexación**: La frecuencia de indexación de una fuente de datos se determina por las necesidades del cliente, los requisitos funcionales, la cantidad de tweets y la frecuencia de publicación de la fuente.
* **Diferenciación de Fechas**: Diferenciar claramente la fecha de captura (`crawled`) de la fecha de creación (`published`) permite que los clientes decidan qué tweets incorporar.
* **Filosofía de Entrega de Contenido**: Nuestra filosofía es entregar todos los tweets procesados, dejando la decisión sobre cómo utilizar este contenido a los clientes.

### Tweets Entregados y Descartados

- **Tweets Entregados**: Todos los tweets procesados se entregan al cliente.
- **Tweets Descartados**: Los clientes tienen la opción de descartar tweets según sus criterios y necesidades específicas.

## Sintaxis de Consultas de Lucene

Las APIs de TrawlingWeb permiten realizar consultas que pueden contener operadores booleanos basados en la sintaxis de Lucene, ofreciendo una poderosa herramienta para realizar búsquedas complejas y precisas. La sintaxis de consultas de Lucene está diseñada para ser intuitiva y expresiva.

En la sección 03_consultas encontrarás cómo usar adecuadamente expresiones booleanas y la sintaxis de Lucene.

---

# Contacto
Si tienes alguna pregunta, necesitas asistencia, contratar o ampliar tus servicios, por favor contacta con nosotros.

**SAT (Soporte Técnico):**
* [Correo SAT](mailto:support@trawlingweb.com)
* [Documentación Oficial](https://docs.trawlingweb.com)

**SAC (Soporte Administrativo):**
* [Correo SAC](mailto:gestion@trawlingweb.com)

**Sales (Soporte Ventas):**
* [Correo Ventas](mailto:sales@trawlingweb.com)
