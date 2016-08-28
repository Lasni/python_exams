from datetime import date, timedelta


class Pacient:
    def __init__(self, ime, priimek, r_dan, r_mesec, r_leto):
        self.ime = ime
        self.priimek = priimek
        self.r_dan = r_dan
        self.r_mesec = r_mesec
        self.r_leto = r_leto

    def izracunajStarost(self):
        birth_date = date(self.r_leto, self.r_mesec, self.r_dan)
        today = date.today()
        years_old = (today - birth_date) // timedelta(days=365.2425)
        return years_old

        # krajsa opcija:
        # return today.year - self.r_leto - ((today.month, today.day) < (self.r_mesec, self.r_dan))


x = Pacient("joze", "burek", 30, 8, 1988)
print(x.izracunajStarost())