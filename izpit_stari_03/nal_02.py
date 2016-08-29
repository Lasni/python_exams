seznam = ["leto", 2009, "mesec", 1]


def izpisi_seznam(lst):
    for i in lst[::-1]:
        print(lst.index(i), i)

izpisi_seznam(seznam)
