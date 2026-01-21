# API FeedScale de Trawlingweb.com

Bienvenido a la documentación de la API FeedScale de Trawlingweb.com. Nuestra API proporciona acceso al repositorio de datos estructurados de publicaciones capturadas desde múltiples fuentes de redes sociales y medios digitales. Los datos se almacenan en BigQuery y están disponibles para consulta bajo demanda a través de una API REST, ofreciendo una solución eficaz y escalable para tus necesidades de análisis de contenido y monitoreo de marca.

## ¿Qué es GeriAI?

**GeriAI** es el motor de inteligencia artificial cognitiva desarrollado por Trawlingweb que procesa y analiza automáticamente las publicaciones capturadas en el repositorio de FeedScale. GeriAI es un sistema de IA avanzado que utiliza técnicas de Procesamiento de Lenguaje Natural (NLP), Machine Learning, Deep Learning, Análisis de Sentimientos, Extracción de Entidades Nombradas (NER), Clasificación de Texto, Análisis de Tópicos (LDA, BERT), Embeddings Semánticos y Transfer Learning para transformar contenido no estructurado en datos inteligentes y accionables.

### Análisis Multidimensional de GeriAI

GeriAI enriquece cada publicación con análisis cognitivo en **9 dimensiones estándar**:

1. **Intención del Mensaje**: Clasifica el propósito comunicativo (publicidad, queja, denuncia, elogio, recomendación, etc.)
2. **País de Origen**: Determina el país más probable del autor basándose en indicadores lingüísticos y culturales
3. **Perfil del Autor**: Identifica el rol del autor (consumidor, afectado, colaborador, directivo, medios, influenciador, etc.)
4. **Género del Autor**: Identifica el género aparente basándose en indicadores lingüísticos
5. **Rango de Edad**: Estima el rango de edad del autor (15-20, 21-30, 31-40, 41-55, 56+)
6. **Temas Sensibles**: Identifica temas críticos específicos del sector que requieren atención especial
7. **Tono del Mensaje**: Analiza el estilo comunicativo (oficial, personal, crítico, apoyo, neutral, emocional, etc.)
8. **Tipo de Apelación**: Identifica la estrategia persuasiva (emocional, lógica, autoridad, urgencia, social)
9. **Entidad Focal del Ecosistema**: Clasifica el contexto sectorial o temático del contenido

### Análisis Adicionales

Además de las dimensiones estándar, GeriAI proporciona:

- **Análisis de Sentimiento**: Clasificación automática del sentimiento (positivo, negativo, neutro) con valores numéricos precisos (`sentimiento`, `tono_positivo`, `tono_neutro`, `tono_negativo`)
- **Categorización Temática**: Clasificación automática en hasta 20 categorías temáticas diferentes (`categoria1` a `categoria20`), permitiendo análisis granular del contenido
- **Detección de Idioma**: Identificación automática del idioma de cada publicación (`lang`)
- **Análisis de Marcas**: Detección y clasificación de menciones de marcas, incluyendo marca principal (`marca_principal`) y marcas relacionadas (`marcas_relacion`)

### Procesamiento Automático

Todos estos análisis son realizados automáticamente por GeriAI durante el proceso de captura y almacenamiento en BigQuery. Los datos que obtienes a través de esta API ya incluyen estos enriquecimientos de inteligencia artificial cognitiva, listos para ser utilizados directamente en tus análisis, reportes y generación de KPIs sin necesidad de procesamiento adicional.

## Características Principales:

- **Acceso Estructurado a Datos de FeedScale**: Obtén datos de publicaciones de forma organizada y accesible desde BigQuery para análisis y procesamiento posterior. Los datos incluyen información detallada sobre publicaciones de Twitter, Instagram, Facebook y otras fuentes.

- **Tecnología Avanzada de Almacenamiento**: Utilizamos Google BigQuery como motor de almacenamiento y consulta, garantizando escalabilidad, rendimiento y capacidad para manejar grandes volúmenes de datos históricos.

- **Consulta Bajo Demanda**: Los datos capturados se almacenan de manera eficiente en BigQuery, permitiendo consultas rápidas y flexibles según tus necesidades específicas de análisis.

- **Paginación Inteligente**: La API implementa un sistema de paginación que permite consumir grandes volúmenes de datos de forma eficiente, con un máximo de 500 resultados por solicitud para garantizar el rendimiento del servidor.

- **Filtrado Temporal Flexible**: Utiliza delimitadores temporales (`ts` y `tsi`) para acotar tus consultas a rangos de fechas específicos, desde las últimas horas hasta períodos históricos completos.

- **Autenticación por API Key**: Sistema de autenticación seguro mediante tokens individuales e intransferibles, vinculados a tus servicios y características específicas.

### Beneficios para Empresas:

- **Monitoreo de Marca**: Facilita a las empresas el seguimiento de menciones y conversaciones sobre sus marcas en múltiples plataformas, proporcionando insights valiosos sobre la percepción de marca y dinámicas del mercado.

- **Análisis de Sentimiento con GeriAI**: Accede a análisis de sentimiento pre-procesados por GeriAI, permitiendo análisis detallados del sentimiento en las publicaciones (positivo, negativo, neutro) sin necesidad de procesar los datos manualmente. Esto ayuda a comprender mejor la opinión pública y las reacciones a eventos específicos de forma inmediata.

- **Análisis Temporal**: Accede a datos históricos para realizar análisis de tendencias, comparaciones temporales y seguimiento de evolución de conversaciones a lo largo del tiempo.

- **Estrategias de Marketing Basadas en Datos**: Apoya el desarrollo de estrategias de marketing basadas en datos reales de interacción y participación en redes sociales.

- **Integración con BigQuery**: Los datos están almacenados en BigQuery, permitiendo integraciones directas con herramientas de análisis y visualización de datos empresariales.

### Estructura de Datos:

La API proporciona acceso a un conjunto completo de campos por cada publicación, incluyendo:

- **Información de la Publicación**: ID, texto, URL, fecha de publicación, autor
- **Métricas de Engagement**: Likes, retweets, comentarios, reproducciones, interacciones totales
- **Análisis GeriAI**: Sentimiento (valores numéricos), tono (positivo/negativo/neutro), tono_positivo, tono_neutro, tono_negativo, categorías temáticas (categoria1 a categoria20)
- **Metadatos**: Idioma, origen (plataforma), marca relacionada, categorías de clasificación
- **Información de Marca**: Marca principal, marcas relacionadas, agente ID, empresa ID

### Formato de Respuesta:

La API devuelve datos en formato JSON estructurado, incluyendo:

- **Datos de Publicaciones**: Array con los posts que coinciden con tus criterios de búsqueda
- **Información de Paginación**: Total de resultados, resultados restantes, URL para la siguiente página
- **Filtros Aplicados**: Información sobre los parámetros utilizados en la consulta

Nuestra API FeedScale está diseñada para ser una herramienta potente y versátil, adaptada a las diversas necesidades de análisis de contenido y monitoreo de redes sociales de nuestros usuarios. Te invitamos a explorar la documentación y descubrir cómo puedes aprovechar al máximo nuestras capacidades avanzadas de consulta y análisis de datos.

---

## Inicio Rápido

Para comenzar a usar la API, necesitarás:

1. **Token de Acceso**: Tu API Key única proporcionada por Trawlingweb
2. **Endpoint Base**: `https://feedscale.trawlingweb.com/posts`
3. **Parámetros de Consulta**: `token`, `ts`, `tsi`, `size` (opcionales)

### Ejemplo Básico:

```
GET https://feedscale.trawlingweb.com/posts?token=TU_API_KEY
```

Esta llamada devolverá los últimos 500 resultados del último mes, con información de paginación para acceder a más datos si es necesario.

---

## Contacto

Si tienes alguna pregunta, necesitas asistencia, contratar o ampliar tus servicios, por favor contacta con nosotros.

**SAT (Soporte Técnico):**

- [Correo SAT](mailto:support@trawlingweb.com)
- [Documentación Oficial](https://docs.trawlingweb.com)

**SAC (Soporte Administrativo):**

- [Correo SAC](mailto:gestion@trawlingweb.com)

**Sales (Soporte Ventas):**

- [Correo Ventas](mailto:sales@trawlingweb.com)
