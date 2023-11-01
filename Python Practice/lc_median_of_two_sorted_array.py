from typing import List 

# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         num = nums1 + nums2
#         num.sort()
#         set_num = set(num)
#         list_num = list(set_num)
#         n = len(list_num)
#         print(list_num)
#         print(n)
#         if n % 2 == 0:
#             me = int(n /2) 
#             re = (list_num[me] + list_num[me -1]) / 2
#             return re
#         else:
#             re = int(n // 2)
#             me = list_num[re]
#             return me
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        return 
        
my_list1 = [1, 1]
my_list2 = [1, 2]
obj = Solution()
result = obj.findMedianSortedArrays(my_list1, my_list2)
print(result)