# Funtion to find the largest element in an array

def largest(arr):
    max = arr[0]
    for i in arr:
        if i > max:
            max = i
    return max


my_arr = [4, 5, 89, 2, 64, 96, 102, 54, 1000, 5005]
re = largest(my_arr)
print(re)

# time complexity O(n)
# Auxiliary space O(1)
