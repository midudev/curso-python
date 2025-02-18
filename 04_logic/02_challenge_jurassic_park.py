"""
En Jurassic Park, se ha observado que los dinosaurios carnívoros, como el temible T-Rex, depositan un número par de huevos. Imagina que tienes una lista de números enteros en la que cada número representa la cantidad de huevos puestos por un dinosaurio en el parque.

Importante: Solo se consideran los huevos de los dinosaurios carnívoros (T-Rex) aquellos números que son pares.

Objetivo:
Escribe una función en Python que reciba una lista de números enteros y devuelva la suma total de los huevos que pertenecen a los dinosaurios carnívoros (es decir, la suma de todos los números pares en la lista).
"""

from os import system
if system("clear") != 0: system("cls")

# Para ver si un número es par
# siempre usamos el módulo %
# nos da el resto de la división: eggs % 2 == 2

def count_carnivore_dinosaur_eggs(egg_list) -> int:
  """
  Esta función recibe una lista de numeros enteros que representan la cantidad de huevos que han puesto diferentes dinosaurios en el parque jurásico y los de número par son de carnívoros. Devuelve un número con la suma de todos los huevos de carnívoros.
  """
  total_carnivore_eggs = 0

  for eggs in egg_list:
    if eggs % 2 == 0:
      total_carnivore_eggs += eggs

  # esta forma más corta:
  # total_carnivore_eggs = sum(filter(lambda x: x % 2 == 0, egg_list))

  return total_carnivore_eggs

egg_list = [3, 4, 7, 5, 8]
print(count_carnivore_dinosaur_eggs(egg_list)) # 12