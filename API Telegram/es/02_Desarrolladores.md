# API Telegram - Cosas que cada desarrollador debería saber

## Integridad de los Datos

La integridad de los datos se refiere a la precisión, consistencia y confiabilidad de los datos a lo largo del tiempo. Para garantizar la integridad de los datos proporcionados por nuestra API, Trawlingweb implementa las siguientes prácticas:

* **Verificación Continua**: Los datos son verificados continuamente durante el proceso de análisis para asegurar su exactitud y coherencia.
* **Corrección de Errores**: Cualquier inconsistencia o error detectado en los datos se corrige inmediatamente para mantener su fiabilidad.
* **Actualización Regular**: Los datos se actualizan regularmente para reflejar la información más reciente y relevante, minimizando la posibilidad de datos obsoletos.
* **Mantenimiento de Fuentes**: Se realiza un mantenimiento periódico de los canales y grupos públicos rastreados para asegurar que los datos procesados sean de alta calidad y actuales.

Implementar estas medidas ayuda a nuestros clientes a mantener la integridad y confiabilidad de los datos procesados por Trawlingweb.

## API REST

`telegram.trawlingweb.com` es una API REST, por lo que aunque los datos están destinados a ser consumidos como un flujo de datos, es necesario llamar a la API de forma continua con el fin de recibir los lotes de datos.

## La autenticación

La autenticación se confirma a través de un token de acceso único aprobado en la URL llamada a la API junto al id del Worker a ingestar.
Puede encontrar su token de acceso y sus ids de Worker en el panel de control.

## Límite de tarifa

Todos los planes de API Telegram incluyen un único token de acceso principal junto con el identificador concreto de cada Worker.
Se establece una limitación de velocidad de solicitud de una cada 5 segundos. Para superar dicho límite se tendrá que solicitar específicamente.

## Formatos de salida

Proporcionamos los datos en el siguiente formato de salida:

| Formato | Descripción                |
| ------- | :------------------------- |
| JSON    | JavaScript Object Notation |

## API de soporte de seguridad HTTP / HTTPS

`telegram.trawlingweb.com` soporta tanto las llamadas de punto final HTTP como HTTPS (SSL). Se recomienda usar siempre HTTPS.

## Las peticiones GET

Puede llamar a la API mediante peticiones GET. Si realiza llamadas muy largas a la API divídelas en varias consultas más cortas (usar `ts` y `tsi` para acotar rangos temporales).

## Códigos de estado HTTP

| Código | Descripción                                    |
| ------ | :--------------------------------------------- |
| 200    | ¡Éxito!                                        |
| 400    | Parámetros faltantes o consulta mal formada    |
| 401    | Usuario no autorizado o sin tokens disponibles |
| 404    | Error de sintaxis                              |
| 429    | Excede el límite de velocidad                  |
| 500    | No se pudo ejecutar la consulta                |
| 503    | Servicio no disponible temporalmente           |

NOTA: Detalle del error explicado en el retorno de la request.

# Contacto
Si tienes alguna pregunta, necesitas asistencia, contratar o ampliar tus servicios por favor contacta con nosotros.

**SAT (Soporte Técnico):**
* [Correo SAT](mailto:support@trawlingweb.com)
* [Documentación Oficial](https://github.com/trawlingweb/APIservicies/tree/main/API%20Telegram)

**SAC (Soporte administrativo):**
* [Correo SAC](mailto:gestion@trawlingweb.com)

**Sales (Soporte ventas):**
* [Correo Ventas](mailto:sales@trawlingweb.com)
