"""
Implementa una función que tome una lista de palabras
y devuelva una nueva lista que contenga sólo las palabras
que tienen más de 5 caracteres.

Por ejemplo, si la función recibe la lista
["Python", "Java", "C", "Scala", "Haskell"]
debe devolver ["Python", "Haskell"].
"""


def filter_words(words):
    return list(filter(lambda x: len(x) > 5, words))


words_list = ["Python", "Java", "C", "Scala", "Haskell"]

print(filter_words(words_list))
