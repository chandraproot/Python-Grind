# function to find the sum of cube of first N numbers

def sum_cube(n):
    if n < 0:
        print("Incorrect input, Please provide a value greater than 0")
        return False
    else:
        sum = pow((n*(n+1)/2), 2)
    return sum


re = sum_cube(-5)
print(re)

# time complexity O(1)
