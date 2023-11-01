# FUNCTOINO TO FIND N LARGEST NUMBERS IN A STRING

def n_largest(lst, n):
    # lst_n = sorted(lst, reverse=True)
    lst.sort()
    return lst[-n:]


my_list = [2, 3, 8, 9, 12, 5, 6, 13, 1]
num = 3
re = n_largest(my_list, num)
print(re)

# er = my_list.sort(reverse=False)
# print(my_list)
