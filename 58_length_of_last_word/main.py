class Solution:

    def lengthOfLastWord(self, s):

        if len(s) == 0 or s is None:
            return 0

        tail = len(s) - 1
        word_length = 0
        is_last_word = False

        while tail >= 0:
            if s[tail] == " " and is_last_word == True:
                return word_length
            if s[tail] != " ":
                is_last_word = True
                word_length += 1
            tail -= 1

        return word_length

sol = Solution()
# print(sol.lengthOfLastWord("Hello World"))
print(sol.lengthOfLastWord("a"))