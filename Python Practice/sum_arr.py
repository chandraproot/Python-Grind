
# funtion to find the sum of the list


def sum_arr(arr):
    sum = 0
    # arr = [1, 2, 63, 4, 7]
    for i in arr:
        # print(i)
        sum = i + sum
    return sum


my_arr = [1, 2, 63, 4, 7, 45, 21, 96]
result = sum_arr(my_arr)
print(result)
