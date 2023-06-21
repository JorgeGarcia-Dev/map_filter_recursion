"""
Implementa una función que genere una
secuencia de números de Fibonacci
utilizando recursividad.

La función debe recibir como parámetro
la longitud de la secuencia que debe generar.
"""


def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        sequence = fibonacci(n - 1)
        sequence.append(sequence[-1] + sequence[-2])
        return sequence


n = 10
fib_sequence = fibonacci(n)
print(fib_sequence)
