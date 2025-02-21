###
# 02 - types()
# Python tiene varios tipos de datos
# int, float, complex, str, bool, NoneType, list, tuple, dict, range, set...
###

from os import system
if system("clear") != 0: system("cls")

"""
El comando `type()` devuelve el tipo de un objeto en Python
"""
print("int:")  # Enteros (números sin parte decimal)
print(type(10))  # Número entero positivo
print(type(0))  # El número cero también es un entero
print(type(-5))  # Número entero negativo
print(type(7238424723784278934789239874))  # Python permite enteros de gran tamaño

print("float:")  # Números decimales (de punto flotante)
print(type(3.14))  # Número con punto decimal
print(type(1.0))  # También es considerado un float, aunque sea un número entero con punto decimal
print(type(1e3))  # Notación científica (equivalente a 1000.0)

print("complex:")  # Números complejos (con parte real e imaginaria)
print(type(1 + 2j))  # Un número complejo en Python (1 es la parte real, 2j es la parte imaginaria)

print("str:")  # Cadenas de texto (strings)
print(type("Hola"))  # Un string con texto
print(type(""))  # Un string vacío
print(type("123"))  # Aunque parezca un número, está entre comillas, por lo que es un string
print(type(""" 
  Multilinea
"""))  # Un string que abarca varias líneas usando triple comillas

print("bool:")  # Valores booleanos (True o False)
print(type(True))  # Valor booleano verdadero
print(type(False))  # Valor booleano falso
print(type(1 < 2))  # Comparación que devuelve un booleano (True)

print("NoneType:")  # Representa la ausencia de valor
print(type(None))  # `None` es un tipo especial en Python que representa "sin valor" o "nulo"