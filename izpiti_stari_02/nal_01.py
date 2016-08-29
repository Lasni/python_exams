def stevilo_pozitivnih(f1):
    count = 0
    lst_of_nums = [float(line.rstrip("\n")) for line in open(f1, "r")]
    for i in lst_of_nums:
        if i > 0:
            count += 1
    print(count)

stevilo_pozitivnih("stevila.txt")
