def pretvori_v_slovar(niz):
    slovar = {}
    znaki = list(niz)
    for i in enumerate(znaki):
        slovar[i[0]] = i[1]
    print(slovar)

pretvori_v_slovar("burek 12")