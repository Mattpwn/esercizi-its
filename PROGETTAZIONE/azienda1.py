from tipi_di_dato import RealGEZ, Telefono
from datetime import date
from progg1 import Indirizzo

class Impiegato:

    _nome: str
    _cognome: str
    _stipendio: RealGEZ
    _nascita: date

    def set_nome(self, nome:str) ->None:
        self._nome = nome

    def set_cognome(self, cognome:str) ->None:
        self._cognome = cognome

    def set_stipendio(self, stipendio:RealGEZ) -> None:
        self._stipendio = stipendio


    def __init__ (self, nome:str, cognome:str, nascita:date, stipendio:RealGEZ):

        self.set_nome(nome)
        self.set_cognome(cognome)
        self._nascita:date = nascita
        self.set_stipendio(stipendio) 


    def nome(self) -> str:
        return self._nome
    
    def cognome (self) -> str:
        return self._cognome
    
    def nascita (self) -> date:
        return self._nascita
    
    def stipendio (self) -> RealGEZ:
        return self._stipendio
    

class Dipartimento:

    _nome: str
    _telefono: Telefono
    _indirizzo: Indirizzo


    def init(self, nome: str, telefono: Telefono, indirizzo: Indirizzo):
        self._nome = nome
        self._telefono:Telefono = telefono
        self._indirizzo = Indirizzo
    
    def set_nome(self, nome) -> None:
        self._nome = nome
    
    def set_telefono(self, telefono) -> None:
        self._telefono = telefono
    
    def set_indirizzo(self, indirizzo: Indirizzo) -> None:
        self._indirizzo = indirizzo

    def get_nome(self) -> str:
        return self._nome
    
    def get_telefono(self) -> Telefono:
        return self._telefono
    
    def get_indirizzo(self) -> Indirizzo:
        return self._indirizzo

    


class Progetto:

    _nome: str
    _budget: RealGEZ

    def init(self, nome: str, budget: RealGEZ):
        self._nome = nome
        self._budget = budget

    def set_nome(self, nome: str) -> None:
        self._nome = nome

    def set_budget(self, budget: RealGEZ) -> None:
        self._budget = budget

    def get_nome(self) -> str:
        return self._nome

    def get_budget(self) -> RealGEZ:
        return self._budget

    

class Afferenza:

    def init(self, data_afferenza: date):
        self._data_afferenza:date = data_afferenza

    def set_data_afferenza(self, data) -> None:
        self._data_afferenza = data
        
    def get_data_afferenza(self) -> date:
        return self._data_afferenza

