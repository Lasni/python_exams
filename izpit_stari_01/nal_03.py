class WrongInputException(Exception):
    def __init__(self):
        print("Error")


class Izdelek:
    def __init__(self, ime, cena):
        if isinstance(cena, float) and cena > 0:
            self.cena = cena
            self.ime = ime
        else:
            raise WrongInputException

    def izpis(self):
        print("Izdelek: {}. Cena: {} €.".format(self.ime, self.cena))


try:
    x = Izdelek("burek", 0.1)
    x.izpis()
except:
    WrongInputException
