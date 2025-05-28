
from tipi_di_dato import *
from typing import Self, Any


class Volo:

    codice: str
    durata_minuti: int

    def __init__(self, codice: str, durata_minuti: int) -> None:
        self.codice = codice
        self.durata_minuti = durata_minuti
    
    def __hash__ (self) -> int:
        return hash((self.codice, self.durata_minuti))
    
    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Volo):
            return False
        return self.codice == other.codice and self.durata_minuti == other.durata_minuti
    
    def set_codice(self, codice: str) -> None:
        self.codice = codice
    
    def set_durata_minuti(self, durata_minuti: int) -> None:
        self.durata_minuti = durata_minuti

        if durata_minuti < 0:
            raise ValueError("La durata del volo non può essere negativa.")

    def get_codice(self) -> str:
        return self.codice
    
    def get_durata_minuti(self) -> int:
        return self.durata_minuti
    

class Aereoporto:
    
    _nome: str
    _codice: str

    def _init_(self, nome:str, codice:str) -> None:
        
        self._nome = nome
        self._codice = codice

    def _eq_(self, value)-> bool:
        
        if not isinstance(value, Aereoporto):
            return False
        return self._nome == value._nome and self._codice == value._codice
    
    def _hash_(self) -> int:
        return hash((self._nome, self._codice))
    
    def set_nome(self, nome:str) -> None:
        
        if not self._nome:
            raise ValueError("Nome non può essere vuoto")
        else:
            self._nome = nome

    def set_codice(self, codice:str) -> None:
        
        if not codice:
            raise ValueError("Il codice non può essere vuoto")
        else:
            self._codice = codice

    def get_nome(self) -> str:
            return self._nome
    
    def get_codice(self) -> str:
        return self._codice
    

class Compagnia:

    _nome: str
    _fondazione: int

    def __init__ (self, nome:str, fondazione: int) -> None:
        
        self._nome = nome
        self._fondazione = fondazione

    def __eq__(self, value: Any) -> bool:
        if not isinstance(value, Compagnia):
            return False
        return self._nome == value._nome and self._fondazione == value._fondazione
    
    def __hash__(self) -> int:
        return hash((self._nome, self._fondazione))
    
    def set_nome(self, nome: str) -> None:
        
        if not nome:
            raise ValueError("Il nome della compagnia non può essere vuoto.")
        self._nome = nome

    def set_fondazione(self, fondazione: int) -> None:

        if self._fondazione < 0:
            raise ValueError("L'anno di fondazione non può essere zero o negativo.")
        self._fondazione = fondazione

    def get_nome(self) -> str:
        return self._nome
    
    def get_fondazione(self) -> int:
        return self._fondazione
    

class Città:

    _nome: str
    _numero_abitanti: int

    def __init__(self, nome: str, numero_abitanti: int) -> None:
        self._nome = nome
        self._numero_abitanti = numero_abitanti

    def __eq__(self, value: Any) -> bool:
        if not isinstance(value, Città):
            return False
        return self._nome == value._nome and self._numero_abitanti == value._numero_abitanti
    
    def __hash__(self) -> int:
        return hash((self._nome, self._numero_abitanti))
    
    def set_nome(self, nome: str) -> None:
        if not nome:
            raise ValueError("Il nome della città non può essere vuoto.")
        self._nome = nome

    def set_numero_abitanti(self, numero_abitanti: int) -> None:
        if numero_abitanti < 0:
            raise ValueError("Il numero di abitanti non può essere negativo.")
        self._numero_abitanti = numero_abitanti

    def get_nome(self) -> str:
        return self._nome
    
    def get_numero_abitanti(self) -> int:
        return self._numero_abitanti
    
    

class Nazione:

    _nome: str

    def __init__(self, nome: str) -> None:
        self._nome = nome

    def __eq__(self, value: Any) -> bool:
        
        if not isinstance(value, Nazione):
            return False
        return self._nome == value._nome
    
    def __hash__(self) -> int:
        return hash(self._nome)
    
    def set_nome(self, nome: str) -> None:
        
        if not nome:
            raise ValueError("Il nome della nazione non può essere vuoto.")
        self._nome = nome

    def get_nome(self) -> str:
        return self._nome
