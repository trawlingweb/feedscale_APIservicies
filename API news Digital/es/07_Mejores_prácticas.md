# API NEWS & BLOGS - Mejores prácticas y consejos

Con el fin de utilizar la API es necesario llamar a una URL de punto final con su token de acceso privado. Puede generar la URL de su llamada en nuestro Testeador visual de la API (que debe acceder a https://dashboard.trawlingweb.com/playground).


## Ejemplo de Llamada

La llamada a la API se construye a partir de la estructura básica:

```
http://api.trawlingweb.com/?token=0000000000000000000000000000&q=casa
```

Esta estructura incluye:
* **Subdominio del API de News & Blogs**: `http://api.trawlingweb.com/`
* **Token de Acceso (API key)**: `token=0000000000000000000000000000` para validar el uso.
* **Consulta (Q)**: `q=casa` para ejecutar la consulta (que en este caso busca resultados que contengan la palabra casa).

Esta es la estructura mínima para acceder al API de News & Blogs, pero a partir de aquí pueden utilizarse los parámetros disponibles en esta documentación para precisar y optimizar las consultas según las necesidades del usuario.


## Ejemplo de Salida

A continuación se muestra un ejemplo de salida de una llamada a la API. Esta salida incluye información sobre los resultados restantes, el número total de resultados y la URL para obtener los siguientes resultados.

```
requestLeft	9999999
totalResults	295404987
restResults	295404887
next	"http://api.trawlingweb.com/?token=0000000000000000000000000000&q=casa&ts=1517443760316&tsi=1524818189854"

```

## Uso de las Fechas `published` y `crawled`

Trawlingweb entrega dos fechas para cada noticia: `published` (fecha de publicación) y `crawled` (fecha de indexación). Esto es crucial ya que, al incorporar nuevas secciones, el sistema puede detectar como nuevas noticias que fueron publicadas días o incluso meses atrás.

También puede suceder que los medios modifiquen sus sistemas de publicación, lo que puede provocar la aparición de noticias antiguas debido a errores o estrategias de SEO. 
Para evitar o controlar estos sucesos, aconsejamos que los clientes implementen reglas de seguridad en sus sistemas.

### Consejos sobre reglas par garantizar el buen uso de las fechas:

* **Filtros de Fecha**: Establecer filtros para ignorar noticias con fechas de publicación muy antiguas.
* **Reglas de Relevancia**: Crear criterios que determinen la relevancia de las noticias en función de su fecha de publicación y la fecha de indexación.
* **Monitoreo de Cambios**: Supervisar los cambios en los sistemas de publicación de los medios para ajustar las reglas de indexación y procesamiento en consecuencia.
* **Alertas y Notificaciones**: Configurar alertas para detectar y notificar la aparición de noticias antiguas, permitiendo una revisión manual si es necesario.

Implementar estas medidas ayuda a nuestros clientes a mantener la integridad y relevancia de los datos indexados por TrawlingWeb.


## Paginación

Cada solicitud al API News & Blogs puede devolver un máximo de 100 mensajes coincidentes con su consulta. Sin embargo, pueden haber muchos más resultados que coincidan con sus parámetros de filtro. Para consumir todos los datos ha de seguir realizando llamadas a la URL indicada en el parámetro **next** de las salida de cada solicitud.

Dependiendo del criterio de clasificación y del orden deseado para los resultados, la URL "next" incluye los valores &ts y &tsi, los cuales se ajustan según la forma en que se ordenan los resultados. Tanto &ts como &tsi son marcas de tiempo (UnixMicrotime).

Por defecto, la API de noticias y blogs devuelve 100 resultados por solicitud, aunque el total de noticias coincidentes pueda ser mayor (por ejemplo, 300 resultados). En la respuesta JSON aparecerá el parámetro next, que sirve para realizar una llamada adicional a la API y obtener la siguiente página de resultados. Este proceso se repite hasta que se consumen todos los resultados disponibles.

Además, es posible modificar la cantidad de resultados que se desea obtener por solicitud. Si necesita recibir menos de 100 resultados por llamada a la API, puede ajustar este número utilizando el parámetro size=n.

## Modos de paginación

Casos y ejemplos de modos de funcionamiento de la paginación.

#### Caso 1: 
&sort=**crawled** &order=**asc** _(Modo por defecto que puede entregar hasta un máximo de 100 resulatdos)_

exemple: 
```
https://api.trawlingweb.com/?token=0000000000000000000&q=obama&sort=crawled&order=desc&ts=1719784800000&tsi=1720130400000
```

Explicación: 
* **Búsqueda**: Busca noticias que contengan en el texto la palabra "obama" ***(q=obama)***
* **Agrupación**: Las noticias se organizan por fecha de indexación ***(sort=crawled)***
* **Ordenación**: Las noticias se ordenan de viejas a nuevas ***(order=asc)***.
* **Resultados**: Sin definir el size=n el máximo siempre será 100.
* **Next**: El "next" dentro dle JSON permite saltar a los siguientes resulatdos, que como máximo seran 100.

#### Caso 2: 
&sort=**published** &order=**desc** _(Modo por defecto que puede entregar hasta un máximo de 100 resulatdos)_

exemple:
```
https://api.trawlingweb.com/?token=0000000000000000000&q=obama&sort=published&order=desc&ts=1719784800000&tsi=1720130400000
```

Explicación: 
* **Búsqueda**: Busca noticias que contengan en el texto la palabra "obama" ***(q=obama)***
* **Agrupación**: Las noticias se organizan por fecha de publicación ***(sort=published)***
* **Ordenación**: Las noticias se ordenan de nuevas a más antiguas ***(order=desc)***.
* **Resultados**: Sin definir el size=n el máximo siempre será 100.
* **Next**: El "next" dentro del JSON permite saltar a los siguientes resulatdos, que como máximo seran 100.

#### Caso 3: 
&sort=**published** &order=**desc** &size=**4** _(Modo por defecto que puede entregar hasta un máximo de 100 resulatdos)_

exemple: 
```
https://api.trawlingweb.com/?token=0000000000000000000&q=obama&sort=published&order=desc&ts=1719784800000&tsi=1720130400000&size=4
```

Explicación: 
* **Búsqueda**: Busca noticias que contengan en el texto la palabra "obama" ***(q=obama)***
* **Agrupación**: Las noticias se organizan por fecha de publicación ***(sort=published)***
* **Ordenación**: Las noticias se ordenan de nuevas a más antiguas ***(order=desc)***.
* **Resultados**: Definido el size=4 el máximo siempre será 4 en cada paginación.
* **Next**: El "next" dentro dle JSON permite saltar a los siguientes resultados, que como máximo seran los definidos en el size=n que en este caso al ser size=4 seran 4 resultados.

## Búsqueda (`q=`)
Revisa las secciones 04_Parámetro_de_filtrado y 05_Sintaxis_para_consultas para manejar correctamente `q=`.

## Agrupación (`sort=`)

El parámetro de agrupación se usa con la siguiente sintaxis: `sort=`. Este permite agrupar las noticias por dos tipos de criterios temporales:

- **Crawled**: Agrupa por fecha de indexación. La fecha que se usará en la llamada al API es la fecha en la que se indexó la noticia o el post. `sort=crawled`
- **Published**: Agrupa por fecha de publicación. La fecha que se usará en la llamada al API es la fecha en la que se publicó la noticia o el post y fue definida por quien la publicó originalmente. `sort=published`

### Ejemplo 1: Agrupar por fecha de indexación

exemple:
```
https://api.trawlingweb.com/?token=0000000000000000000&q=obama&sort=crawled&order=desc&ts=1719784800000&tsi=1720130400000&size=4
```

Explicación: 
* **Búsqueda**: Busca noticias que contengan en el texto la palabra "obama" ***(q=obama)***
* **Agrupación**: Las noticias se organizan por fecha de indexación ***(sort=crawled)***
* **Ordenación**: Las noticias se ordenan de nuevas a más antiguas ***(order=desc)***.
* **Resultados**: Definido el size=4 el máximo siempre será 4 en cada paginación.
* **Next**: El "next" dentro dle JSON permite saltar a los siguientes resulatdos, que como máximo seran los definidos en el size=n que en este caso al ser size=4 seran 4 resulatdos.

### Ejemplo 2: Agrupar por fecha de publicación

exemple:
```
https://api.trawlingweb.com/?token=0000000000000000000&q=obama&sort=published&order=desc&ts=1719784800000&tsi=1720130400000&size=4
```

Explicación: 
* **Búsqueda**: Busca noticias que contengan en el texto la palabra "obama" ***(q=obama)***
* **Agrupación**: Las noticias se organizan por fecha de publicación ***(sort=published)***
* **Ordenación**: Las noticias se ordenan de nuevas a más antiguas ***(order=desc)***.
* **Resultados**: Definido el size=4 el máximo siempre será 4 en cada paginación.
* **Next**: El "next" dentro dle JSON permite saltar a los siguientes resulatdos, que como máximo seran los definidos en el size=n que en este caso al ser size=4 seran 4 resulatdos.

#### Tips: 
* Si queremos obtener resultados agrupados por fecha de indexación, usaremos `sort=crawled`, y si queremos obtener resultados agrupados por fecha de publicación, usaremos `sort=published`.
* Si no utilizamos el parametro `sort=` por defecto la agrupación será `crawled`.

## Ordenación (`order=`)

El parámetro de ordenación se usa con la siguiente sintaxis: `order=`. Este permite ordenar el criterio de agrupación de forma ascendente o descendente:

* **order=asc**: Ordena de forma ***ascendente*** la agrupacion `sort`.
* **order=desc**: Ordena de forma ***descendente*** la agrupacion `sort`.

### Ejemplos:

* Si queremos obtener resultados agrupados por fecha de indexación en orden ascendente, usaremos `sort=crawled&order=asc`.
* Si queremos obtener resultados agrupados por fecha de publicación en orden descendente, usaremos `sort=published&order=desc`.

## Número de Resultados (`size=`)
Como se mencionó en la sección anterior "Paginación," cada llamada a esta API devuelve por defecto un máximo de 100 resultados. Sin embargo, como se demostró en los ejemplos de paginación, este número máximo de resultados devueltos puede ajustarse según las necesidades de uso para las llamadas.

Para modificar el número máximo de resultados que devuelve la llamada a la API, utilice el parámetro `size=`.

## Ejemplos:
* No uso de `size=`: Devolverá como máximo 100 resultados si están disponibles.
* `size=1`: Devolverá solo un resultado en cada paginación, independientemente de si hay más resultados disponibles.
* `size=20`: Devolverá un máximo de 20 resultados en cada paginación, independientemente de si hay más resultados disponibles.

## Mantenimiento Periódico de Fuentes de Medios

El mantenimiento periódico de las fuentes de medios es constante y core en TrawlingWeb e implica una reevaluación integral de cada fuente, lo que a menudo conlleva la incorporación de nuevas secciones para indexar contenido no procesado anteriormente. Contar con las fechas de indexación (`crawled`) y publicación (`published`) permite gestionar estas actualizaciones de manera eficiente.

Al agregar nuevas fuentes de medios a nuestra cobertura, frecuentemente incluimos su historial realizando una indexación inicial profunda de todas sus secciones. Nuevamente, las fechas de indexación (`crawled`) y publicación (`published`) facilitan este proceso.

Ciertas secciones de los medios, además del contenido cronológico, muestran contenido no cronológico (como rankings o noticias relacionadas) que también indexamos.

### Consideraciones

* **Frecuencia de Indexación**: La frecuencia de indexación de una fuente de medios se determina por las necesidades del cliente, los requisitos funcionales, la cantidad de noticias y la frecuencia de publicación del medio.
* **Diferenciación de Fechas**: Diferenciar claramente la fecha de indexación (`crawled`) de la fecha de publicación (`published`) permite que los clientes decidan qué noticias incorporar.
* **Filosofía de Entrega de Información**: Nuestra filosofía es entregar todas las noticias indexadas, dejando la decisión sobre cómo utilizar esta información a los clientes.

### Noticias Entregadas y Descartadas

* **Noticias Entregadas**: Todas las noticias indexadas se entregan al cliente.
* **Noticias Descartadas**: Los clientes tienen la opción de descartar noticias según sus criterios y necesidades específicas.

## Sintaxis de Consultas de Lucene

Las APIs de TrawlingWeb permiten realizar consultas que pueden contener operadores booleanos basados en la sintaxis de Lucene, ofreciendo una poderosa herramienta para realizar búsquedas complejas y precisas. La sintaxis de consultas de Lucene está diseñada para ser intuitiva y expresiva.

En la sección 03_consultas encontrarás como usar adecudamente expresiones booleanas y la sintaxy de lucene.

---

# Contacto
Si tienes alguna pregunta, necesitas asistencia, contratar o ampliar tus servicios por favor contacta con nosotros.

**SAT (Soporte Técnico):**
* [Correo SAT](mailto:support@trawlingweb.com)
* [Documentación Oficial](https://docs.trawlingweb.com)

**SAC (Soporte administrativo):**
* [Correo SAC](mailto:gestion@trawlingweb.com)

**Sales (Soporte ventas):**
* [Correo Ventas](mailto:sales@trawlingweb.com)

