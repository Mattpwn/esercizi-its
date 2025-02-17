
# lista4 = [i for i in range(10)]
# for numero in lista4:
#     print(numero)

# lista2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

lista3 = ["a", "b", "c"]
lista1 = [1, 2, 3]
# prodotto cartesiiano di due liste
#  abbiamo creato una matrice 3 per 3
for lettera in lista3:
   for numero in lista1:   # sto annidando un for all'interno di un for
       print(lettera, numero)    # per far stampare le lettere insiene ai numeri 

L = [[("a",1), ("a",2), ("a",3)], [("b",1), ("b",2), ("b",3)], [("c",1), ("c",2), ("c",3)]]

for i in range (len(lista3)):
    for j in range (len(lista1)):   # con questo programma ho creato una matrice e sto prendendo i suoi elementi uno ad uno in base alle coordinate i e j
        print(L[0][0])

for i in range(3):
    for j in range(3):    # un'altro modo di scrivere ciò che si trova nelle righe precedenti
        print(L[1][2])
# questo  programma printera la risposta 9 volte perchè la matrice creata è 3 per 3

for i in range(3):
    for j in range(3):
        if(L[i][j][1]%2) == 0:   # %2 sarebbe il  modulo e serve a verificare che il numero sia pari
            print(L[i][j])

for num in lista1:
    if num %2 == 0:   # per vedere quale nummero sia pari all'interno della lista1
        print(num)



lista5 = [i for i in range(10)]   # un modo per creare una lista di elementi ordinati da 0 al numero nel range
print(lista5) 

lista6 = [i for i in range(0, 10, 2)] # questa linea di codice crea un lista da 0 a 10 con step 2 ovvero che va di due in due 
print(lista6)