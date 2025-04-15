
# ESERCIZIO 5 

from typing import Callable

odd_or_even : Callable [[int] , int] = lambda x : "Pari" if x % 2 == 0 else "Dispari"

print(odd_or_even(7))