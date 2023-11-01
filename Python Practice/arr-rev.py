
# funtion to reverse a list
my_arr = [2, 3, 5, 8, 11, 45, 9]


def array(my_arr):
    rev_arr = []
    for i in range(len(my_arr)):
        # print(my_arr[-i - 1])
        rev_arr.append(my_arr[-i - 1])
    return (rev_arr)


re = array(my_arr)
print(re)
