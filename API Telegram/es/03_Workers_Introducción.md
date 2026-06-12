## ¿Qué es un Worker?

Un **Worker** en TrawlingWeb es una entidad clave que permite a los usuarios realizar búsquedas automatizadas y específicas sobre los mensajes capturados de canales y grupos públicos de Telegram, utilizando Palabras Clave. Estos Workers son configurados por los usuarios para monitorizar, analizar y procesar contenido en tiempo real o en intervalos establecidos, según sus necesidades específicas.

### Funcionamiento de los Workers

- **Palabras Clave:** Cada Worker está asociado a una o más Palabras Clave, que son términos de búsqueda definidos por el usuario. Estos términos pueden incluir menciones (@usuario), términos exactos, frases entre comillas o cualquier palabra o frase relevante para el monitoreo de mensajes en Telegram. La efectividad de un Worker depende de la precisión y relevancia de las Palabras Clave configuradas.

- **Créditos:** La cantidad de Palabras Clave que un usuario puede configurar dentro de un Worker depende del número de créditos disponibles en su cuenta de TrawlingWeb. En TrawlingWeb, 1 crédito equivale a 1 Palabra Clave. Por lo tanto, si un usuario tiene 10 créditos, puede configurar hasta 10 Palabras Clave para uno o varios Workers.

- **Rastreos y Resultados:** Una vez configurado, el Worker filtra el flujo continuo de mensajes capturados por nuestros rastreadores de Telegram en busca de contenido que coincida con las Palabras Clave especificadas. El contenido encontrado (texto del mensaje, autor, canal, fecha, etc.) es procesado y almacenado en índices mensuales `telegram_YYYY_MM`, permitiendo al usuario acceder a estos datos, analizarlos y generar informes detallados.

- **Intervalos de Búsqueda:** Los usuarios pueden consultar sus Workers tan a menudo como necesiten, ajustando la frecuencia de las llamadas según el nivel de detalle y la actualidad de la información que necesiten. Esto es particularmente útil para campañas de monitoreo en tiempo real, donde la inmediatez de la información es crucial.

- **Personalización:** Los Workers en TrawlingWeb permiten combinar las Palabras Clave configuradas con consultas booleanas / Lucene adicionales mediante el parámetro `q=`, así como acotar rangos temporales con `ts` y `tsi`. Esta personalización asegura que los resultados obtenidos sean altamente relevantes y específicos a las necesidades del usuario.

### Ejemplo de Uso

Supongamos que una marca quiere monitorizar en tiempo real cómo se habla de un lanzamiento de producto en canales públicos de Telegram. Configuran un Worker en TrawlingWeb con Palabras Clave como el nombre del producto, la marca y menciones a la cuenta oficial. A medida que los rastreadores de Trawlingweb capturan mensajes en canales públicos, el Worker analiza y almacena las coincidencias, permitiendo a la marca analizar el sentimiento general, identificar canales relevantes y responder rápidamente a las interacciones.

### Beneficios de Usar Workers en TrawlingWeb

- **Eficiencia:** Los Workers automatizan el proceso de búsqueda y monitoreo en Telegram, ahorrando tiempo y esfuerzo al usuario.
- **Escalabilidad:** Los usuarios pueden ajustar la cantidad de Workers y Palabras Clave según sus necesidades y créditos disponibles.
- **Precisión:** Al personalizar las Palabras Clave y combinarlas con `q=` en cada llamada, los resultados son altamente relevantes, permitiendo análisis más efectivos.
- **Inmediatez:** Ideal para campañas que requieren información en tiempo real, como gestión de crisis, monitoreo de filtraciones o lanzamientos de producto.

En resumen, un Worker en TrawlingWeb es una herramienta poderosa para gestionar y analizar grandes volúmenes de mensajes públicos de Telegram, proporcionando insights valiosos que pueden guiar decisiones estratégicas en tiempo real.
