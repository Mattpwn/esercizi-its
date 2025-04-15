# Con questo programma printom una persona inesistente  

class Persona:

    def __init__(self):

        self.name = ""
        self.lastname = ""
        self.age = 0

    def displayData(self) -> None:  

        print(f"Nome: {self.name} \nCognome: {self.lastname} \nEtà: {self.age}")

    def setName(self, name:str) -> None:  # funzione usata solamente per far ritornare il nome che inserisco dentro setName

        self.name = name


    def setLastname(self, lastname:str) -> None:  # uso None solo perchè sto impostando l'età

        self.lastname = lastname

    def setAge(self, age:int) -> None:

        if age < 0 or age > 130:

            self.age = 0

        else:

            self.age = age

    def getNome(self) -> str:

        return self.name
    
    def getLastname(self) -> str:

        return self.lastname
    
    def getAge(self) -> int:

        return self.age

# crea un oggetto di tipo persona

ma: Persona = Persona()

# stampa i dati della persona creata 

# imposto il nome di una persona con setName

ma.setName("Matteo")   # andrà a printare il nome che gli ho dato

# imposto il cognome di una persona con setLastname

ma.setLastname("Argenti")

ma.setAge(21)

ma.displayData()

print("----------------")
print(ma.getNome(), ma.getLastname(), ma.getAge())

