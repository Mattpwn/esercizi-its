name:str = "Matteo"
age:int = 21

# concatenazione
print("Ciao! io sono "  + name + "! Ho" +  str(age) + " anni!")   # da errore perchè age è una stringa cambiamo age in --> str(age)

# nella creazione di una variabile sempre dichiarare il tipo 
''' esempio cambio variabile
print(type(age))
print(type(str(age)))  # il valore di age resterà sempre int perchè ho solamente cambiato il valore nel print non il valore iniziale 
print(type(age))

age = str(age)   # ora ha cambiato valore perchè ho cambiato il suo valore iniziale
print(type(age))
'''

# output formattato
print(f"Ciao! Io sono {name}! Ho {age} anni!")


''' esempio per accorciare numeri con la virgola
pi: float = 3.14159265359
print(f"P Greco vale: {pi}") # con questo valore stampa solamente ciò che ho scritto sopra

# scriviamo p greco con 2 cifre decimali 
print(f"P Greco vale: {pi:.2f}")  # :.2f è il comando per scriverlo con due cifre decimali

# scriviamo p greco con 3 decimali 
print(f"P Greco vale: {pi:.3f}") # :.3f lo faà scrivere  con tre cifre decimali
# queste due scritture del numero arrotondano per difetto o eccesso ciò che c'è dietro la virgola
'''

# output caratteri escape 

print(f"Ciao! Io sono  {name}!\nHo {age} anni!") # \n serve solo per scrivere ciò che segue sulla riga sotto

# come inserire virgolette nell'output 

print(" sei \"bellissimo!\"")

