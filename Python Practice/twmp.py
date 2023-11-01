# string = "This is the string to be reversed"

# lenght = len(string)
# print("The length of the string is: ", lenght)

str = input("Enter the string: ")
str2 = "BanBanjara has the right to terminate this agreement at any point if it observes unsatisfactory performance. Only a one week notice would be served during this period."


def leng(str):
    n = 0
    for i in str:
        n = n + 1
    return n


leng(str)
print(leng(str))
