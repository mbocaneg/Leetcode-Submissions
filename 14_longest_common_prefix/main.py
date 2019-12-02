class Solution:
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""
        if strs[0] == "":
            return ""

        prefix = strs[0]

        str_iterator = iter(strs)
        next(str_iterator)

        for str in str_iterator:
            min_length = min(len(prefix), len(str))

            for i in range(0, min_length):
                if str[i] != prefix[i]:
                    prefix = prefix[:i]
                    break
            if min_length < len(prefix):
                prefix = prefix[:min_length]

        return "".join(prefix)

# strs = ["flower","flow","flight","fog"]
strs = ["aa","a"]

sol = Solution().longestCommonPrefix(strs)
print(sol)