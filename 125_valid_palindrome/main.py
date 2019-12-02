class Solution:
    def isPalindrome(self, s):
        if s == "":
            return True
        
        i = 0
        j = len(s)-1

        while i < j:
            while not s[i].isalnum() and i < len(s)-1:
                i += 1
            while not s[j].isalnum() and j > 0:
                j -= 1
            if i > len(s)-1 or j < 0 or i > j:
                return True


            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        
        return True


# s = "A man, a plan, a canal: Panama"
s = ".,"

sol = Solution().isPalindrome(s)
print("is palindrome: %r" % sol)