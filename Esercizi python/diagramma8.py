# DIAGRAMMA 8

# A = int(input("Inserire A: ")) # Read A
# B = int(input("Inserire B: ")) # Read B

# if A % 1 == 0 and B % 1 == 0 and 0 < A < B:
#     somma = 0
#     # con il ciclo while
#     x = A
#     while x <= B:
#         somma += x
#         x += 1
#     print(f"il risultato della somma dei valori tra {A} e {B} è {somma}")


# else:
#     print(f"Errore: i valori A={A} e B={B} non sono validi")

# con il for sarebbe 

# for n in range(A, B + 1):
#     somma += n
# print(f"il risultato è {somma}")

# # bonus trick

# somma = sum(range(A, B + 1))

# DIAGRAMA 9

num_div = 0 
inseriti = 0 

n = int(input("Inserisci un divisore positivo: "))

if n > 0:
    continua = True

    while continua and inseriti < 10:
        num = int(input("Inserisci un valore: "))
        inseriti += 1

        if num % n == 0:
            num_div += 1

        inseriti += 1

        scelta = input("Vuoi continuare: ")
        if scelta.lower() == "no":
            continua = False

    # fine del while
    print(f"Hai inserito {num_div} numeri divisibili per {n}: ")       
        
        