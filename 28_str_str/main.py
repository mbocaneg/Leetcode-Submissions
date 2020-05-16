class Solution:
    def strStr(self, haystack, needle):
        if needle == "":
            return 0
        if len(needle) > len(haystack):
            return -1
        if needle == haystack:
            return 0
        
        for i in range(len(haystack)):
            for j in range( len(needle)):
                if haystack[i] == needle[0] :
                    if j + i > len(haystack) - 1:
                        return -1
                    if needle[j] != haystack[i + j]:
                        break
                    if j == len(needle) - 1:
                        return i
                else:
                    break
        
        return -1

        
sol = Solution()
# print(sol.strStr("hello", "ll"))
# print(sol.strStr("aaaaa", "bba"))
# print(sol.strStr("", "a"))
# print(sol.strStr("ssssd", "sd"))
# print(sol.strStr("mississippi","issipi"))
print(sol.strStr("h", "h"))
