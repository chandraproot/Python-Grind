
# def even_num(lst):
#     lst2 = []
#     for i in lst:
#         if i % 2 == 0:
#             lst2.append(i)
#     return lst2


# my_list = [2, 3, 8, 9, 12, 5, 6, 13, 1]
# num = 3
# re = even_num(my_list)
# print(re)


# Python program to print even Numbers in a List

# Initializing list
list1 = [10, 21, 4, 45, 66, 93]

# using list comprehension
even_nos = [num for num in list1 if num % 2 == 0]

print("Even numbers in the list: ", even_nos)
