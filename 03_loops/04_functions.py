import os
os.system('clear')

###
# 04 - Funciones
# Bloques de código reutilizables y parametrizables para hacer tareas especificas
###

""" Definición de una función

def nombre_de_la_funcion(parametro1, parametro2, ...):
  # docstring
  # cuerpo de la función
  return valor_de_retorno # opcional

"""

# Ejemplo de una función para imprimir algo en consola
def saludar():
  print("¡Hola!")

# Ejemplo de una función con parámetro
def saludar_a(nombre):
  print(f"¡Hola {nombre}!")

saludar_a("midudev")
saludar_a("madeval")
saludar_a("pheralb")
saludar_a("felixicaza")
saludar_a("Carmen Ansio")

# Funciones con más parámetros
def sumar(a, b):
  suma = a + b
  return suma

result = sumar(2, 3)
print(result)

# Documentar las funciones con docstring
def restar(a, b):
  """Resta dos números y devuelve el resultado"""
  return a - b

# Parámetros por defecto
def multiplicar(a, b = 2):
  return a * b

print(multiplicar(2))
print(multiplicar(2, 3))

# Argumentos por posición
def describir_persona(nombre: str, edad: int, sexo: str):
  print(f"Soy {nombre}, tengo {edad} años y me identifico como {sexo}")

# parámetros son posicionales
describir_persona(1, 25, "gato")
describir_persona("midudev", 25, "gato")
describir_persona("hombre", "madeval", 39)

# Argumentos por clave
# parámetros nombrados
describir_persona(sexo="gato", nombre="midudev", edad=25)
describir_persona(sexo="hombre", nombre="madeval", edad=21) 

# Argumentos de longitud de variable (*args):
def sumar_numeros(*args):
  suma = 0
  for numero in args:
    suma += numero
  return suma

print(sumar_numeros(1, 2, 3, 4, 5))
print(sumar_numeros(1, 2))
print(sumar_numeros(1, 2,3 ,4, 5, 6, 7, 8, 9, 10))

# Argumentos de clave-valor variable (**kwargs):
def mostrar_informacion_de(**kwargs):
  for clave, valor in kwargs.items():
    print(f"{clave}: {valor}")

mostrar_informacion_de(nombre="midudev", edad=25, sexo="gato")
print("\n")
mostrar_informacion_de(name="madeval", edad=21, country="Uruguay")
print("\n")
mostrar_informacion_de(nick="pheralb", es_sub=True, is_rich=True)
print("\n")
mostrar_informacion_de(super_name="felixicaza", es_modo=True, gatos=40)

# Ejercicios

# Volver a los ejercicios anteriores
# y convertirlos en funciones
# e intentar utilizar todos los casos y conceptos
# que hemos visto hasta ahora

print('\nEjercicio 1: Calculadora simple')
# Pide al usuario dos números y una operación (+, -, *, **, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)
def calculadora():
  a = int(input('  favor ingresar un numero entero: '))
  b = int(input('  Por favor ingresar un numero entero: '))
  operacion = input('  Por favor inqique que operacion desea hacer: ')

  if (operacion == '+'): return print(f'{a} {operacion} {b} = {a + b}')
  if (operacion == '-'): return print(f'{a} {operacion} {b} = {a - b}')
  if (operacion == '*'): return print(f'{a} {operacion} {b} = {a * b}')
  if (operacion == '**'): return print(f'{a} {operacion} {b} = {a ** b}')
  if (operacion == '/'): return print(f'{a} {operacion} {b} = {a / b}')

# calculadora()

print("\nEjercicio 2: Ordenar y contar")
# Crea una lista con los siguientes números: [5, 2, 8, 1, 9, 4, 2].
# Ordena la lista de forma ascendente usando sort().
# Pide al usuario un numero para contar cuántas veces aparece en la lista usando count().
# Comprueba si el número 7 está en la lista usando in.
numeros = [5, 2, 8, 1, 9, 4, 2]
print(f'  Lista original: {numeros}')

def ordenar(lista):
    lista.sort()  
    print(f'  Lista ordenada: {lista}')

    return lista

def contar_en (lista):
  numero = int(input('Por favor indica que numero te gustaria buscar en la lista:  '))
  contador = lista.count(numero)
  print(f'El numero {numero} se puede encontrar {contador}')

  return contador

# contar_en(ordenar(numeros))

print("\nEjercicio 3: Números primos") 
# Pide al usuario que introduzca un número entero positivo N.
# Imprime todos los números primos menores o iguales que N usando un bucle while.
# Un número es primo si es divisible por sólo uno de los números enteros entre 1 y él mismo, incluido.
def primos_de(n):
  numero = 1

  while numero <= n:
    es_primo = True
    divisor = 2

    while divisor**2 <= numero:
      if numero % divisor == 0:
          es_primo = False
          break
      divisor += 1
    
    if es_primo: print(numero)
    numero += 1
        
# n = int(input("Introduce un número entero positivo N: "))
# primos_de(n)

print('\nEjercicio 4: Calcular la media de una lista')
# Dada la siguiente lista de números:
# numeros = [10, 20, 30, 40, 50]
# Calcula la media de los números usando un bucle for.
numeros = [10, 20, 30, 40, 50]
def calcular_media_de(lista):
  sum = 0

  for num in lista:
    sum += num
  
  print(f'  Media de {numeros} es: {sum / len(lista)}')
  return sum / len(lista)

# calcular_media_de(numeros)      

print('\nEjercicio 5: Filtrar cadenas por longitud')
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna"]
# Crea una nueva lista que contenga solo las palabras con más de 5 letras
# usando un bucle for y list comprehension.
palabras = ["casa", "arbol", "sol", "elefante", "luna", 'esternocleidomastoideo']

def chequear_contrasena():
  contrasena = ''

  es_valida = False
  while len(contrasena) < 8:
    contrasena = input("Introduce una contraseña (al menos 8 caracteres): ")

    if len(contrasena) < 8:
      print("La contraseña debe tener al menos 8 caracteres. Inténtalo de nuevo.")

  print("Contraseña válida")
  es_valida = True

  return es_valida

def filtrar_cadena(lista):
  while chequear_contrasena() != True:
    chequear_contrasena()
  
  por_encima_de_5 = [palabra for palabra in lista if len(palabra) > 5]
  print(por_encima_de_5)

  return por_encima_de_5

# filtrar_cadena(palabras)

print('\nEjercicio 6: Año bisiesto')
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.

year = int(input("Introduce un año que quieras saber si es bisiesto: "))

def verificar_bisiesto(year):
  if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(f'El año {year} si es bisiesto')
  else: print(f'El año {year} NO es bisiesto')

verificar_bisiesto(year)
