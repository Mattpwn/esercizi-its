mydict:dict = {"key1":"value1","key2":"value2"}

for key in mydict:
    print(key)       # printa solamnete le chiavi

for key in mydict:
    print(mydict[key])

for keys, values in mydict.items():       # questa funzione ti crea una lista di tuple dove ogni tupla ha come elemento chiave e valore corrispondente
    print(f"chiave:{keys}, valore: {values}")

for value in mydict.values():
    print(value)       # printa solo i valori del dizionario

for key in mydict.keys():
    print(key)          # printa solo le chiavi del dizionario

#  ESTENSIONE DELLA LISTA

firstlst : list[int] = [1,5,7,8]
secondlst : list[int] = [2,3,7,6]

firstlst.extend(secondlst)
print(firstlst)

#OR

thirdlst : list[int] = firstlst + secondlst
print(thirdlst)

firstlst = [1,2,3,4,5]



