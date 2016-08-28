def skupniDelitelj(x, y):
    s_d = 1

    if x < y:
        n = x
    else:
        n = y

    for i in range(1, n):
        if x % i == 0 and y % i == 0:
            s_d = i
    return s_d

print(skupniDelitelj(35, 45))

