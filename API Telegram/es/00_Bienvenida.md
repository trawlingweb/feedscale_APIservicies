# API de Telegram de Trawlingweb.com

Bienvenido a la documentación de la API de Telegram de Trawlingweb.com. Nuestra API proporciona acceso al repositorio de datos estructurados de **mensajes públicos de canales y grupos públicos de Telegram**. Nuestros sistemas analizan, procesan y estructuran esta información para su consulta bajo demanda, ofreciendo una solución eficaz y personalizada para tus necesidades de análisis de mensajería pública.

## Características Principales:

- **Contratación mediante Planes de créditos**: Contratación del servicio basada en la contratación de planes de créditos canjeables en número de palabras clave, donde 1 crédito = 1 palabra clave. De esta manera, el cliente puede escoger la cantidad de créditos que desea contratar, los cuales le permiten crear y monitorear palabras clave dentro de Telegram.

* **Palabras clave**: Una Palabra Clave es un término de búsqueda configurado dentro de un "worker". La cantidad de Palabras Clave que puedes registrar depende de los créditos contratados (1 crédito = 1 Palabra Clave). Los "workers" usan estas palabras clave para realizar búsquedas sobre los mensajes capturados de Telegram y recopilar datos específicos, los cuales se almacenan y están disponibles para consulta y descarga a través de API REST. Por lo tanto, los workers funcionan como una lista de palabras clave.

  Ejemplos de palabras clave y créditos necesarios para su creación:

| Palabra     | Número de elementos | Créditos necesarios (c1) | Búsqueda ejecutable                                                                |
| ----------- | ------------------- | ------------------------ | ---------------------------------------------------------------------------------- |
| @cocacola   | 1                   | 1                        | Menciones a una cuenta o lo que publica una cuenta que contiene otras palabras clave |
| cocacola    | 1                   | 1                        | Término exacto en el texto del mensaje                                             |
| "coca cola" | 1                   | 1                        | Frase exacta en el texto del mensaje                                               |

<br>

- **Acceso Estructurado a Datos de Telegram**: Obtén mensajes públicos de canales y grupos públicos de Telegram de forma organizada y accesible para análisis y procesamiento posterior.
- **Tecnología de Análisis Avanzada**: Utilizamos sistemas de última generación que garantizan el análisis preciso y actualizado de la información capturada.
- **Almacenamiento y Consulta Bajo Demanda**: Los datos procesados se almacenan en índices mensuales (`telegram_YYYY_MM`) para permitir consultas rápidas y flexibles según tus necesidades.
- **Cobertura Multidioma**: Mensajes en múltiples idiomas, con cobertura ampliada en canales públicos relevantes para monitoreo de marca, reputación e inteligencia.
- **Versatilidad y Optimización**: Combina la lista de palabras clave del worker con consultas booleanas / Lucene en el parámetro `q=` para refinar resultados sin consumir créditos adicionales.

### Beneficios para Empresas:

- **Monitoreo de Mensajería Pública**: Facilita a las empresas el seguimiento de conversaciones en canales y grupos públicos de Telegram, proporcionando insights valiosos sobre la percepción de marca, campañas, crisis y temas emergentes.
- **Análisis de Sentimiento**: Permite realizar análisis detallados del sentimiento en los mensajes, ayudando a comprender mejor la opinión pública y las reacciones a eventos específicos.
- **Detección Temprana**: Apoya la detección temprana de menciones críticas, filtraciones, alertas y desinformación que circulan por canales públicos.
- **Inteligencia y Riesgos**: Útil para equipos de reputación, compliance y seguridad corporativa que necesitan visibilidad sobre lo que se dice en Telegram.

Nuestra API de Telegram está diseñada para ser una herramienta potente y versátil, adaptada a las diversas necesidades de análisis de canales públicos de mensajería de nuestros usuarios. Te invitamos a explorar la documentación y descubrir cómo puedes aprovechar al máximo nuestras capacidades avanzadas de análisis y procesamiento de datos de Telegram.

---

# Contacto

Si tienes alguna pregunta, necesitas asistencia, contratar o ampliar tus servicios, por favor contacta con nosotros.

**SAT (Soporte Técnico):**

- [Correo SAT](mailto:support@trawlingweb.com)
- [Documentación Oficial](https://github.com/trawlingweb/APIservicies/tree/main/API%20Telegram)

**SAC (Soporte Administrativo):**

- [Correo SAC](mailto:gestion@trawlingweb.com)

**Sales (Soporte Ventas):**

- [Correo Ventas](mailto:sales@trawlingweb.com)
