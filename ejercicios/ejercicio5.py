"""
Implementa una función que genere una
secuencia de números de Fibonacci
utilizando recursividad.

La función debe recibir como parámetro
la longitud de la secuencia que debe generar.
"""


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


n = 10
fib_sequence = list(map(fibonacci, range(n)))
print(fib_sequence)
