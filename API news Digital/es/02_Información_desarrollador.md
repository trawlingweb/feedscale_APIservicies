# API NEWS & BLOGS - Cosas que cada desarrollador debería saber

## API REST

Trawlingweb.com API NEWS & BLOGS es una API REST, por lo que aunque los datos está destinado a ser consumido como un flujo de datos, es necesario llamar a la API de forma continua con el fin de recibir los lotes de datos.

## Integridad de los Datos

La integridad de los datos se refiere a la precisión, consistencia y confiabilidad de los datos a lo largo del tiempo. Para garantizar la integridad de los datos proporcionados por nuestra API, Trawlingweb implementa las siguientes prácticas:

* **Verificación Continua**: Los datos son verificados continuamente durante el proceso de indexación para asegurar su exactitud y coherencia.
* **Corrección de Errores**: Cualquier inconsistencia o error detectado en los datos se corrige inmediatamente para mantener su fiabilidad.
* **Actualización Regular**: Los datos se actualizan regularmente para reflejar la información más reciente y relevante, minimizando la posibilidad de datos obsoletos.
* **Mantenimiento de Fuentes**: Se realiza un mantenimiento periódico de las fuentes de medios para asegurar que los datos indexados sean de alta calidad y actuales.

Implementar estas medidas ayuda a nuestros clientes a mantener la integridad y confiabilidad de los datos indexados por Trawlingweb.

## Estructura de URL

### La llamada de consulta URL tiene tres partes:

- Autentificación
- El HTTP GET cadena de parámetros para la autenticación, período de tiempo, la paginación, y el formato.
- La cadena de consulta que pasa las llaves de filtro y emparejamientos de valor respectivos lo que la API recupera sólo los datos que necesita.

## La autenticación

La autenticación se confirmó a través de un token de acceso única aprobada en la URL llamada a la API. Puede encontrar su token de acceso en el panel de control.

## Límite de tarifa

Todos los planes de API NEWS & BLOGS incluyen un único token de acceso único, con una limitación de velocidad incorporados de 1 (un) solicitud por segundo. Para superar dicho límite se tendrá que añadir un segundo plan.

## Los formatos de salida

Proporcionamos los datos en varios formatos de salida que puede elegir:

| Formato | Descripción                |
| ------- | :------------------------- |
| JSON    | JavaScript Object Notation |
| XML     | eXtensible Markup Language |

## API de soporte de seguridad HTTP / HTTPS

Twalingwerb.com soporta tanto las llamadas de punto final HTTP y HTTPS (SSL).

## Las peticiones GET

Puede llamar a la API mediante peticiones GET. si realiza llamadas muy largas a la API dividela en varias consultas más cortas.

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
