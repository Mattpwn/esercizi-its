# ESERCIZIO 1

# def check_value (number):

#     if number < 5:
#         print(f" il numero {number} è minore di 5:" )

#     elif number > 5:
#         print(f" il numero {number} è maggiore di 5:")

#     else:

#         print(f"Il numero {number} è uguale a 5:")


# check_value(10)


#ESERCIZIO 2

# def check_lenght (stringa):

#     if len(stringa) > 10:
#         print(f"La stringa {stringa} è maggiore di 10.")

#     elif len(stringa) < 10:
#         print(f"La stringa {stringa} è minore di 10.")

#     else:
#         print(f"La stringa {stringa} è uguale a 10.")

# check_lenght(input(f"Inserire stringa: "))


# ESERCIZIO 3

# def print_numbers(mylist: list[int]):

#     for i in mylist:

#         print(i)

# mylist: list[int] = [1,2,3,4,5]
# print_numbers(mylist)


# ESERCIZIO 4

# def check_each(lista:list[int]):
#     for i in lista:
#         if i > 5:
#             print(f"Numero maggiore di 5")
#         elif i < 5:
#             print(f"Numero minore di 5")
#         else:
#             print(f"Numero uguale a 5")

# lista:list[int] = [1,2,3,5,6,9,80,87,50,21,23,54,13]
# check_each(lista)

# ESERCIZIO 5

# def add_one(a:int):
#     result = a+1
#     return result
# def add_one_to_list(lista:list[int]):
#     new_list:list[int] = []
#     for i in lista:
#         new_list.append(add_one(i))
#     return new_list

# lista:list[int] = [1,2,3]
# new_list=add_one_to_list(lista)
# print(new_list)