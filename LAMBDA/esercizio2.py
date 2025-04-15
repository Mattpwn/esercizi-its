
# ESERCIZIO 2

from typing import Callable

somma: Callable [[float, float], float] = lambda a , b : a + b

print(somma(2.5,4.2))
