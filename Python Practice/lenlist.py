list = [8, 9, 11, 6, 7, 6, 23, 56, 6,]


def length(list):
    n = 0
    for i in list:
        n = n + 1
    return n


length = length(list)
print(f"The lenght of the list is {length}")
