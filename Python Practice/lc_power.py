# checks wheather the input number n is a power of 4
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        check = 1
        while n >= check:
            if n == check:
                return True
            check = check * 4
        return False


re = Solution()
va = re.isPowerOfFour(25)
print(va)