
from typing import Self, Any

from enum import *    # per importare StrEnum

class Genere (StrEnum): #  i valori possono essere interpretati sia come numero che come stringa

    uomo = auto()    # auto crea il valore del tipo di dato uomo che è anche una stringa
    donna = auto()

class Continente (StrEnum):

    asia = auto()
    europa = auto()
    america = auto()
    africa =  auto()
    anatrtide = auto()

class Voto (int):

    def __new__ (cls, v:int|float|Self) -> Self:

        if v < 18 or v > 30:

            raise Exception (f"Value v == {v} must be between 18 and 30")
        
        return int .__new__ (cls, v)
    
    def __add__ (self, other: Self) -> Self:

        return (Voto)
    
class Indirizzo:

    _via: str
    _civico : int

    def __init__ (self, via: str, civico: int) -> None:

        self._via = via
        self._civico = civico

    def via(self) -> str:
        return self._via
        
    def civico(self) -> int:
        return self._civico
        
    def __hash__ (self) -> int:
        return hash(self._via, self._civico)
        
    def __eq__ (self, other:Any) -> bool:
            
        if other is None or \
                not isinstance (other, type(self)) or \
                hash(self) != hash(other):
            return False
        return self._via == other._via and self._civico == other._civico    

        
