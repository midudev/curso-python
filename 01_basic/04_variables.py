##
# 04 - Variables
# Las variables sirven para guardar datos en memoria.
# Python es un lenguaje de tipado dinámico y de tipado fuerte.
###

from os import system
if system("clear") != 0: system("cls")

# Para asignar una variable solo hace falta poner el nombre de la variable y asignarle un valor
my_name = "midudev"
print(my_name)  # Imprime el valor de la variable my_name

age = 32
print(age)  # Imprime el valor de la variable age)

# Reasignar un nuevo valor a una variable existente
age = 39
print(age)  # Ahora la variable age tiene el valor 39

# Tipado dinámico: el tipo de dato se determine en tiempo de ejecución
# No es necesario declarar explícitamente el tipo de variable
name = "midudev"
print(type(name))  # Muestra el tipo de dato de la variable name (str)

name = 32
print(type(name))  # Ahora la variable tiene un número entero (int)

# Tipado fuerte: Python no realiza conversione de tipo automáticas
# Esto generará un error porque no se puede sumar un número con una cadena
# print(10 + "2")  # ❌ TypeError: unsupported operand type(s) for +: 'int' and 'str'

# f-string (literal de cadena de formato)
# desde la versión Python 3.6
print(f"Hola {my_name}, tengo {age + 5} años")

# No recomendada forma de asignar variables
name, age, city = "midudev", 32, "Bogotá"

# Convenciones de nombres de variables
mi_nombre_de_variable = "ok" # snake_case
nombre = "ok"

miNombreDeVariable = "no-recomendado" # camelCase
MiNombreDeVariable = "no-recomendado" # PascalCase
minombredevariable = "no-recomendado" # todojunto

mi_nombre_de_variable_123 = "ok"

MI_CONSTANTE = 3.14 # UPPER_CASE -> constantes

# Nombres NO válidos de variables (esto generaría errores)
# 123123_variable = "ko"  # ❌ No puede comenzar con un número
# mi-variable = "ko"  # ❌ No puede contener guiones (-), usa guion bajo (_)
# mi variable = "ko"  # ❌ No puede contener espacios
# True = False  # ❌ No puedes sobrescribir palabras reservadas

# Palabras reservadas en Python (no se pueden usar como nombres de variables)

# ['False', 'None', 'True', 'and', 'as', 'assert',
# 'async', 'await', 'break', 'class', 'continue',
# 'def', 'del', 'elif', 'else', 'except', 'finally',
# 'for', 'from', 'global', 'if', 'import', 'in', 'is',
# 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise',
# 'return', 'try', 'while', 'with', 'yield']

# Anotaciones de tipo (opcional, para mayor claridad en el código)
is_user_logged_in: bool = True # Indica que la variable es un booleano
print(is_user_logged_in)

name: str = "midudev" # Indica que la variable es una cadena de texto
print(name)

