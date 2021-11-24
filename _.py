from PyQt5.QtCore import endl


l = [["s", "a", "d"], ["3", "4", "5"], ["s", "a", "d"]]


def add(a, c, d):
    return a, c, d


print([print(*i, end="\n") for i in l], end="\n")
