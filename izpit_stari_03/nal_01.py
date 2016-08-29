def znaki(f1):
    lines = [line.strip() for line in open(f1, "r")]
    lst = [len(line) for line in lines]
    print(lst)

znaki("datoteka.txt")
