# API Print media – Cosas que cada desarrollador debería saber

## API REST

La API de **Print media** de TrawlingWeb es una API REST. Los datos se entregan en lotes, por lo que deberás hacer llamadas continuas para recuperar todos los registros de artículos en prensa escrita.

---

## Integridad de los Datos

Para garantizar que los datos de prensa escrita sean siempre precisos y fiables, TrawlingWeb aplica:

- **Verificación Continua**
  Cada artículo extraído se somete a validaciones automáticas (metadatos, fechas, formato de texto) en el momento del procesamiento.

- **Corrección de Errores**
  Cualquier anomalía detectada (texto truncado, campos faltantes) se corrige o marca para retrabajo antes de ponerla a disposición.

- **Actualización Regular**
  Los artículos pueden actualizarse tras su publicación; el campo `updated` refleja la última revisión.

- **Mantenimiento de Fuentes**
  Revisamos periódicamente nuestros repositorios de periódicos y revistas para incorporar nuevos títulos o rutas de acceso.

---

## Estructura de la URL de Consulta

La URL de llamada al endpoint de Print media consta de tres partes:

1. **Autenticación**
2. **Cadena GET** con parámetros de token, rango de fechas, paginación y formato.
3. **Filtros** que limitan la búsqueda a campos como `site`, `published`, `site_country`, etc.

```text
https://api.trawlingweb.com/press-written?
   token=TU_TOKEN           ← Autenticación
 & from=2025-05-01          ← Fecha inicio (ISO 8601)
 & to=2025-05-29            ← Fecha fin (ISO 8601)
 & page=1                   ← Paginación
 & format=json              ← JSON o xml
 & site=Expreso             ← Filtros opcionales
```

---

## Autenticación

Cada petición requiere un parámetro `token` válido en la URL. Encuentra tu token en el panel de control de TrawlingWeb.

---

## Límite de tarifa

- **1 solicitud/segundo** por token.
- Para elevar el throughput, adquiere un plan adicional o amplía tu suscripción.

---

## Formatos de salida

| Formato | Descripción                |
| ------- | :------------------------- |
| `json`  | JavaScript Object Notation |
| `xml`   | eXtensible Markup Language |

---

## Soporte HTTP/HTTPS

Los endpoints están disponibles tanto en HTTP como en HTTPS. Se recomienda HTTPS para producción.

---

## Peticiones GET

- La API se consume mediante peticiones HTTP GET.
- Para rangos muy amplios (muchos artículos) particiona la consulta en tramos de fechas o páginas.

---

## Códigos de estado HTTP

| Código | Descripción                                |
| ------ | :----------------------------------------- |
| 200    | Éxito: la respuesta contiene datos válidos |
| 401    | No autorizado: token ausente o inválido    |
| 404    | Recurso no encontrado o error de ruta      |
| 429    | Límite de velocidad excedido               |
| 500    | Error interno del servidor                 |
| 503    | Servicio temporalmente no disponible       |

> **Nota:** El cuerpo de error (`error` / `message`) detalla la causa.

---

# Contacto

Si tienes dudas, necesitas asistencia o quieres ampliar tu plan:

**Soporte Técnico (SAT):**

- [support@trawlingweb.com](mailto:support@trawlingweb.com)
- [Documentación Oficial](https://docs.trawlingweb.com)

**Soporte Administrativo (SAC):**

- [gestion@trawlingweb.com](mailto:gestion@trawlingweb.com)

**Ventas (Sales):**

- [sales@trawlingweb.com](mailto:sales@trawlingweb.com)

---
