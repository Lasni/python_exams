some_dict = {"Burek": 2.3, "Slanik": 2, "Krof": 1.90}

loop_bool = True

while loop_bool:
    kljuc = input("Enter a key\n")
    try:
        assert kljuc in some_dict
        loop_bool = False
        print(kljuc, some_dict[kljuc])
    except:
        print("Zapis s tem kljucem ne obstaja.")

