
# ESERCIZIO 4.1

# lista_pizza: list[str] = ["Diavola", "Pistacchiosa", "Margherita"]

# for i in lista_pizza:
#     print(i)

# for i in lista_pizza:
#     print(f"Adoro la {i}")

# print("la pizza è il mio cibo preferito")

# ESERCIZIO 4.2

# lista_animali: list[str] = ["foca", "balena", "narvalo", "pesce rosso"]

# for i in lista_animali:
#     print(i)
   
# for i in lista_animali:
#     print(f" {i} è un animale acquatico")

# print("il pesce rosso è un ottimo animale domestico")

# ESERCIZIO 4.3

# lista_1 : list = (range(1,21))

# for i in range(1,21):
#     print(i)

# ESERCIZIO 4.4

# lista_1 : list = (range(1,1000001))

# for i in range(1,1000001):
#     print(i)

# ESERCIZIO 4.5

# list_number:list[int] = []
# for i in range(1,1000001):
#     list_number.append(i)
# print(min(list_number))
# print(max(list_number))
# print(sum(list_number))

# ESERCIZIO 4.6

# list_number : list[int] = []

# for i in range(1,21,2):
#     print(i)


# ESERCIZIO 4.7 

# ist_number : list[int] = []

# for i in range(3,31,3):
#     print(i)

# ESERCIZIO 4.8

# cubes: list[int]=[]
# for i in range(1,10):
#     i=i**3
#     cubes.append(i)
# print(cubes)

# ESERCIZIO 4.10

# lista_pizza: list[str] = ["Diavola", "Pistacchiosa", "Margherita","Crostino","Patate","Salsiccia e patate","Marinara","Supplì","Capricciosa"]

# print(f"Questi sono i primi tre elementi della lista {lista_pizza [0:3]}")
# print(f"Questo è il centro della lista {lista_pizza [3:6]}")
# print(f"Questa è la fine della tua lista  {lista_pizza [6:9]}")

# ESERCIZIO 4.11

# pizza_list : list[str] = ["Margherita" , "Marinara" , "Diavola"]
# friend_pizzas:list[str]= ["Margherita" , "Marinara" , "Diavola"]
# pizza_list.append ("Vegetariana")
# friend_pizzas.append ("Pistacchiosa")

# for i in pizza_list:
#     print(f"le mie pizze preferite sono:\n {i}")
# for i in friend_pizzas:
#     print(f"Le pizze preferite del mio amico sono:\n {i}")

# ESERCIZIO 4.15

#indentation

# lista_pizza: list[str] = [
#     "Diavola", "Pistacchiosa", "Margherita"
#     ]
# friend_pizzas: list[str] = [
#     "Diavola", "Pistacchiosa", "Margherita"
#     ]

# lista_pizza.append ("Vegetariana")
# friend_pizzas.append ("Napoli")

# for i in lista_pizza:
#     print (f" Le mie pizze preferite sono: \n {i}")
# for i in friend_pizzas:
#     print (f" Le pizze preferite del mio amico sono: \n {i}")

# #comments

# #definisco una lista
# lista_animali: list[str] = ["foca", "balena", "narvalo", "pesce rosso"]

# #ciclo for
# for i in lista_animali:
#     print(i)

# #ciclo for   
# for i in lista_animali:
#     print(f" {i} è un animale acquatico")


# print("il pesce rosso è un ottimo animale domestico")

# #spaces

# lista_pizza: list[str] = ["Diavola","Pistacchiosa","Margherita"]
# friend_pizzas: list[str] = ["Diavola","Pistacchiosa","Margherita"]

# lista_pizza.append ("Vegetariana")
# friend_pizzas.append ("Napoli")

# for i in lista_pizza:
#     print (f" Le mie pizze preferite sono: \n {i}")
# for i in friend_pizzas:
#     print (f" Le pizze preferite del mio amico sono: \n {i}")


# ESERCIZIO 5.1

# macchine : str = input("Inserisci il modello della macchina: ")

# predict : bool

# if macchine == "BMW":
#     predict = True
#     print(f" is {macchine} == macchina? I predict {predict}")

# elif macchine == "Audi":
#     predict = True
#     print(f" is {macchine} == macchina? I predict {predict}")

# elif macchine == "Ferrari":
#     predict = True
#     print(f" is {macchine} == macchina? I predict {predict}")

# elif macchine == "Lamborghini":
#     predict = True
#     print(f" Is {macchine} == macchina? I predict {predict}")

# elif macchine == "Mercedes":
#     predict = True
#     print(f" Is {macchine} == macchin? I predict {predict}")

# elif macchine == "Ducati":
#     predict = False
#     print(f" Is {macchine} = macchina? I predict {predict}")

# elif macchine == "SH":
#     predict = False
#     print(f" Is {macchine} == macchina? I predict {predict}")

# elif macchine == "KTM":
#     predict = False
#     print(f" Is {macchine} == macchiana?  predict {predict}")

# elif macchine == "Kawasaki":
#     predict = False
#     print(f" Is {macchine} == macchina? I predict {predict}")

# elif macchine == "Yamaha":
#     predict = False
#     print(f" Is {macchine} == macchina. I predict {predict}")

# else:
#     print(" La macchina inserita non sta nell'elenco ")

# ESERCIZIO 5.2

# from typing import Any
# color:str = input("Inserisci un colore: ")
# num:int = int(input("Inserisci un numero da 1 a 10: "))
# list_cose:list[Any] = [1,2,3,4,5,6,7,8,9,10]
# predict:bool

# if color == "yellow":
#     predict=True
#     print(f"Il colore inserito è yellow? {predict}")
# else:
#     predict=False
#     print(f"Il colore inserito è yellow? {predict}")

# if color == "red".lower():
#     predict=True
#     print(f"{color.lower()} == color? {predict}")
# else:
#     predict=False
#     print(f"Predict {predict}")

# if num > 6:
#     predict=True
#     print(f"Il numero inserito {num} è maggiore di 6? {predict}") 
# else:
#     predict=False
#     print(f"Il numero inserito {num} è maggiore di 6? {predict}")

# if num < 5:
#     predict=True
#     print(f"Il numero inserito {num} è minore di 5? {predict}") 
# else:
#     predict=False
#     print(f"Il numero inserito {num} è minore di 5? {predict}")

# if num >= 3:
#     predict=True
#     print(f"Il numero inserito {num} è maggiore o uguale a 3? {predict}") 
# else:
#     predict=False
#     print(f"Il numero inserito {num} è maggiore o uguale a 3? {predict}")

# if num <=8:
#     predict=True
#     print(f"Il numero inserito {num} è minore o uguale a 8? {predict}") 
# else:
#     predict=False
#     print(f"Il numero inserito {num} è minore o uguale a 8? {predict}")

# if num > 6 or num <3:
#     predict=True
#     print(f"Il numero inserito {num} è maggiore di 6 o minore di 3? {predict}") 
# else:
#     predict=False
#     print(f"Il numero inserito {num} è maggiore di 6 o minore di 3? {predict}")

# if num > 2 and num <9:
#     predict=True
#     print(f"Il numero inserito {num} è maggire di 2 e minore di 9? {predict}") 
# else:
#     predict=False
#     print(f"Il numero inserito {num} è maggiore di 2 o minore di 9? {predict}")

# if 1 in list_cose:
#     predict=True
#     print(f"Il numero 1 è presente nella lista? {predict}")
# elif 21 not in list_cose:
#     predict=True
#     print(f"Il numero 21 non è presente nella lista? {predict}")


#ESERCIZIO 5.3

# alien_color:str = "green"

# if alien_color == "green":
#     print ("the player just earned 5 points")

# alien_color:str = "yellow"

# if alien_color == "green":
#     print ("the player just earned 5 points")

# #ESERCIZIO 5.4

# alien_color:str = "green"

# if alien_color == "green":
#     print ("the player just earned 5 points")
# else:
#     print ("the player just earned 10 points")

# alien_color:str = "red"

# if alien_color == "green":
#     print ("the player just earned 5 points")
# else:
#     print ("the player just earned 10 points")

# ESERCIZIO 5.5

# alien_color:str = "green"
# if alien_color == "green":
#     print("the player earned 5 points")
# elif alien_color == "yellow":
#     print("The player earned 10 points")
# else:
#     alien_color == "red"
#     print("The player earned 15 points")

# alien_color:str = "yellow"
# if alien_color == "yellow":
#     print("the player earned 5 points")
# elif alien_color == "green":
#     print("The player earned 10 points")
# else:
#     alien_color == "red"
#     print("The player earned 15 points")

# alien_color:str = "red"
# if alien_color == "red":
#     print("the player earned 5 points")
# elif alien_color == "yellow":
#     print("The player earned 10 points")
# else:
#     alien_color == "green"
#     print("The player earned 15 points")

# ESERCIZIO 5.6

# age:int = 21

# if  age < 2:
#     print(" the person is a baby")

# elif age >= 2 and age < 4:
#     print("the person is a toddler")

# elif age >= 4 and age < 13:
#     print("the person is a kid")

# elif age >= 13 and age < 20:
#     print("the person is a teenager")

# elif age >= 20 and age < 65:
#     print("the person is an adult")

# else:
#     print("the person is an elder")

#5.7

# favourite_fruits:list[str] = ["fragola","mela","pesca"]

# if "fragola" in favourite_fruits:
#     print("You really like Fragola!")

# if "mela" in favourite_fruits:
#     print("You really like Apples!")

# if "pesca" in favourite_fruits:
#     print("You really like Peaches!")

# if "banana" in favourite_fruits:
#     pass

# if "pera" in favourite_fruits:
#     pass

# ESRCIZIO 5.8

# username:list[str] = ["Admin","Silvia","Luca","Matteo","Thomas"]
# user:str = input("Log in: ")

# if user=="Admin":
#     print("Hello Admin, would you like to see a status report?")
# if user !="Admin":
#     print(f"Hello {user},thank you for logging in again!")

# ESERCIZIO 5.9

# username:list[str] = []

# if len(username) == 0:
#     print("We need some Users")


