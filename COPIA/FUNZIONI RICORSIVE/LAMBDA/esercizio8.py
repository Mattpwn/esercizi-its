
# ESERCIZIO 8

studenti: list[dict] = [
    {"nome": "Anna", "media": 28},
    {"nome": "Luca", "media": 25},
    {"nome": "Marco", "media": 30}
]

studenti_sorted : list[dict] = sorted (studenti, key = lambda student : student, reverse = True)

print(studenti_sorted)