
class Persona:
    '''
    di una persona dobbiamo sapere delle informazioni.'
    queste informazioni vengono chiamati attributi (della classe Persona)
    Le informazioni saranno:
    - nome
    - cognome
    - età

    come li rappresento in python?

    self.name: str (attributo di tipo stringa)
    self.lastname: str (attributo di tipo stringa)
    self.age: int (attributo di tipo integer)

    '''

    # costruttore della classe Persona
    # senza init non posso creare una variabile del tipo della classe (in questo caso Persona)
    # init --> costruttore
    #   SELF indica che init è una funzione che corrisponde alla classe (in questo caso Persona)

    def __init__(self, name:str, lastname:str, age:int):

        self.name = name 
        self.lastname = lastname
        self.age = age

    # funzione che mostri in output tutti i dati di una persona

    def displayData(self) -> None:  # con il None vuole dire che il tipo è non e non restituisce nulla

        print(f"Nome: {self.name} \nCognome: {self.lastname} \nEtà: {self.age}")

        
ma:Persona = Persona("Matteo", "Argenti", 21)       # in questo modo restituisce la posizione in memoria del dato

# utilizzo il ma.Persona perchè adesso la variabile è di tipo Persona --> ma viene chiamata istanza della classe Persona

print(ma)

# mostra i dati di una persona

ma.displayData()    

