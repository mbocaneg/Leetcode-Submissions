class Solution:
    def reverse(self, x):
        div = x
        acc = 0

        while div != 0:
            mod = div % 10
            print(mod)
            acc = acc * 10 + mod

            div = div // 10
        print(acc)

x = 123
sol = Solution().reverse(x)
# print(sol)