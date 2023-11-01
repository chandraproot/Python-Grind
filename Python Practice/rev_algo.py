# function for reversal algorithm

def rev_alg(arr, n):
    for i in range(0, len(arr)):
        # print(arr[0])
        # print(len(arr))

        if i < len(arr)-n:
            arr[i] = arr[i + n]
            # return (arr[i])

        elif (i + n >= len(arr)):
            arr[i] = arr[i + n - 13]
    print(arr)


my_list = [8, 9, 5, 6, 3, 12, 7, 4, 16, 11, 10, 21]
n = 1
result = rev_alg(my_list, n)
# print(result)
# print(len(result))
