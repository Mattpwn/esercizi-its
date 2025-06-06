
#importare dal modulo persona.py la classe Persona

from personaNuova import Persona

class Studente (Persona):

    '''
    Attributi della classe Persona (in quanto Studente eredita da Persona)
    self.name: str
    self.lastname: str
    self.age:int

    Attributi della classe Studente
    self.matricola: str
    
    '''

    #inizializzare un oggetto della classe Studente 
    def _init_ (self, name: str, lastname:str, age:int, matricola:str):

        #inizializzare la classe Persona richiamando il metodo init della superclasse
        super()._init_ (name, lastname, age)

        #istruzioni che inizializzano un oggetto della classe Studente
        self.setMatricola (matricola)

    #metodi setter
    
    #metodo che imposta il valore dell'attributo self.matricola
    def setMatricola (self, matricola:str) -> None:
        if matricola:
            self.matricola = matricola
        else:
            print ("Errore! La matricola non può essere rappresentata da una stringa vuota")

    #metodi getter
    
    #metodo che ritorna il valore dell'attributo self.matricola
    def getMatricola(self) -> str:
        return self.matricola            
    
    #ridefinire il metodo _str_
    def _str_(self) -> str:
        return f"\nNome: {self.name}\nCognome: {self.getLastname()}\nMatricola: {self.getMatricola()}"