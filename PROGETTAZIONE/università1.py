import re
from typing import Self

class CodiceFiscale:

    _cf:str = r"^([A-Z]{6}[0-9LMNPQRSTUV]{2}[ABCDEHLMPRST]{1}[0-9LMNPQRSTUV]{2}[A-Z]{1}[0-9LMNPQRSTUV]{3}[A-Z]{1})$|([0-9]{11})$"

    def __init__ (self, codice) -> None:
        codice = codice.upper()

        if not re.findall (self._cf, codice):
            raise ValueError (f"Codice Fiscale non valido {codice}")
        self._cf = codice

    def cf(self) -> bool:
        return self._cf
    
    def __hash__ (self) -> int:
        return hash(self._cf)
    
    def __str__ (self) -> str:
        return f"Codice Fiscale: {self._cf}"
    

class Iscrizione:

    anno: int

    def __new__ (anno: int|Self) -> Self:

        if anno < 1900:

            raise ValueError(f"l'anno di Iscrizione deve essere maggiore di 1900")
        return int.__new__(anno)
    

class Corso:

    numero_minuti: int

    def __new__ (numero_minuti: int|Self) -> Self:

        if numero_minuti < 1900:

            raise ValueError(f"La lezione deve durare più di 0 minuti")
        return int.__new__(numero_minuti)
