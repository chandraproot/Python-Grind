
# funtion to find the multiply the all the elements of the list
def multi_arr(arr):
    multi = 1
    # arr = [1, 2, 63, 4, 7]
    for i in arr:
        # print(i)
        multi = i * multi
    return multi


my_arr = [1, 2, 63, 4, 7, 45, 21, 96]
lst = [1, 2, 8, 2, 5]
result = multi_arr(lst)
print(result)
