##
# 01 - Expresiones regulares
# 

""" 
Las expresiones regulares son una secuencia de caracteres que forman un patrón de búsqueda.

Se utilizan para la búsqueda de cadenas de texto, validación de datos, etc. 
"""


""" ¿Por qué aprender Regex?

- Búsqueda avanzada: Encontrar patrones específicos en textos grandes de forma rápida y precisa. (un editor de Markdown sólo usando Regex)

- Validación de datos: Asegurarte que los datos que ingresa un usuario como el email, teléfono, etc. son correctos.

- Manipulación del texto: Extraer, reemplazar y modificar partes de la cadena de texto fácilmente
"""

# 1. Importar el módulo de expresiones regulares "re"
import re
# 2. Crear un patrón, que es una cadena de texto que describe lo que queremos encontrar
pattern = "Hola"
# 3. El texto donde queremos buscar
text = "Hola mundo"
# 4. Usar la función de búsqueda de "re"
result = re.search(pattern, text)

if result:
  print("He encontrado el patrón en el texto")
else:
  print("No he encontrado el patrón en el texto")

# .group() devuelve la cadena que coincide con el pattern
print(result.group())

# .start() devolver la posición inicial de la coincidencia
print(result.start())

# .end() devolver la posición final de la coincidencia
print(result.end())

# EJERCICIO 01
# Encuentra la primera ocurrencia de la palabra "IA" en el siguiente texto
# e indica en que posición empieza y termina la coincidencia.
text = "Todo el mundo dice que la IA nos va a quitar el trabajo. Pero solo hace falta ver cómo la puede cagar con las Regex para ir con cuidado"
pattern = "IA"
found_ia = re.search(pattern, text)

if found_ia:
  print(f"He encontrado el patrón en el texto en la posición {found_ia.start()} y termina en la posición {found_ia.end()}")
else:
  print("No he encontrado el patrón en el texto")

# -----------------------

### Encontrar todas las coincidencias de un patrón
# .findall() devuelve una lista con todas las coincidencias

text = "Me gusta Python. Python es lo máximo. Aunque Python no es tan difícil, ojo con Python"
pattern = "Python"

matches = re.findall(pattern, text)

print(len(matches))

# -------------------------

# iter() devuelve un iterador que contiene todos los resultados de la búsqueda

text = "Me gusta Python. Python es lo máximo. Aunque Python no es tan difícil, ojo con Python"
pattern = "Python"

matches = re.finditer(pattern, text)

for match in matches:
  print(match.group(), match.start(), match.end())

# EJERCICIO 02
# Encuentra todas las ocurrencias de la palabra "midu" en el siguiente texto e indica en que posición empieza y termina cada coincidencia y cuantas veces se encontró.
text = "Este es el curso de Python de midudev. ¡Suscríbete a midudev si te gusta este contenido! midu"
pattern = 'midu'
matches = re.finditer(pattern, text)

total_matches = 0
for match in matches:
  total_matches += 1
  print(f'{match.group()} => {match.start()}:{match.end()}')

print(f'Total de coincidencias: {total_matches}')


### Modificadores

# Los modificadores son opciones que se pueden agregar a un patrón para cambiar su comportamiento

# re.IGNORECASE: Ignora las mayúsculas y minúsculas

text = "Todo el mundo dice que la IA nos va a quitar el trabajo. Pero la ia no es tan mala. ¡Viva la Ia!"
pattern = "ia"
found = re.findall(pattern, text, re.IGNORECASE)

if found: print(found)

# EJERCICIO 03
# Encuentra todas las ocurrencias de la palabra "python" en el siguiente texto, sin distinguir entre mayúsculas y minúsculas.
text = "Este es el curso de Python de midudev. ¡Suscríbete a python si te gusta este contenido! PYTHON"
pattern = 'python'
matches = re.findall(pattern, text, re.I)

print(matches)

### Reemplazar el texto

# .sub() reemplaza todas las coincidencias de un patrón en un texto

text = "Hola, mundo! Hola de nuevo. Hola otra vez."
pattern = "hola"
replacement = "Adiós"

new_text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
print(new_text)
