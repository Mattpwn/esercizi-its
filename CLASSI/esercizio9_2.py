
#ESERCIZIO 9.2

class Restaurant:

    def __init__ (self, restaurant_name:str, cusine_type:str):

        self.restaurant_name = restaurant_name
        self.cusine_type = cusine_type
    
    def describe_restaurant(self):

        print(f" {self.restaurant_name} : {self.cusine_type}")  

ristorante: Restaurant = Restaurant("Schiano", "Pesce")
ristorante2: Restaurant = Restaurant("Maison Blu", "Pesce")
ristorante3: Restaurant = Restaurant("La Casetta di Campagna", "Carne")
ristorante4: Restaurant = Restaurant("Vesuvio", "Pizza")

ristorante.describe_restaurant()
ristorante2.describe_restaurant()
ristorante3.describe_restaurant()
ristorante4.describe_restaurant()