
# ESERCIZIO 6

from functools import reduce

numeri:list [int] = [2, 3, 4]

prodotto = reduce(lambda x, y: x * y, [2, 3, 4])

print(prodotto)