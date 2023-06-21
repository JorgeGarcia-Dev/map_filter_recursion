"""
Implementa una función que tome una lista de números
y devuelva True si todos los números son mayores
que 0 y False en caso contrario.
"""


def all_positive(numbers):
    return all(map(lambda x: x > 0, numbers))


print(all_positive([1, 2, 3, 4, 5]))
