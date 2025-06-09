
#1) Scrivi una funzione che converta una lista di tuple (chiave, valore) in un dizionario. Se
#la chiave è già presente, somma il valore al valore già associato alla chiave.

from typing import Any

def converti (lista:list[tuple]) -> dict:

    dizionario_1 : dict[Any, Any] = {}

    for key, value in lista:

        if key in dizionario_1:

            dizionario_1[key] += value

        else:

            dizionario_1[key] = value

    return dizionario_1

#2) Scrivi una funzione che prenda una lista di numeri e ritorni un dizionario che
#classifichi i numeri in liste separate per numeri positivi e negativi.

def number_list (lista:list[float | int]) -> dict[str, list[int | float]]:  

    dict_1: dict[str, list[int | float]] = {"positivi" : [], "negativi" : []}

    for element in lista:

        if element >= 0:

            dict_1["positivi"].append(element)

        else:

            dict_1["negativi"].append(element)

    return dict_1
            

#3) Scrivi una funzione che accetti un dizionario di prodotti con i relativi prezzi e
#restituisca un nuovo dizionario con solo i prodotti che hanno un prezzo inferiore a 50, ma
#con i prezzi aumentati del 10% e arrotondati a due cifre decimali

def esercizio_3 (dict_3:dict [str, float|int]) -> dict [str, float|int]:
    dict_4:dict [str, float|int] = {}

    for key, value in dict_3.items():
        if value <= 50:
            dict_4[key] = value + (value * 0.1)
        else:
            continue

    return dict_4

#1.1) Scrivi una funzione che verifica se una combinazione di condizioni (X, Y, e Z) è
#soddisfatta per procedere con un'azione. L'azione può procedere solo se la condizione X
#è vera e almeno una tra Y e Z è vera. La funzione deve ritornare "Azione permessa"
#oppure "Azione negata" a seconda delle condizioni che sono soddisfatte

def condizione (X:bool, Y:bool, Z:bool) -> bool:
    if X and (Y or Z):
        return "Azione permessa"
    else:
        return "Azione negata"
    
#2.1) Scrivi una funzione che moltiplica tutti i numeri interi di una lista che sono minori di un
#dato valore intero definito threshold (soglia)

def prodotto (list_3:list [int], threshold:int = 30) -> int:
    prodotto_1:int = 1 

    for element in list_3:
        if element < threshold:
            prodotto_1 *= element

    return prodotto_1

#3.1) 3) Scrivere in Python dei cicli che stampino le seguenti sequenze di valori:
#a) 2, 4, 6, 8, 10, 12, 14
#b) 1, 4, 7, 10, 13
#c) 30, 25, 20, 15, 10, 5, 0
#d) 5, 15, 25, 35, 45       

#esercizio fattoriale

def fattoriale (n:int) -> int:
    if n == 1:
        return 1
    





# esercizio sulle classi

class ContactManager:

    def _init_(self, contacts: dict[str, list[str]] = {}):
        
        self.contacts = contacts

    def create_contact (self, name: str, phone_numbers: list[str]) -> dict[str, list[str]]:
        
        if name in self.contacts:
            raise ValueError ("Errore: il contatto esiste già")
        else:
            self.contacts [name] = phone_numbers

            return {name : phone_numbers} #nuovo dizionario che contiene una chiave sola e un valore solo

    def add_phone_number(self, contact_name: str, phone_number: str) -> dict[str, list[str]]:
        
        if contact_name not in self.contacts:
            raise ValueError ("Errore: il contatto non esiste")
        if phone_number in self.contacts[contact_name]:
            raise ValueError ("Errore: il numero di telefono esiste già")
        
        self.contacts[contact_name].append(phone_number)

        return {contact_name: self.contacts[contact_name]}
    
    def remove_phone_number(self, contact_name: str, phone_number: str) -> dict[str, list[str]]:

        if contact_name not in self.contacts:
            raise ValueError ("Errore: il contatto non esiste")
        if phone_number not in self.contacts[contact_name]:
            raise ValueError ("Errore: il numero di telefono non è presente.") 

        self.contacts[contact_name].remove(phone_number)

        return {contact_name: self.contacts[contact_name]}   

    def update_phone_number(self, contact_name: str, old_phone_number: str,new_phone_number: str) -> dict[str, list[str]]:

        if contact_name not in self.contacts:
            raise ValueError ("Errore: il contatto non esiste")
        if old_phone_number not in self.contacts [contact_name]:
            raise ValueError ("Errore: il numero di telefono non è presente")

        index: int = self.contacts[contact_name].index(old_phone_number)
        self.contacts[contact_name][index] = new_phone_number

        return {contact_name: self.contacts[contact_name]}

    def list_contacts(self) -> list[str]:

        return list(self.contacts.keys())

    def list_phone_numbers(self, contact_name: str) -> list[str]:

        if contact_name not in self.contacts:
            raise ValueError ("Errore: il contatto non esiste")

        return self.contacts[contact_name]

    def search_contact_by_phone_number(self, phone_number: str) -> list[str]:

        contacts_list:list[str] = []

        for contacts, list_contacs in self.contacts.items():
            if phone_number in list_contacs:
                contacts_list.append(contacts)
        if contacts_list == []:
            raise Exception ("Newssun contatto trovato con questo numero di telefono")

        return contacts_list