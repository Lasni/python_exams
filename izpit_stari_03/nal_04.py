loop_bool = True


while loop_bool:
    num = input("Enter a number between 0 and 1")

    try:
        float(num)
        x = float(num)
        assert 0.0 <= x <= 1.0
        loop_bool = False
        print("{0:.6f}".format(x))

    except:
        continue