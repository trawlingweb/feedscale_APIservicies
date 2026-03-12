# API Facebook - Cosas que cada desarrollador debería saber

## Integridad de los Datos

La integridad de los datos se refiere a la precisión, consistencia y confiabilidad de los datos a lo largo del tiempo. Para garantizar la integridad de los datos proporcionados por nuestra API, Trawlingweb implementa las siguientes prácticas:

* **Verificación Continua**: Los datos son verificados continuamente durante el proceso de análisis para asegurar su exactitud y coherencia.
* **Corrección de Errores**: Cualquier inconsistencia o error detectado en los datos se corrige inmediatamente para mantener su fiabilidad.
* **Actualización Regular**: Los datos se actualizan regularmente para reflejar la información más reciente y relevante, minimizando la posibilidad de datos obsoletos.
* **Mantenimiento de Fuentes**: Se realiza un mantenimiento periódico de las fuentes de medios para asegurar que los datos procesados sean de alta calidad y actuales.

Implementar estas medidas ayuda a nuestros clientes a mantener la integridad y confiabilidad de los datos procesados por Trawlingweb.

## API REST

Trawlingweb.com es una API REST, por lo que aunque los datos está destinado a ser consumido como un flujo de datos, es necesario llamar a la API de forma continua con el fin de recibir los lotes de datos.

## La autenticación

La autenticación se confirmó a través de un token de acceso única aprobada en la URL llamada a la API junto al id del Worker a ingestar.
Puede encontrar su token de acceso y sus ids de Worker en el panel de control.

## Límite de tarifa

Todos los planes de API Facebook incluyen un único token de acceso único principal junto con el identificador concreto del cada Worker.
Se establece una limitación de velocidad de solicitud de una cada 5 segundos. Para superar dicho límite se tendrá que solucitar especificamente.

## Formatos de salida

Proporcionamos los datos en el siguiente formato de salida:

| Formato | Descripción                |
| ------- | :------------------------- |
| JSON    | JavaScript Object Notation |

## API de soporte de seguridad HTTP / HTTPS

Twalingwerb.com soporta tanto las llamadas de punto final HTTP y HTTPS (SSL).

## Las peticiones GET

Puede llamar a la API mediante peticiones GET. Si realiza llamadas muy largas a la API dividela en varias consultas más cortas.

## Códigos de estado HTTP

| Código | Descripción                                    |
| ------ | :--------------------------------------------- |
| 200    | ¡Éxito!                                        |
| 401    | Usuario no autorizado o sin tokens disponibles |
| 404    | Error de sintaxis                              |
| 500    | No se pudo ejecutar la consulta                |
| 503    | Servicio no disponible temporalmente           |
| 429    | Excede el límite de velocidad                  |

NOTA: Detalle del error explicado en el retorno de la request.

# Contacto
Si tienes alguna pregunta, necesitas asistencia, contratar o ampliar tus servicios por favor contacta con nosotros.

**SAT (Soporte Técnico):**
* [Correo SAT](mailto:support@trawlingweb.com)
* [Documentación Oficial](https://docs.trawlingweb.com)

**SAC (Soporte administrativo):**
* [Correo SAC](mailto:gestion@trawlingweb.com)

**Sales (Soporte ventas):**
* [Correo Ventas](mailto:sales@trawlingweb.com)


