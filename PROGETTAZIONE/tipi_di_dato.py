
from typing import Self, Any
import re

class CodiceFiscale(str):
    # gli oggetti di questa classe sono stringhe
    #  che rispettano il formato del codice fiscale

    def _new_(cls, cf:str) -> Self:
        cff:str = cf.upper().strip() #rendo la stringa maiuscola e senza spazi iniziali e finali
        if re.fullmatch(r'^[A-Z]{6}\d{2}[A-Z]\d{2}[A-Z]\d{3}[A-Z]$', cff):
            return super()._new_(cls, cf)
        
        raise ValueError (f"La stringa '{cff}' non è un codice fiscale italiano valido")
    
class CAP(str):

    def _new_(cls, cap:str) -> Self:
        if re.fullmatch(r'^\d{5}$', cap):
            return super()._new_(cls, cap)
        
        raise ValueError (f"La stringa '{cap}' non è un CAP italiano valido")    

class RealGEZ(float):
    # tipo di dato specializzato Reale >= 0
    def _new_(cls, v: float|int|str|bool|Self) -> Self:
        n: float = float._new_(cls,v) # prova a converitre

        if n >= 0:
            return n
        
        raise ValueError (f"Il valore {n} è negativo!")

class Valuta(str):
    def _new_(cls, v:str) -> Self:
        if re.fullmatch(r'^[A-Z]{3}$',v):
            return super()._new_(cls, v)
        raise ValueError(f"La stringa {v} non è un codice valuta")

class Denaro:
    # rappresenta il tipo di dato concettuale composto 
    # con i seguenti campi:
    #  -importo: Reale
    #  -valuta: Valuta
    _importo: float
    _valuta: Valuta

    def _init_(self, imp:float, val: Valuta) -> None:
        self._importo = imp
        self._valuta = val

    def importo(self) -> float:
        return self._importo

    def valuta(self) -> Valuta:
        return self._valuta
    
    def _str_(self) -> str:
        return f"{self.importo()} {self.valuta()}"
        
    def _repr_(self) -> str:
        return f"Denaro: {self.importo()} unità di valuta: {self.valuta()}"

    def _hash_(self) -> int:
        return hash ( (self.importo(), self.valuta()))
    
    def _eq_(self, other: Any) -> bool:
        if not isinstance (other, type(self)) or \
            hash(self) != hash(other):
            return False
        return self.importo() == other.importo() and \
            self.valuta() == other.valuta()
    
    def _add_ (self, other: Self) -> Self:
        """Somma self  ad un'altra istanza di Deanro, ma solo se la valuta è la stessa
        Restituisce una nuova istanza di Denaro"""

        if self.valuta() != other.valuta():
            raise ValueError (f"Non posso sommare importi di valute diverse : '{self.valuta} e {other.valuta}")
        
        somma: float = self.importo() + other.importo()
        return Denaro (somma, self.valuta())
    
class FloatDenaro(float):
    _valuta:Valuta
    def _new_(cls, imp:float, val:Valuta) -> Self:
        d = super()._new_(cls, imp)
        
        d._valuta = val
        return d
    
    def importo(self) -> float:
        return self.real
    
    def valuta(self) -> Valuta:
        return self.valuta
    
    def _str_(self) -> str:
        return f"{self.importo()} {self.valuta()}"
        
    def _repr_(self) -> str:
        return f"Denaro: {self.importo()} unità di valuta: {self.valuta()}"

    def _hash_(self) -> int:
        return hash ( (self.importo(), self.valuta()))
    
    def _eq_(self, other: Any) -> bool:
        if not isinstance (other, type(self)) or \
            hash(self) != hash(other):
            return False
        return self.importo() == other.importo() and \
            self.valuta() == other.valuta()
    
    def _add_ (self, other: Self) -> Self:
        """Somma self  ad un'altra istanza di Deanro, ma solo se la valuta è la stessa
        Restituisce una nuova istanza di Denaro"""

        if self.valuta() != other.valuta():
            raise ValueError (f"Non posso sommare importi di valute diverse : '{self.valuta} e {other.valuta}")
        
    def _sub_(self, other: Self) -> Self:
        return self + FloatDenaro(-other, other.valuta())

    
            
class CodiceFiscaleBrutto:
    # gli oggetti di questa classe contengono una stringa
    #  che rispetta il formato del codice fiscale

    cf:str

    def _init_(self, cf:str) -> None:
        cff:str = cf.upper().strip() #rendo la stringa maiuscola e senza spazi iniziali e finali
        if re.fullmatch(r'^[A-Z]{6}\d{2}[A-Z]\d{2}[A-Z]\d{3}[A-Z]$', cff):
            self.cf = cff
        else:
            raise ValueError (f"La stringa '{cff}' non è un codice fiscale italiano valido")
        
class Telefono (str):

    def _new_(cls, telefono: str):

        if re.fullmatch(r"^\+?[1-9][0-9]{7,14}$", telefono):

            return super()._new_(cls, telefono)
        
        else:

            raise Exception("numero di telefono inserito non correttamente")    