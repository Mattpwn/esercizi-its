
# m: dict = {"key1" : "Valore1"}  # ogni dizionario ha bisogno di una chiave e un valore
# print(m)

# m: dict = {"key1": {"key1" : "Valore1"}}   # posso aggiungere dizionari dentro altri dizionari e possono avere la stessa chiave

# m: dict = {"key": 5}
# m["key"]  # chiedo quale valore sia associato alla chiave e il programma darà indietro 5

# dichiarazione di un dizionario

m: dict = {"a": 1, "b": 2, "c": 3}
# aggiunta di un elemento al dizionario
m["d"] = 4
print(m)
variabile: int = m["a"]
print(f"{variabile=}")  # con questa scrittura con = finale printa anche il nome "variabile" con =

var: int = m["a"]
print(f"il valore di {var=}")  # con questa scrittura printa sia "il valore di" che "var"

c: dict = {"i": 1, "j": 2, "k": 3}
m["inner"] = c   # con questa scrittura dichiare una chiave inner con valore il dizionario "c" (dizionari annidati)

# come posso vedere il valore associato a k?
 
m["inner"]["k"]  # con questo comando sto entrando nella chiave "inner" successivamente alla chiave "k" printando così il valore 3

m["lista"] = [1, 2, 3, 4, 5]

# come aggiungere un dizionario ad un dizionario

menu: dict = {"menuestivo":{"Pizza": 15, "Pasta": 10, "Insalata": 5}}

# menu["menuestivo"]["Pizza"]

menuinvernale: dict = {"Pizza": 20, "Pasta": 15, "Insalata": 10}
menu["menuinvernale"] = menuinvernale  # ho agginto menuinvernale al dizionario menu ma prima devo dichiararlo come dict (vedi riga 37)
print(menu)

menu["menuestivo"]["Bistecca"] = 25  # con questo comando ho aggiunto "Bistecca" al menuestivo

# come cancellare un elemento da un dizionario

 # menu["menuestivo"].pop("PIzza")   # con ["menuestivo"] mi apre il dizionario interno al menu e toglie il valore pizza
# questa funzione mi restituisce il valore di ciò che ho cancellato quindi se eseguo riga 45 mi trona il prezzo ovvero il valore
prezzo = menu["menuestivo"].pop("Pizza")  # con questa scrittura rimuove sia la chiave "Pizza" che il valore 15 ovvero il prezzo

print(menu)
print(f"{prezzo=}")   # questo codice ti mostra il valore che è stato cancellato dalla funzione pop 

# comme modificare valori gia esistenti nel dizionario?

menu["menuestivo"]["Pasta"] = 35  # per cambiare il valore basta entrare nel dizionario e modificare il valore
# lo stesso passaggio è da usare per il secondo menu basta cambiare il  dizionario
print(menu)  