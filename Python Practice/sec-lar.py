# funtion to find the second largest number in a list
def largest(arr):
    max = arr[0]
    for i in arr:
        if i > max:
            max = i
    lar = arr.index(max)
    sec = arr.pop(lar)
    nw_arr = arr
    # print(nw_arr)
    # print(sec)
    # print(max)
    # print(lar)
    mx = nw_arr[0]
    for i in nw_arr:
        if i > mx:
            mx = i
    return mx


my_arr = [4, 5, 89, 2, 64, 96, 102, 54, 5005, 100]
re = largest(my_arr)
print(re)
