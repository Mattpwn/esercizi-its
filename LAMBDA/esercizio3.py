
# ESERCIZIO 3 

num_list : list[int] = [5, 12, 17, 18, 24, 32]

pari : list[int] = list(filter(lambda x : x % 2 == 0, num_list))

print(pari)