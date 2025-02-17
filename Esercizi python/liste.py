
list1 =[1,2,3,4]

print(list1)

print(*list1)   # per stampare gli elementi della lista senza le parentesi

print(*list1, sep= ",")  # per separare gli elemneti della lista con tutto ciò che ho tra ""

print(list1[0])  # serve a stampare l'elemento che nella lista si trova nella posizione 0 ovvero il numero 1

mylist=["Andrea", "Benedetta", "Camilla"]

print(mylist)

# voglio cambiare la posizione del terzo elemento della lista
mylist[2] ="Carlo"
print(mylist) # con questo comando ho cambiato il terzo nome della lista

mylist[-1] ="Hadolf"
print(mylist)

# come aggiungere o rimuovere elementi alla lista

mylist1=["Andrea","Benedetta", "Camilla"]

mylist1.append("Davide")   # con il comando "append" posso aggiungere elementi alla lista
print(mylist1)

mylist1.append("Erald")   # con la funzione append l'elemento verrà aggiunto sempre alla fine della lista
print(mylist1)

mylist1.insert(1, "Andrea2.0")    # con insert posso aggiungere un elemnto alla lista e scegliere anche la posizione
print(mylist1)                    # basta eseguire il comando "list.insert(index, "element")"

mylist1.insert(1, "Andrea_7.0")
print(mylist1)

mylist1.remove("Andrea_7.0")    # per rimuovere un elemento dalla lista si usa il comando remove
print(mylist1)

mylist1.pop(3)    # per togliere elemento nella posizione indicata in questo caso 3
print(mylist1)