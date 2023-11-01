# def smallest(lst):
#     small =lst[0]
#     for i in lst:
#         if i < small:
#             small = i
       
#     return small
my_list = [2, 5, 8, 1, -1, 10, 6]
# res = smallest(my_list)
# print(res)

my_list.sort()
# print(my_list)
print("Smallest", min(my_list))