
# function to find the sum of first n natural numbers
def n_sum(n):
    sum = 0
    for i in range(1, n+1):
        sum = i*i + sum
    return sum


# Sum of first N natural numbers
su = n_sum(5)
print(su)
