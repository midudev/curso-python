###
# 01 - print()
# El módulo print() es el módulo que nos permite imprimir en consola
# Sirve para mostrar información en consola y te va a acompañar
# TODA TU VIDA. Desde hoy hasta el fin de los tiempos
###

# Podemos importar módulos de Python para usarlos en nuestros programas.
# En este caso, importamos el módulo "os" que nos da acceso a funciones
# relacionadas con el sistema operativo
from os import system

# system() nos permite ejecutar un comando en la terminal.
# En este caso, lo hacemos para limpiar la pantalla tanto
# en MacOS/Linux usando "clear" como en Windows con "cls"
if system("clear") != 0: system("cls")

# Este es un ejemplo básico de cómo imprimir un texto en consola
print("¡Hola, Twitch!")

# También puedes usar comillas simples para imprimir texto
print('Esto también funciona con una comilla')

# Puedes imprimir múltiples elementos separados por un espacio
print("Python", "es", "genial")

# El parámetro 'sep' permite definir cómo se separan los elementos impresos
print("Python", "es", "brutal", sep = "-")

# El parámetro 'end' define lo que se imprime al final de la línea
print("Esto se imprime", end = "\n") # Aquí, el 'end' tiene un salto de línea explícito
print("en una línea") # Esto se imprime en la línea siguiente

# También se pueden imprimir números directamente
print(42)

# Ejemplo de cómo imprimir el símbolo de pulgadas (")
# Si usamos comillas dobles dentro de un string con comillas dobles, se produce un error:
# print("Esto es una "pulgada"")  # ❌ Esto generaría un error de sintaxis

# ✅ Solución 1: Usar comillas simples para encerrar la cadena
print('Esto es una "pulgada" dentro de un string con comillas simples')

# ✅ Solución 2: Usar el carácter de escape \ para incluir comillas dobles dentro de un string con comillas dobles
print("Esto es una \"pulgada\" dentro de un string con comillas dobles")

# ✅ Solución 3: Usar triple comillas para definir el string
print("""Esto es una "pulgada" dentro de un string con triple comillas""")