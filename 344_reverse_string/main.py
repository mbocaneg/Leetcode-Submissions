class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """

        if s == "":
            return
        
        i = 0
        j = len(s) - 1

        while j > i:
            temp = s[j]
            s[j] = s[i]
            s[i] = temp
            i += 1
            j -= 1

str = ["h","e","l","l","o"]
sol = Solution().reverseString(str)

for c in str:
    print(c)
        