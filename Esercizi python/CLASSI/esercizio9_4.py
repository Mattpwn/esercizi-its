
#ESERCIZIO 9.4

class Restaurant:

    def __init__ (self, restaurant_name:str, cusine_type:str):

        self.restaurant_name = restaurant_name
        self.cusine_type = cusine_type
    
    def describe_restaurant(self):

        print(f" {self.restaurant_name} : {self.cusine_type}")  

    def open_restaurant(self):

        print(f" {self.restaurant_name} is open")

ristorante: Restaurant = Restaurant("Schiano", "Pesce")
ristorante.describe_restaurant()
ristorante.open_restaurant()
