from persona import Persona

class Paziente(Persona):
    _codice:int
    
    def init(self, first_name, last_name,IdCode:int,age:int):
        super().init(first_name, last_name)
        
        self.setAge(age)
        
        self.setIdCode(IdCode)

    def setIdCode(self,IdCode:int):
        
        self._codice=IdCode

    def getIdCode(self):
        
        return self._codice

    def patientInfo(self):
        print(f"Paziente: {Persona.getName(self)} {Persona.getLastName(self)}\n ID:{self._codice}")
