# API de Reddit de Trawlingweb.com

Bienvenido a la documentación de la API de Reddit de Trawlingweb.com. Nuestra API proporciona acceso al repositorio de datos estructurados de **posts y comentarios públicos de Reddit**. Nuestros sistemas analizan, procesan y estructuran esta información para su consulta bajo demanda, ofreciendo una solución eficaz y personalizada para tus necesidades de análisis de foros.

## Características Principales:

- **Contratación mediante Planes de créditos**: Contratación del servicio basada en la contratación de planes de créditos canjeables en número de palabras clave, donde 1 crédito = 1 palabra clave. De esta manera, el cliente puede escoger la cantidad de créditos que desea contratar, los cuales le permiten crear y monitorear palabras clave dentro de Reddit.

* **Palabras clave**: Una Palabra Clave es un término de búsqueda configurado dentro de un "worker". La cantidad de Palabras Clave que puedes registrar depende de los créditos contratados (1 crédito = 1 Palabra Clave). Los "workers" usan estas palabras clave para realizar búsquedas sobre los posts y comentarios capturados de Reddit y recopilar datos específicos, los cuales se almacenan y están disponibles para consulta y descarga a través de API REST. Por lo tanto, los workers funcionan como una lista de palabras clave.

  Ejemplos de palabras clave y créditos necesarios para su creación:

| Palabra        | Número de elementos | Créditos necesarios (c1) | Búsqueda ejecutable                                                                |
| -------------- | ------------------- | ------------------------ | ---------------------------------------------------------------------------------- |
| u/cocacola     | 1                   | 1                        | Menciones a un usuario o lo que publica un usuario que contiene otras palabras clave |
| cocacola       | 1                   | 1                        | Término exacto en el texto del post/comentario                                     |
| "coca cola"    | 1                   | 1                        | Frase exacta en el texto del post/comentario                                       |

<br>

- **Acceso Estructurado a Datos de Reddit**: Obtén posts y comentarios públicos de Reddit de forma organizada y accesible para análisis y procesamiento posterior.
- **Búsqueda por Subreddit**: Filtra por el subreddit en el que aparece el contenido (campo `subreddit` indexado y buscable).
- **Tecnología de Análisis Avanzada**: Utilizamos sistemas de última generación que garantizan el análisis preciso y actualizado de la información capturada.
- **Almacenamiento y Consulta Bajo Demanda**: Los datos procesados se almacenan en índices mensuales (`reddit_YYYY_MM`) para permitir consultas rápidas y flexibles según tus necesidades.
- **Versatilidad y Optimización**: Combina la lista de palabras clave del worker con consultas booleanas / Lucene en el parámetro `q=` para refinar resultados sin consumir créditos adicionales.

### Beneficios para Empresas:

- **Monitoreo de Foros Públicos**: Facilita a las empresas el seguimiento de conversaciones y tendencias en Reddit, proporcionando insights valiosos sobre la percepción de marca, dinámicas de comunidad y temas emergentes.
- **Análisis de Sentimiento**: Permite realizar análisis detallados del sentimiento en los hilos de discusión, ayudando a comprender mejor la opinión pública y las reacciones a eventos específicos.
- **Identificación de Comunidades Relevantes**: Detecta los subreddits donde más se habla de tu marca, producto o categoría.
- **Estrategias de Marketing**: Apoya el desarrollo de estrategias de marketing basadas en datos reales de discusión y engagement en Reddit.

Nuestra API de Reddit está diseñada para ser una herramienta potente y versátil, adaptada a las diversas necesidades de análisis de foros y comunidades online de nuestros usuarios. Te invitamos a explorar la documentación y descubrir cómo puedes aprovechar al máximo nuestras capacidades avanzadas de análisis y procesamiento de datos de Reddit.

---

# Contacto

Si tienes alguna pregunta, necesitas asistencia, contratar o ampliar tus servicios, por favor contacta con nosotros.

**SAT (Soporte Técnico):**

- [Correo SAT](mailto:support@trawlingweb.com)
- [Documentación Oficial](https://github.com/trawlingweb/APIservicies/tree/main/API%20Reddit)

**SAC (Soporte Administrativo):**

- [Correo SAC](mailto:gestion@trawlingweb.com)

**Sales (Soporte Ventas):**

- [Correo Ventas](mailto:sales@trawlingweb.com)
