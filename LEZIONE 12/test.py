# dal modulo esercizio12_1.py importare la classe MovieCatalog
from esercizio12_1 import MovieCatalog

# creare un oggetto della MovieCatalog

catalog: MovieCatalog = MovieCatalog()

# aggiungiamo un regista e dei film al catalogo

catalog.add_movie('Steven Spielgerg', ['Casper', 'Ritorno al futuro'])

# visualizziamo il catalogo
# print(catalog.getCatalog())

# aggiungere un altro film di steven spielberg al catalogo

catalog.add_movie('Steven Spielger', ['ET'])

# print(catalog.getCatalog())

# aggiungere un nuovo regista

catalog.add_movie('Quentin Tarantino', ['Pulp Fiction','KIll Bill'])

# print(catalog.getCatalog)

# rimuovere ET dal catalogo
catalog.remove_movie('Steven Spielger', 'ET')

print(catalog.getCatalog())

print(catalog.list_directors())