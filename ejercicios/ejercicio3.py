"""
Implementa una función recursiva que
calcula el factorial de un número dado.

Recuerda que el factorial de un número
es el producto de todos los números
desde 1 hasta el propio número.
"""


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


n = 5
factorial_result = factorial(n)
print(factorial_result)
