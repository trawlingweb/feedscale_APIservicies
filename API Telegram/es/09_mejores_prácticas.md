# API Telegram - Mejores Prácticas y Consejos

Para utilizar la API de Telegram, es necesario llamar a una URL de punto final con tu token de acceso privado. Puedes generar la URL de tu llamada en nuestro Testeador Visual de la API, accesible en [https://dashboard.trawlingweb.com/playground](https://dashboard.trawlingweb.com/playground).

## Ejemplo de Llamada

La llamada a la API se construye a partir de la estructura básica:

```
https://telegram.trawlingweb.com/posts/010101010101010101?token=0000000000000000000000000000&q=crisis
```

Esta estructura incluye:
* **Subdominio del API de Telegram**: `https://telegram.trawlingweb.com/`
* **Método**: `posts/`
* **IDworker**: `010101010101010101` (ejemplo numérico de una ID de worker necesaria para el uso de palabras clave de recuperación almacenadas dentro de un worker y creadas anteriormente).
* **Token de Acceso (API key)**: `token=0000000000000000000000000000` para validar el uso.
* **Consulta (q)**: `q=crisis` para ejecutar la consulta booleana adicional (que en este caso busca, dentro del universo del worker, resultados que contengan la palabra crisis).

Esta es la estructura mínima para acceder a la API de Telegram, pero a partir de aquí pueden utilizarse los parámetros disponibles en esta documentación (`ts`, `tsi`, `size`) para precisar y optimizar las consultas según las necesidades del usuario.

## Ejemplo de Salida

A continuación se muestra un ejemplo de salida de una llamada a la API. Esta salida incluye información sobre los resultados totales, restantes y la URL para obtener los siguientes resultados.

```
totalResults 295404987
restResults  295404887
next "https://telegram.trawlingweb.com/posts/010101010101010101?token=0000000000000000000000000000&ts=...&tsi=..."
```


## Uso de las Fechas `published` y `crawled`

TrawlingWeb entrega dos fechas para cada mensaje: `published` (fecha de creación/publicación en Telegram) y `crawled` (fecha de captura). Esto es crucial ya que, al incorporar nuevos canales o sufrir backfill, el sistema puede detectar como nuevos mensajes que fueron publicados días o incluso meses atrás.

También puede suceder que Telegram modifique la visibilidad de algún canal o reediciones provoquen capturas posteriores. Para evitar o controlar estos sucesos, aconsejamos que los clientes implementen reglas de seguridad en sus sistemas.

### Consejos sobre reglas para garantizar el buen uso de las fechas:

* **Filtros de Fecha**: Establecer filtros para ignorar mensajes con fechas de publicación muy antiguas si no son relevantes.
* **Reglas de Relevancia**: Crear criterios que determinen la relevancia de los mensajes en función de su fecha de publicación y la fecha de captura.
* **Monitoreo de Cambios**: Supervisar cambios en los canales rastreados para ajustar las reglas de procesamiento.
* **Alertas y Notificaciones**: Configurar alertas para detectar y notificar la aparición de mensajes antiguos, permitiendo una revisión manual si es necesario.

Implementar estas medidas ayuda a nuestros clientes a mantener la integridad y relevancia de los datos procesados por TrawlingWeb.

## Paginación

Cada solicitud a la API de Telegram puede devolver un máximo de resultados igual al `size` del plan (por defecto 100, configurable hasta el máximo permitido por el token). Sin embargo, pueden haber muchos más resultados que coincidan con tus parámetros de filtro. Para consumir todos los datos debes seguir realizando llamadas a la URL indicada en el parámetro **next** de la salida de cada solicitud.

La URL `next` incluye los valores `&ts` y `&tsi`, los cuales se ajustan automáticamente según el `crawled` del último resultado devuelto, permitiendo continuar la paginación sin perder mensajes.

Por defecto la API devuelve hasta 100 resultados por solicitud, aunque el total de mensajes coincidentes pueda ser mayor. En la respuesta JSON aparecerá el parámetro `next`, que sirve para realizar una llamada adicional a la API y obtener la siguiente página de resultados. Este proceso se repite hasta que se consumen todos los resultados disponibles.

Si necesitas recibir menos resultados por llamada a la API, puedes ajustar este número utilizando el parámetro `size=n`.

## Rangos temporales `ts` y `tsi`

* `ts` (timestamp inicial) — fecha desde la cual buscar mensajes capturados. Por defecto, 1 mes hacia atrás desde el momento de la petición.
* `tsi` (timestamp final) — fecha hasta la cual buscar. Por defecto, la fecha actual.
* Ambos en milisegundos Unix.
* Si se omiten o son inválidos, se aplican los valores por defecto.
* Si `ts > tsi`, la API responde con error.

## Endpoint de búsqueda booleana sobre el universo del consumer

Además de `/posts/:worker_id` (filtrado por las palabras clave de un worker concreto), la API expone `/posts/?q=…` que ejecuta la consulta booleana sobre **la unión de palabras clave de todos los workers del consumer**. Útil para búsquedas transversales sin tener que escoger un worker específico.

```
https://telegram.trawlingweb.com/posts/?token={APIKEY}&q=cocacola%20AND%20crisis&ts=...&tsi=...
```

## Mantenimiento Periódico de Fuentes de Datos

El mantenimiento periódico de los canales y grupos públicos rastreados es constante y esencial en TrawlingWeb. Implica una reevaluación integral de cada fuente, lo que a menudo conlleva la incorporación de nuevos canales relevantes. Contar con las fechas de publicación (`published`) y de captura (`crawled`) permite gestionar estas actualizaciones de manera eficiente.

### Consideraciones

* **Frecuencia de Indexación**: La frecuencia de indexación de una fuente se determina por las necesidades del cliente, los requisitos funcionales, la cantidad de mensajes y la frecuencia de publicación de cada canal.
* **Diferenciación de Fechas**: Diferenciar claramente la fecha de captura (`crawled`) de la fecha de publicación (`published`) permite que los clientes decidan qué mensajes incorporar.
* **Filosofía de Entrega de Contenido**: Nuestra filosofía es entregar todos los mensajes procesados, dejando la decisión sobre cómo utilizar este contenido a los clientes.

### Mensajes Entregados y Descartados

* **Mensajes Entregados**: Todos los mensajes procesados se entregan al cliente.
* **Mensajes Descartados**: Los clientes tienen la opción de descartar mensajes según sus criterios y necesidades específicas.

## Sintaxis de Consultas de Lucene

Las APIs de TrawlingWeb permiten realizar consultas que pueden contener operadores booleanos basados en la sintaxis de Lucene, ofreciendo una poderosa herramienta para realizar búsquedas complejas y precisas. La sintaxis de consultas de Lucene está diseñada para ser intuitiva y expresiva.

En la sección `06_Workers_Sintaxi_de_filtrado.md` encontrarás cómo usar adecuadamente expresiones booleanas y la sintaxis de Lucene.

---

# Contacto
Si tienes alguna pregunta, necesitas asistencia, contratar o ampliar tus servicios, por favor contacta con nosotros.

**SAT (Soporte Técnico):**
* [Correo SAT](mailto:support@trawlingweb.com)
* [Documentación Oficial](https://github.com/trawlingweb/APIservicies/tree/main/API%20Telegram)

**SAC (Soporte Administrativo):**
* [Correo SAC](mailto:gestion@trawlingweb.com)

**Sales (Soporte Ventas):**
* [Correo Ventas](mailto:sales@trawlingweb.com)
