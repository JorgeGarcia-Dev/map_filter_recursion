"""
Implementa una función que tome una lista de números y
devuelva una lista nueva donde cada elemento sea el doble del valor original.

Por ejemplo, si la función recibe la lista [1, 2, 3] debe devolver [2, 4, 6].
"""


def double_list():
    return list(map(lambda x: x * 2, num_list))


num_list = [1, 2, 3, 4, 5]

print(double_list())
