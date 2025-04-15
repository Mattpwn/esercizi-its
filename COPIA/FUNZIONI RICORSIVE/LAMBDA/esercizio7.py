
# ESERCIZIO 7

parole = ["cane", "gatto", "elefante", "ratto", "orso"]

parole_4_lettere : list[str] = list(filter(lambda x : len(x) > 4, parole))

print(parole_4_lettere)