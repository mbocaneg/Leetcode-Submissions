class Solution:
    def plusOne(self, digits):

        carry = 1

        for i in range(len(digits)-1, -1, -1):
            sum = digits[i] + carry
            carry = 1 if sum > 9 else 0
            digits[i] = sum % 10

        if carry > 0:
            digits.insert(0, 1)
        
        return digits


sol = Solution()
print(sol.plusOne([9]))
# print(sol.plusOne([9, 9]))