# function to check an element is in a list or not


def check_element(lst, n):

    for i in range(0, len(lst)):
        # print(lst[i])
        # print(n)
        if lst[i] == n:
            return f"Yes, the element {n} is in the list"
    else:

        return f"The element {n} is not in the list"


my_list = [2, 8, 9, 6, 8, 7, 13, 45, 65, 23, 41]
num = 23
re = check_element(my_list, num)
print(re)
