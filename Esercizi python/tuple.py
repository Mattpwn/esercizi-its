
tupla: tuple = (1, 2, 3,)  # una volta scritta la tupla non posso aggiungere altri elementi 
print(tupla)

# per cancellare la tupla basta usare il comando del 

# la scrittura "tupla[0]" può essere usata solo come lettura ma non per aggiuingere qualcosa 

tuple[0]
print(tupla[0])

# posso contare gli elementi all'interno della tupla con il comando ".count"

tupla.count(4)  # darà zero perchè nessun elemento chiamato 4 è all'interno della tupla 

tupla.index(2)  # ti printa ciò che si trova in posizione 2 all'interno della tupla