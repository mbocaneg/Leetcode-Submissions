class Solution:
    def fizzBuzz(self, n):
        if n <= 0:
            return [None]
            
        l = [None] * n
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                l[i-1] = "FizzBuzz"
            elif i % 3 == 0:
                l[i-1] = "Fizz"
            elif i % 5 == 0:
                l[i-1] = "Buzz"
            else:
                l[i-1] = str(i)
        return l

sol = Solution().fizzBuzz(1)
for i in sol:
    print(i)