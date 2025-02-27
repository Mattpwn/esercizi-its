
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

mammiferi : list = []
rettili : list = []
uccelli : list = []
pesci : list = []

nome_animale : str = str(input(" Inserisci un animale "))

match nome_animale:
    case "cane"|"gatto"|"cavallo"|"elefante"|"leone":
        print(f"{nome_animale} appartiene alla categoria dei mammiferi")

    case "serpente"|"lucertola"| "tartaruga"| "coccodrillo.":
        print(f" {nome_animale} appartiene alla classe dei rettili")

    case "aquila"| "pappagallo"| "gufo"| "falco":
        print(f" {nome_animale} appartiene alla categoria uccelli ")

    case "squalo"| "trota"| "salmone" | "carpa":
        print(f" {nome_animale} appartiene alla categoria pesci")

    case _:
        print(f" Non so dire di che categoria sia {nome_animale}")
