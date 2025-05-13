
class User:

    def __init__ (self, first_name:str, last_name:str, user_age:int, user_email:str ):

        self.first_name = first_name
        self.last_name = last_name
        self.user_age = user_age
        self.user_email = user_email

    def describe_user(self):

        print(f"First name: {self.first_name}\nLast name: {self.last_name}\nAge: {self.user_age}\nEmail: {self.user_email} ")

    def greet_user(self):

        print(f"Bentornato caro utente {self.first_name} {self.last_name}")


ma : User = User ("Matteo", "Argenti", 21, "argenti.m@hotmail.com")
ma.describe_user()
ma.greet_user()