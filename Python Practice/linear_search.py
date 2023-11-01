def lin(arr , n):
    new = []
    for i in range(len(arr)):
        if arr[i] in new:
            if arr[i] == n:
                print("The element is also found at index, ", i)
                return
        if arr[i] == n:
            new.append(i)
            print("The element is found at index", i)
    print(new)
    return
my_arr = [5, 8, 9, 6, 7, 51, 6, 8, 2, 3, 1, 7]
lin(my_arr, 7)
