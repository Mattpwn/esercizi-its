class Persona:

    _first_name: str
    _last_name: str
    _age: int

    def __init__ (self,first_name: str, last_name: str):

        if isinstance ( first_name, str):

            self._first_name = first_name

        else:
            print ("il nome inserito non è una stringa")

            self._first_name = None

        if isinstance (last_name, str):

            self._last_name = last_name

        else:
            print ("il cognome inserito non è una stringa")

            self._last_name = None

        if isinstance (first_name, str) and isinstance (last_name, str):

            self._age = 0

        else: 
            self._age = None

    def setName (self, first_name: str):
          
        if isinstance ( first_name, str):

            self._first_name = first_name
        
        else:
            print("il nome inserito non è una stringa")
        
    def setLastName (self, last_name: str):

        if isinstance (last_name, str):

            self._last_name = last_name

        else:
            print ("il cognome inserito non è una stringa")

    def setAge (self, age: int):

        if isinstance ( age, int):

            self._age = age
        
        else: 
            print("L'età deve essere un numero intero")

    def getName(self):

        return self._first_name
    
    def getLastName (self):

        return self._last_name
    
    def getAge (self):

        return self._age
    
    def greet(self):

        print(f"Ciao sono {self._first_name} {self._last_name}! Ho {self._age} anni!")


if __name__ == "__main__":

    persona: Persona = Persona ("Matteo", "Argenti") # per verificare se il programma funzione

    persona.greet()