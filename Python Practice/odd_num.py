# funtion to find odd numbers in a list

# def odd_num(lst):
#     lst2 = []
#     for i in lst:
#         if i % 2 != 0:
#             lst2.append(i)
#     return lst2

# 2nd funtion

def odd_num1(number):
    return number % 2 == 1


def print_odd(numbers):
    odd_num = list(filter(odd_num1, numbers))
    return odd_num


my_list = [8, 9, 12, 4, 26, 45, 12, 3, 7, 8, 8, 13]
numbers = [8, 9, 12, 4, 26, 45, 12, 3, 7, 8, 8, 13]
# re = odd_num1(my_list)
re = print_odd(numbers)
print(re)
