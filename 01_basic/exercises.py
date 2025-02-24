###
# exercises.py
# Ejercicios para practicar los conceptos aprendidos en las lecciones.
###

print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")

### Completa aquí

name, city = input("What is your name and Where do you live?\n").split()
print("My name is" + " " + name, "I live in" + " " + city, sep="\n")

print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

### Completa aquí

print(
  f"a type is {type(a)}",
  f"b type is {type(b)}",
  f"c type is {type(c)}",
  f"d type is {type(d)}",
  f"e type is {type(e)}",
  sep="\n"
)

print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

### Completa aquí
str = "12345"
float_number = 3.99

new_int = int(str)
new_float = float(new_int)

print(new_int, new_float, sep="\n"  )

new_int = int(float_number)
print(new_int)

print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")

# "Hola! Me llamo midudev y tengo 39 años, mido 1.70 metros"

### Completa aquí

name = "Santiago"
age = 26
height = 1.71

print(f"Hola! Me llamo {name} y tengo {age}, mido {height} metros")

print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
print("2. Redondea el número con round()")
print("3. Haz la división entera entre el número que te salió y el número 2")
print("4. El resultado debería ser 1")

print(3.1416)
print(round(3.1416))
print(int(round(3.1416) / 2))