# lst = []


# def find_all_prime(x, y):
#     for j in range(x, y):
#         for i in range(2, y):

#             if j % i != 0 and j % j == 0:
#                 lst.append(j)

#         return lst


# pr = find_all_prime(4, 9)
# print(pr)

# x = 3 % 2
# print(x)
# Python program to print all
# prime number in an interval

def prime(x, y):
    prime_list = []
    for i in range(x, y):
        if i == 0 or i == 1:
            continue
        else:
            for j in range(2, int(i/2)+1):
                if i % j == 0:
                    break
            else:
                prime_list.append(i)
    return prime_list


# Driver program
starting_range = 5
ending_range = 19
lst = prime(starting_range, ending_range)
if len(lst) == 0:
    print("There are no prime numbers in this range")
else:
    print("The prime numbers in this range are: ", lst)
