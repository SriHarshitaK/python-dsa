class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        original = x
        reverse = 0

        while x > 0:
            digit = x % 10
            reverse = reverse * 10 + digit
            x = x // 10

        return original == reverse
        # if x < 0: return False
        # div = 1
        # while x >= 10 * div:
        #     div *= 10
        # while x:
        #     right = x % 10
        #     left = x//div
        #     if left != right: return False
        #     x = (x % div) // 10
        #     div = div / 100
        # return True