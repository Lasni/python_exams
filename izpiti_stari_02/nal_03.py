class Datum:
    def __init__(self, d, m, l):
        self.d = d
        self.m = m
        self.l = l


    def __str__(self):
        meseci = {1: "januar", 2: "februar", 3:"marec",
                  4:"april", 5:"maj", 6:"junij",
                  7: "julij", 8: "avgust", 9: "september",
                  10:"oktober", 11: "november", 12: "december"}

        return "{}. {}, {}".format(self.d, meseci[self.m], self.l)


datum = Datum(14, 5, 2008)
print(datum)
