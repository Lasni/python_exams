class Nezemljan:
    def __init__(self, ime, velikost, seznam_snovi):
        self.ime = ime
        self.velikost = velikost
        self.seznam_snovi = seznam_snovi

    def __str__(self):
        snovi = {1: "kisik", 2:"dusik", 3:"ogljik"}
        return "{}, {}, {}: {}, {}".format(self.ime, self.velikost,
                                           "snovi", snovi[self.seznam_snovi[0]],
                                           snovi[self.seznam_snovi[1]])


n = Nezemljan("Marsovec", 250, [1, 3])

print(n)