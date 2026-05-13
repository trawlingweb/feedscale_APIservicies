# Guía Básica - Operadores Booleanos en Búsquedas (Todas las APIs)

Todas las APIs de TrawlingWeb (News & Blogs, Twitter, Facebook, Instagram, TikTok) permiten el uso de sintaxis avanzada para afinar las búsquedas. Esta sintaxis se aplica siempre dentro del parámetro `q` (query) en la llamada a la API.

El motor de búsqueda subyacente utiliza **Apache Lucene**, lo que significa que puedes crear expresiones lógicas para encontrar exactamente lo que necesitas.

A continuación, se detallan los operadores lógicos universales que puedes usar en **cualquier API de TrawlingWeb**.

## 1. Operadores Booleanos Esenciales (AND, OR, NOT)

Los operadores booleanos deben escribirse siempre en **MAYÚSCULAS**.

### AND (Y)
Devuelve resultados que contienen **ambos** términos de búsqueda. Si omites el operador verbal pero dejas un espacio entre dos palabras, el sistema lo interpreta por defecto como un `AND`.

*   **Ejemplo:** `coca AND cola` (o alternativamente `coca cola`)
*   **Resultado:** Solo devolverá publicaciones que contengan la palabra "coca" y la palabra "cola" simultáneamente.

### OR (O)
Devuelve resultados que contienen **al menos uno** de los términos de búsqueda (o ambos).

*   **Ejemplo:** `coca OR pepsi`
*   **Resultado:** Devolverá publicaciones que contengan "coca", publicaciones que contengan "pepsi", y publicaciones que tengan ambas. Es ideal para buscar sinónimos o cubrir diferentes marcas en la misma petición.

### NOT (NO)
Excluye de los resultados las publicaciones que contengan el término situado justo después del `NOT`. También se puede utilizar el signo menos `-` enganchado a la palabra a excluir.

*   **Ejemplo:** `coca NOT pepsi` (o alternativamente `coca -pepsi`)
*   **Resultado:** Devolverá publicaciones que contengan "coca", pero descartará cualquiera de ellas si también contiene la palabra "pepsi".

---

## 2. Agrupación y Expresiones Exactas

Para construir consultas complejas o buscar frases específicas, debes usar paréntesis y comillas.

### Uso de Comillas (" ") - Búsqueda Exacta
Si buscas una frase compuesta por varias palabras en un orden específico, debes encerrarla entre comillas dobles.

*   **Ejemplo:** `"coca cola zero"`
*   **Resultado:** Buscará exactamente esa secuencia de tres palabras juntas. Si no usaras comillas, buscaría documentos que tengan las palabras "coca", "cola" y "zero" esparcidas por el texto.

### Uso de Paréntesis ( ) - Agrupación
Los paréntesis son fundamentales cuando combinas diferentes operadores (`OR` junto con `AND` o `NOT`), ya que agrupan lógicamente la consulta asegurando que el motor de búsqueda la ejecute en el orden correcto.

*   **Ejemplo:** `(coca OR pepsi) AND oferta`
*   **Resultado:** Busca publicaciones que contengan la palabra "oferta" y que, además, tengan la palabra "coca" o la palabra "pepsi".

*   **Ejemplo Complejo:** `((madrid OR barcelona) AND "coche electrico") NOT tesla`
*   **Resultado:** Busca publicaciones sobre coches eléctricos en Madrid o Barcelona, pero excluye cualquier resultado que mencione la marca Tesla.

---

## 3. Resumen de Caracteres Reservados

Si necesitas buscar uno de estos caracteres literalmente (y no usarlo como operador), debes "escaparlo" colocando una barra invertida `\` delante de él:

`+ - = && || > < ! ( ) { } [ ] ^ " ~ * ? : \ /`

*Por ejemplo: Para buscar la url exacta `https://trawlingweb.com`, deberías escribir `https\:\/\/trawlingweb.com`.*
