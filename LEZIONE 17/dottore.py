from persona import Persona
class Dottore(Persona):

    def __init__(self, first_name: str, last_name: str, specialization: str, parcel: float):
        super().__init__(first_name, last_name)
