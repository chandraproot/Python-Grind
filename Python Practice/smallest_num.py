
def smallest(my_arr):
    small = my_arr[0]
    for i in my_arr:
        if i < small:
            small = i
    return small


my_arr = [56, 22, 63, 4, 7, 45, 21, 96, 1, -8]
result = smallest(my_arr)
print(result)
