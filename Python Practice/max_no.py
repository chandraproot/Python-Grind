# no2 = input("Enter the second no: ")
# no1 = input("Enter the first no: ")
# no1 = 5
# no2 = 8


def max_num(n1, n2):
    if (n1 > n2):
        return n1
    if (n2 > n1):
        return n2
    else:
        return ("Both numbers are equal")


result = max_num(5, 7)
print(f"The max of the two numbers is {result}")
