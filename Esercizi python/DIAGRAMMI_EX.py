# DIAGRAMMI 1


# #es1

# import math

# a:float = float (input ("Inserire il valore ipotenusa: "))
# b:float = float (input ("Inserire il valore cateto: "))

# if a > b:
#     c:float = math.sqrt (a*2 + b*2)
#     print (f"Il cateto c vale {c}: ")
# else:
#     print ("errore")

# #es2

# max:int = int (input ("Inserisci valore : "))
# cont:int = 1

# while cont < 4:
#     cont += 1
#     n:int = int (input ("Inserisci valore: "))

# if n > max:
#     max = n
# print (f"Questo è il valore maggiore<: {max}")

# #es3

# sum:int = 0
# cont:int = 1

# while cont <= 5:
#     n:int = int (input (" Inserisci valore: "))
#     if n > 0:
#         sum += n
#     cont += 1
# print (f"La somma dei numeri inseriti è: {sum}")

# #es4

# n:int = int (input (" Inserisci un numero:  "))

# if n % 2 == 0:
#     print (f" Il numero è pari")
# else:
#     print (f" Il numero è dispari")

# #es5

# n:int = int (input(" Inserisci un numero: "))

# if n < 2:
#     print (" Il numero non è primo")
# else:
#     div = 2
# while div < n:
#     if n % div == 0:
#         print (" Il numero non è primo")
#         break
#     else:
#         div += 1
# else:
#     print (" Il numero è primo")        

# #es6

# n:int = int (input (" Inserisci un numero: "))

# if n > 0:
#     fattoriale = 1
#     cont = 1
#     while cont <= n:
#         fattoriale *= cont
#         cont += 1
#     print (f" Il fattoriale di {n} è {fattoriale}")    
# else:
#     print (" Il numero inserito deve essere psotivo")

# #es7

# pari: int = 0
# dispari:int = 0
# cont:int = 1
 
# while cont <= 10:
#     n:int = int (input (" Inserisci un numero: "))
#     cont += 1

#     if n %2 == 0:
#         pari += 1
#     else:
#         dispari += 1

# print (f" I numeri pari sono {pari}")
# print (f" I numeri dispari sono {dispari}")        

# #es8

# soglia:int = int (input (" Inserisci un valore: ") )
# cont:int = 1

# while cont <= 7:
#     n:int = int (input (" Inserisci un valore: "))

#     if n > soglia:
#         print (f" Il numero che supera la soglia è: {n}")
#     cont += 1

# #es9

# nome:str = input(" Inserisci nome: ")
# vendite:int = int (input(" Inserisci valore: "))
# max_nome: str =  nome
# max: int = vendite
# min_nome:str = nome
# min:int = vendite
# cont: int = 1

# while cont != 20:
#     new_nome: str = input (" Inserisci nome:")
#     new_vendite: int = int (input (" Inserisci valore: "))
#     cont += 1

#     if new_vendite > max:
#         max_nome = new_nome
#         max = new_vendite
#         if new_vendite < min:
#             min_nome = new_nome
#             min = new_vendite

# print (max_nome, max)
# print (min_nome, min)

# #es10

# reddito: int = int (input ( "Inserisci valore: "))
# media: int = int ( input ( "Inserisc valore: "))

# if reddito < 20000 and media > 27:
#     print (" Borsa di studio approvata")
# else:
#     print (" Borsa di studio rifiutata")

# #es11

# liberi:int = 20

# while True:
#     opzione:str = input (" Inserisci opzione: ")
#     if opzione == "prenota":
#         if liberi > 0:
#             liberi -= 1
#         else:
#             print (" Non ci sono posti disponibili")
#     elif opzione == "libera":
#         if liberi < 20:
#             liberi += 1
#             print (" Tutti i posti sono già disponibili")
#     elif opzione == "visualizza":
#         print (liberi)
#         print (20 - liberi)
#     elif opzione == "esci":      
#         break
#     else:
#         print (" Errore, inserire una delle opzioni disponibili")


# DIAGRAMMI 2

#es1.2

# posti_max:int = int (input (" Inserisci numero max di posti: "))
# posti_liberi = posti_max

# while True:
#     opzione:str = input (" Inserisci opzione: ")
#     if opzione == "ingresso":
#         if posti_liberi > 0:
#             posti_liberi -= 1
#         else:
#             print (" Il parcheggio è pieno")
#     elif opzione == "uscita":
#         if posti_liberi < posti_max:
#             posti_liberi += 1
#         else:
#             print (" Il parcheggio è già vuoto") 
#     elif opzione == "stato":
#         print (posti_liberi)
#         print (posti_max - posti_liberi)
#     elif opzione == "esci":
#         break
#     else:
#         print (" Errore selezionare una scelta tra quelle disponibili")

# #es2.2

# num_NS:int = int (input (" Inserisci numero veicoli nord-sud: "))
# num_EO = int (input (" Inserisci numero veicoli est-ovest: "))
# soglia:int = int (input (" Inserisci valore: "))
# tempo_priorità:int = int (input (" Inserisci valore: "))

# if num_NS > soglia:
#     if num_EO > soglia:
#         tempo_NS = 50
#         tempo_EQ = 50
#     else:
#         tempo_NS = tempo_priorità
#         tempo_EQ = (100 - tempo_priorità)
#     if num_EO > soglia:
#         tempo_NS = (100 - tempo_priorità)
#         tempo_EQ = tempo_priorità
#     else:
#         veicoli_tot = (num_NS + num_EO)
#         tempo_NS = (num_NS / veicoli_tot) * 100
#         tempo_EQ = (100 - tempo_NS)
# print (tempo_EQ)
# print (tempo_NS) 

# #es3.2

# nome_corso:str = input (" Inserisci il nome del corso: ")
# max_posti:int = 100

# while True:
#     opzione:str = input (" Inserisci opzione: ")
#     if opzione == "iscrivi":
#         if max_posti > 0:
#             max_posti -= 1
#         else:
#             print (" Non ci sono posti disponibili")
#     elif opzione == "annulla":
#         if max_posti < 100:
#             max_posti += 1
#         else:
#             print (" Tutt i posti sono già dispoibile")
#     elif opzione == "visualizza":
#         print ( max_posti)
#         print ( 100 - max_posti)
#     elif opzione == "elimina ":
#         nome_corso:str = input (" Inserisci il nome del corso: ")
#     elif opzione == "esci":
#         break    
                             
# #es4.2

# n_tutor:int = 10
# attesa:int = 0


# es 5.2


# n : int = int(input("Inserisci un numero: "))

# if n %1 == 0 and n > 0:
#     sum : int = 0
#     i = 0

#     while i <= n:

#         sum = (sum + (i * i))
#         i += 1
#     print(f" La somma è {sum}")

# else:
#     print(" Errore il numero deve essere positivo ")

# es 7.2

# somma = 0
# i = 0
# option: str = None
# while True:
#     option = str(input("vuoi inserire un voto ? : "))
#     if option == "no":
#         break
#     if (option != "si") and (option != "no"):
#         print("errore")
#     else:
#         if option == "si":
#             voto = int(input("inserisci voto: "))
#             i+=1
#             somma = somma + voto
#             media = somma / i
# print(media)
    

# es 8.2



