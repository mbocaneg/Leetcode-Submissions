class Solution:
    def firstUniqChar(self, s):
        if s == "":
            return -1
        
        d = {}

        for i in range(0, len(s)):
            if(d.get(s[i]) != None):
                d[s[i]] += 1
            else:
                d[s[i]] = 1

        for i in range(0, len(s)):
            if d[s[i]] == 1:
                return i
        return -1

s = "leetcode"
sol = Solution().firstUniqChar(s)
print(sol)