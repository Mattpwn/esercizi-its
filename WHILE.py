
contatore: int = 0

while contatore < 10:
    print(contatore)
    contatore += 1      # quesste operazioni andranno avanti aumentando di 1 in 1 fino a quando contatore < 10

# una volta arrivato a 10 il while diventerà falso uscendo così dai passaggi sotto terminando il programma

lista_1: list = [1, 2, 3, 4, 5]  # possiamo anche scorrere una lista usando il while


while contatore < len(lista_1):
    print(lista_1[contatore])
    contatore += 1      # questo programma andrà avanti fino alla fine della lista 
# quando il contatore raggiungerà la fine della lista uscirà dal programma


password: dict = {"Matteo" : "12345"}

nome_utente: str = input("inserisci il nome utente: ")
password: str = password[nome_utente]

while True:
    b = input("inserisci la password")
    if b == password:
        print("Password corretta")
        break
    else:
        print("Password errata")
pass


import time    # TIMER

second: int = 10 

while second > 0:

    print(f"Mancano {second} secondi")
    time.sleep(-1)
    second =  1

for i in range(10):   

    if i == 5:
        continue
    print(i)

if True:
    pass
else:
    pass 


