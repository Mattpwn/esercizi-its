
# ESERCIZIO 4

student_list : list[tuple] = [("Luca", 21), ("Anna", 19), ("Marco", 22)]

lista_sorted_age : list[tuple] = sorted (student_list, key = lambda age: tuple[0] (age))

print(lista_sorted_age)