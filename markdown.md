

 # Guía Básica de Sintaxis Markdown

## Encabezados

Para crear encabezados, utiliza el símbolo `#`. El número de `#` determina el nivel del encabezado.

```markdown
# Encabezado 1
## Encabezado 2
### Encabezado 3
#### Encabezado 4
##### Encabezado 5
###### Encabezado 6

Énfasis

Para aplicar énfasis al texto, utiliza asteriscos * o guiones bajos _.

 *Italic* o _Italic_
**Bold** o __Bold__
***Bold and Italic*** o ___Bold and Italic___

Listas
Listas Desordenadas

Para crear listas desordenadas, utiliza asteriscos *, guiones - o signos más +.

 * Elemento 1
* Elemento 2
  * Subelemento 2.1
  * Subelemento 2.2
* Elemento 3

Listas Ordenadas

Para crear listas ordenadas, utiliza números seguidos de un punto.

 1. Primer elemento
2. Segundo elemento
   1. Subelemento 2.1
   2. Subelemento 2.2
3. Tercer elemento

Enlaces

Para crear enlaces, utiliza corchetes [] para el texto del enlace y paréntesis () para la URL.

 [Texto del enlace](https://www.ejemplo.com)

Imágenes

Para insertar imágenes, utiliza un signo de exclamación ! seguido de corchetes [] para el texto alternativo y paréntesis () para la URL de la imagen.

 ![Texto alternativo](https://www.ejemplo.com/imagen.jpg)

Citas

Para crear citas, utiliza el símbolo >.

 > Esta es una cita.
> Puede tener múltiples líneas.

Código
Código en Línea

Para insertar código en línea, utiliza acentos graves `.

 Este es un ejemplo de código en línea: `print("Hola, mundo")`.

Bloques de Código

Para insertar bloques de código, utiliza tres acentos graves ```. Puedes especificar el lenguaje de programación para el resaltado de sintaxis.

 ```python
def hola_mundo():
    print("Hola, mundo")

## Tablas

Para crear tablas, utiliza guiones `-` y barras verticales `|`.

```markdown
| Encabezado 1 | Encabezado 2 |
|--------------|--------------|
| Celda 1      | Celda 2      |
| Celda 3      | Celda 4      |

Líneas Horizontales

Para crear líneas horizontales, utiliza tres o más asteriscos *, guiones - o guiones bajos _.

 ---

Saltos de Línea

Para forzar un salto de línea, utiliza dos espacios al final de la línea o una barra invertida \.

 Esta es una línea.
Esta es otra línea.

Listas de Tareas

Para crear listas de tareas, utiliza corchetes [] con un espacio y un guion -.

 - [ ] Tarea pendiente
- [x] Tarea completada

Notas al Pie

Para crear notas al pie, utiliza corchetes [] para el identificador y corchetes [] con un signo de circunflejo ^ para el contenido de la nota.

 Este es un texto con una nota al pie[^1].

[^1]: Este es el contenido de la nota al pie.

Ejemplo Completo

Aquí tienes un ejemplo completo que combina varios elementos de Markdown:

 # Título Principal

Este es un ejemplo de **Markdown**. Puedes crear *énfasis* y [enlaces](https://www.ejemplo.com).

## Listas

### Lista Desordenada

* Elemento 1
* Elemento 2
  * Subelemento 2.1
  * Subelemento 2.2

### Lista Ordenada

1. Primer elemento
2. Segundo elemento
   1. Subelemento 2.1
   2. Subelemento 2.2

## Imágenes

![Texto alternativo](https://www.ejemplo.com/imagen.jpg)

## Código

Este es un ejemplo de código en línea: `print("Hola, mundo")`.

```python
def hola_mundo():
    print("Hola, mundo")

Tablas
Encabezado 1	Encabezado 2
Celda 1	Celda 2
Celda 3	Celda 4
Citas

    Esta es una cita.
    Puede tener múltiples líneas.

Líneas Horizontales
Listas de Tareas

    Tarea pendiente
    Tarea completada

Notas al Pie

Este es un texto con una nota al pie1.

Puedes copiar y pegar este texto en tus apuntes que aceptan Markdown para tener una guía completa de la sintaxis de Markdown.

Espero que esto te sea útil para aprender Markdown. ¡Buena suerte con tus apuntes!
Footnotes

    Este es el contenido de la nota al pie. ↩
