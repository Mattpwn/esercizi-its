from pagamento import *

class PagamnetoCartaDiCredito(Pagamento):

    _nomeTitolare: str
    _data_scadenza: str
    _numero_carta: int

    def __init__ (self, importo: float, nomeTitolare: str, data_scadenza:str, numero_carta: int):
        self.setImporto(importo)
        self.setNomeTitolare(nomeTitolare)
        self.setDataScadenza(data_scadenza)
        self.setNumeroCarta(numero_carta)

    def setNomeTitolare(self, nome:str):
        self._nomeTitolare = nome

    def setDataScadenza(self, data:str):
        self._data_scadenza = data

    def setNumeroCarta(self, numero: int):
        self._numero_carta = numero

    def getNomeTitolare(self):
        return self._nomeTitolare
    
    def getDataScadenza(self):
        return self._data_scadenza
    
    def getNumeroCarta(self):
        return self._numero_carta
    

    
if __name__ == "__main__":

    cardPay: PagamnetoCartaDiCredito = PagamnetoCartaDiCredito(2500.00, "Matteo Argenti", "10/29", 1234567890123456)
    print (cardPay.dettagliPagamento())
    print (cardPay.getNomeTitolare())
    print (cardPay.getDataScadenza())
    print (cardPay.getNumeroCarta())