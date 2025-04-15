
print("Hello, World")

lista1: list = [1,2,3,4,5]

lista1.append (6)
print(lista1)

lista1.extend ([7,8,9])
print(lista1)

lista2: list = [10,11,12]

lista1.append (lista2)
print(lista1)  

matrice: list = ([2, 1], [5, 3]) 
img: list = ([0, 1, 1], [1, 0, 0], [0, 0, 0]) 

#  R: list = [[24, 128, 233], [10, 23, 255], [1, 0, 34]]
# G: list = [[24, 128, 233], [10, 23, 255], [1, 0, 34]]
# B: list = [[24, 128, 233], [10, 23, 255], [1, 0, 34]]

# print(B[0: len(B)]) 

a: list = [1, 2, 3]
b: list = [4, 5, 6]

   # print(a + b)    # sto unendo le due liste usando un comando diverso da extend ovvero (concatenazione)

# a = a + b 
# print(f"Funzione Extend  {a}")
# print(a.append(b))
# print(f"Funzione Append: {a}")   # f sta per formatter e formatta le stringhe sta a dire a python di sostituire il valore di a dove sta a 

# b = a
# a = 4
# print(a)   # se vado a printare queste righe di comando abbiamo che seguendo il codice b è la lista a e a è 4
# print(b)

# a.append(b)
# print(a[0][0])  # darà errore perchè non puoi indicizzare un intero 


m: set = {1, 1, 1, 1,}
print(m)

n: set = {1, 2, 5, 6, 9, "Francesco", "tre"}   # nei set non c'è ordine quindi dopo il comando print lìordine può cambiare
print(n)

myset = {1, 5, 7}
print(myset)
