class Solution:
    # def isPalindromeNaive(self, x):
    #     orig = x
    #     rev = 0

    #     while x > 0:
    #         rev = rev * 10 + x%10
    #         x = x // 10

    #     if rev == orig:
    #         return True
    #     else:
    #         return False

    def isPalindrome(self, x):

        if x == 0:
            return True

        if x < 0 or x%10 == 0:
            return False

        rev = 0

        while x > rev:
            rev = rev * 10 + x %10
            x = x // 10

        return x == rev or x == rev // 10


sol = Solution()
print(sol.isPalindrome(1234))
print(sol.isPalindrome(1221))
print(sol.isPalindrome(141))
