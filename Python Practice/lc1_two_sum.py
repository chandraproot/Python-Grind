# program to find to sum in a array and return index of the numbers
#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.


# Brute force approach
# class Solution:
#     def twoSum(self, nums, target):
#         new = []
#         for i in nums:
#             for j in nums:
#                 if i != j and i + j == target:
#                     a = nums.index(i)
#                     b = nums.index(j)
#                     new.append(a)
#                     new.append(b)
#                     return new

class Solution:
    def twoSum(self, nums, target):
        preVMap = {} # index : value
        for i, n in enumerate(nums):
            diff = target - n
            if diff in preVMap:
                return [preVMap[diff], i]
            preVMap[n] = i
            print(preVMap)
        return


    
my_list = [8,7,11,15,2]
# my_list = [3,3]
# my_list = [3,2,4]
n = 9
obj = Solution()
va = obj.twoSum(my_list, n)
print(va)

#This algorithm has a time complexity of O(n) because it only needs to iterate through the nums list once, and the dictionary operations (lookups and insertions) have an average time complexity of O(1)