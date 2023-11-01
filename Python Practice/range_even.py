# funtion to print all even numbers in a range

def range_even(n, m):
    lst2 = []
    if n < m:
        for i in range(n, m):
            if i % 2 == 0:
                lst2.append(i)
    elif m < n:
        for i in range(m, n):
            if i % 2 == 0:
                lst2.append(i)
    elif n == m:
        return f"No even numbers exits between the two numbers"

    return lst2


# my_list = [8, 14, 13, 5, 6, 4, 45, 13, 15, 96, 4, 41]
n = 450
m = 45

result = range_even(n, m)
print(result)
