
# CONGETTURA DI COLLATZ

import matplotlib.pyplot as plt  # libreria che serve per fare il garafico della funzione

def collatz (num:float) -> list[float]:
    numeri: list = [num]

    while num != 1:

        if num % 2 == 0:
            num = num / 2
        else:
            num = (3 * num) + 1

        numeri.append(num)
    return numeri

print(collatz(8))

numeri: list[float] = collatz(9.0)
plt.plot(numeri)
plt.show()


