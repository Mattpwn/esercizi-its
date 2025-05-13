# ESERCIZIO 1.1

# x: float = 2.36

# y: float = 1.0 / x

# print(x)
# print(y)

# prodotto: float = x * y

# print(prodotto)

# print(prodotto -x)

# # ESERCIZIO 1.2

# x: float = 3.56   # x: float = -3.56

# y: float = x % 2.0

# print(x)
# print(y)

# # ESERCIZIO 1.3

# x: int = 3
# y: int = 54
# z: int = 70

# sum = x + y + z
# media: float = sum / 3
# print(media)

# ESERCIZIO 1.4

# numero: int = (input("inserire numero a 4 cifre"))

# for i in numero:
#     print(i)

# ESERCIZIO 1.5

# gradiF = int (input("inserisci temperatura in F "))

# gradiCelsius: float = 5 * (gradiF - 32) / 9

# print(f"In gradi Celsius il risultato è {gradiCelsius: .1f}°")

# ESERCIZIO 1.6

menu: dict = {"Pizza": 9.00, "Pasta": 10.50, "Zuppa": 7.00, "Hamburger": 15.50, "Cotoletta": 10.00, "Salmone": 20.20, "Patatine Fritte": 5.50, "Patate al forno": 5.50, "Verdura del giorno": 7.00, "Cheesecake": 6.00, "Tiramisù": 6.00, "Focaccia con nutella": 6.00, "Coca": 3.50, "Acqua": 1.50, "Vino": 5.00}

ordine: dict = {"Pizza", "Hamburger", "Patate al forno", "Tiramisù", "Coca"}

prezzo_pizza = menu["Pizza"]
prezzo_hamburger = menu["Hamburger"]
prezzo_patate = menu["Patate al forno"]
prezzo_tiramisù = menu["Tiramisù"]
prezzo_coca = menu["Coca"]

totale = prezzo_pizza + prezzo_hamburger + prezzo_patate + prezzo_tiramisù + prezzo_coca

print(totale)
