

lst = []


def arm_strong(ints):
    ori = ints
    st = str(ints)
    for letter in st:
        lst.append(letter)
    for i in range(0, len(lst)):
        lst[i] = int(lst[i])
    # print(lst)
    ln = len(lst)
    # print(type(ln))
    # print(ln)
    sum = 0
    for i in range(0, len(lst)):
        sum = pow(lst[i], ln) + sum
        # print(sum)
    if ori == sum:
        return print("Yes")
    else:
        return print("No")


arm_strong(120)
