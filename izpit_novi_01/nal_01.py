import math


def average(lst):
    assert len(lst) > 0
    return float(sum(lst)) / len(lst)


def pearson_r(lst1, lst2):
    assert len(lst1) == len(lst2)
    n = len(lst1)
    assert n > 0
    avg_x = average(lst1)
    avg_y = average(lst2)
    diff_prod = 0
    xdiff2 = 0
    ydiff2 = 0

    for i in range(n):
        xdiff = lst1[i] - avg_x
        ydiff = lst2[i] - avg_y

        diff_prod += xdiff * ydiff

        xdiff2 += xdiff * xdiff
        ydiff2 += ydiff * ydiff

    return diff_prod / math.sqrt(xdiff2 * ydiff2)


print(pearson_r([1, 2, 3], [1, 5, 7]))
