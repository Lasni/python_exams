class Matrika:
    def __init__(self, sez_matrike):
        self.matrika = sez_matrike

    def zapisi(self, f):
        self.f = f
        assert isinstance(f, str)
        outfile = open(f, "a")
        for row in self.matrika:
            for token in row:
                outfile.write(str(token) + "\t")
            outfile.write("\n")


m = Matrika([[1,2,3],[4,5,6]])

m.zapisi("matrika.txt")
