
def binary(arr, num):
    left, right = 0, len(arr) -1
   
    while left <= right:
        mid = int((left + right)/2) 
        # print(arr[mid])
        if arr[mid] == num:
            re = f'The element {num} is found at the index {mid}'
            return mid
        elif arr[mid] > num:
            right = mid -1
        elif arr[mid] < num:
            left = mid + 1
            # print(left)

    return -1


my_array = [1, 2, 4, 6, 9, 10, 13, 16, 17, 19, 20, 23]
num = 15
result = binary(my_array, num)
# print(result)

if result != -1:
    print(f"Element {num} found at index {result}")
else:
    print(f"Element {num} not found in the array")