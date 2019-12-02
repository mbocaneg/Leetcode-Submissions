class Solution:
    def isAnagram(self, s, t):
        d = {}

        for c in s:
            if not c in d:
                d[c] = 1
            else:
                d[c] += 1
        
        for c in t:
            if not c in d:
                return False
            else:
                d[c] -= 1

        for c in d:
            if d[c] != 0:
                return False

        return True

s = "anagram"
t = "nagaram"

# s = "rat"
# t = "car"

sol = Solution().isAnagram(s, t)
print(sol)