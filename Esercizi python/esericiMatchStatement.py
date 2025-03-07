
# n : int = int(input("Inserisci il numero di neonati: "))

# match n:

#     case 1:
#         print("Congratulazioni!!")

#     case 2:
#         print("Wow Gemelli!! ")

#     case 3:
#         print("Wow! Tre! ")

#     case 4:
#         print("Mamma mia! Quattro! Wow! ")

#     case 5:
#         print("Incredibile! Cinque! ")

#     case _:
#         print("Non ci credo!")


# ESERCIZIO 2

# nome : str = str(input("Inserisci il tuo nome: "))

# gender: str = str(input("Inserisciil tuo gender: "))

# match gender:

#     case "m":
#         print(f"  nome: {nome}  Gender: {gender}:")

#     case "f":
#         print(f" nome: {nome}  gender: {gender}")

#     case _:
#         print(f" Mi dispiace {nome} ma non è possibile stampare un documento valido")

# ESERCIZIO 3

# voto : int = int(input("Inserisci il tuo voto: "))

# match voto:

#     case 10:
#         print("Eccellente!")

#     case 8|9:
#         print("Molto buono ")

#     case 6|7:
#         print("Sufficiente ")

#     case 4|5:
#         print("Insufficinte")

#     case 1|2|3:
#         print("Gravemente insufficiente ")

#     case _:
#         print("Voto non valido ")

# ESERCIZIO 4


# n:int = int(input("Inserisci il voto: "))
# match n:
#     case 106|107|108|109|110:
#         print("GPA 4.0")
#     case 101|102|103|104|105: 
#         print("GPA 3.7")
#     case 96|97|98|99|100:
#         print("GPA 3.3")
#     case 91|92|93|94|95:
#         print("GPA 3.0")
#     case 86|87|88|89|90:
#         print("GPA 2.7")
#     case 81|82|83|84|85:
#         print("GPA 2.3")
#     case 76|77|78|79|80:
#         print("GPA 2.0")
#     case 70|71|72|73|74|75:
#         print("GPA 1.7")
#     case 66|67|68|69:
#         print("GPA 1.0")
#     case _:
#         print("Voto non valido")
        

#   ESERCIZIO 5


# oggetti : list = []

# for i in range (3):
#     lista: str = input(f"Inserisci oggetti: ")
#     oggetti.append(lista)

# match oggetti:
    
#     case ["Computer, Telefono, Tablet"]:
#         print("Dispositivi  elettronici")
    
#     case ["penna", "matita", "quaderno"]:
#         print("Materiale scolastico")

#     case ["pane", "latte", "uova"]:
#         print("Prodotti alimentari")

#     case ["sedia", "tavolo", "armadio"]:
#         print("Mobili")

#     case _:
#         print("Categoria sconosciuta")


# ESERCIZIO 6

# mammiferi : list = []
# rettili : list = []
# uccelli : list = []
# pesci : list = []

# nome_animale : str = str(input(" Inserisci un animale "))

# match nome_animale:
#     case "cane"|"gatto"|"cavallo"|"elefante"|"leone":
#         print(f"{nome_animale} appartiene alla categoria dei mammiferi")

#     case "serpente"|"lucertola"| "tartaruga"| "coccodrillo.":
#         print(f" {nome_animale} appartiene alla classe dei rettili")

#     case "aquila"| "pappagallo"| "gufo"| "falco":
#         print(f" {nome_animale} appartiene alla categoria uccelli ")

#     case "squalo"| "trota"| "salmone" | "carpa":
#         print(f" {nome_animale} appartiene alla categoria pesci")

#     case _:
#         print(f" Non so dire di che categoria sia {nome_animale}")

# ESERCIZIO 7

# ruoli : dict [str , int ] = {"nome": input("Inserisci nome utente: ") , "ruolo": input("Inserire il ruolo dell'utente: ") , "età" : int (input("Inserire età dell'utente: "))}

# match ruoli:

#     case {"nome" : name, "ruolo" : "Admin"}:
#         print("Accesso completo a tutte le funzionalità")

#     case {"nome" : name, "ruolo" : "Moderatore"}:
#         print("Può gestire i contenuti ma non modificare le impostazioni")

#     case {"nome" : name, "ruolo" : "Adulto", "età" : età} if età >= 18:
#         print("Accesso standard a tutti i servizi")

#     case {"nome" : name, "ruolo" : "Minorenne", "età" : età} if età < 18:
#         print("Accesso limitato! Alcune funzionalità sono bloccate")

#     case {"nome" : nome, "ruolo" : "Ospite"}:
#         print("Accesso ristretto! Solo visualizzazione dei contenuti")

#     case _:
#         print("Attenzione! Ruolo non riconsciuto! Accesso Negato!")


# ESERCIZIO 8

# from typing import Any
# habitat : list = ["terra", "acqua", "aria"]
# nome_animale : str = str(input(" Inserisci un animale "))
# animal_type : str

# animalDict : dict[str , Any] = {"animale": nome_animale, "tipo" : animal_type, "habitat" : habitat}

# match animalDict:
    


# ESERCIZIO 9

# i = 0
# countTesta: int = 0
# countCroce: int = 0
# while i < 8:

#     lancio : str = input("Inserisci il simbolo che è uscito: T o C: ")
    

#     match lancio:
#         case lancio if lancio == "t" or lancio == "T":
#             countTesta += 1

#         case lancio if lancio == "c" or lancio == "C":
#             countCroce += 1

#         case _:
#             print("Non sono stati fatti lanci: ")
#     i += 1 

# print(f"Il totale delle teste è {countTesta} mentre la percentuale è {(countTesta *100)/i:.2f}%")
# print(f"Il totale delle croci è {countCroce} mentre la percentuale è {(countCroce *100)/i:.2f}%")


# ESERCIZIO 10

# frase:str = input("Inserisci un frase: ")

# match frase:
#     case frase if len(frase)%2==0 and frase[-1]=="?":
#         print("Si")
#     case frase if len(frase)%2==1 and frase[-1]=="?":
#         print("No")
#     case frase if frase[-1]=="!":
#         print("Wow!")
#     case _:
#         print(f"Tu dici {frase}")


# ESERCIZIO 3C-9

# point_x : int = int (input("Inserire coordinata x: "))
# point_y : int = int (input("Inserire coordinata y: "))

# coordinate : tuple = (point_x, point_y)

# match coordinate:

#     case coordinate if coordinate == (0 , 0):
#         print(f"Il punto si trova nell'origine. ")

#     case coordinate if coordinate == (point_x, 0):
#         print(f"Il punto si trova sull'asse x. ")

#     case coordinate if coordinate == (0, point_y):
#         print(f"Il punto si trova nell'asse y. ")

#     case coordinate if point_x > 0 and point_y > 0:
#         print (f" Il punto si trova nel primo quadrante")   
    
#     case coordinate if point_x < 0 and point_y > 0:
#         print (f" Il punto si trova nel secondo quadrante")
    
#     case coordinate if point_x < 0 and point_y < 0:
#         print (f" Il punto si trova nel terzo quadrante")
    
#     case coordinate if point_x > 0 and point_y < 0:
#         print (f" Il punto si trova nel quarto quadrante")


# ESERCIZIO 3C-10


# day:int = int (input (f" Inserire il giorno: "))
# month:int = int (input (f" Inserire il mese: "))

# date:tuple = (day, month)

# match date:
#     case (1, 1):
#         print (f" Il 1/1 è Capodanno")
#     case (14, 2):
#         print (f" Il 14/02 è San Valentino")
#     case (2, 6):
#         print (f" Il 2/6 è la Festa della Repubblica Italiana")
#     case (15, 8):
#         print (f" Il 15/8 è Ferragosto")
#     case (31, 10):
#         print (f" Il 31/10 è Halloween")
#     case (25, 12):
#         print (f" Il 25/12 è Natale")
#     case _:
#         print (f" Nessuna festività importante in questa data")
