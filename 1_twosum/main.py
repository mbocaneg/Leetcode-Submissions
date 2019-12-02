class Solution:
    def twoSum(self, nums, target):
        d = {}
        for index, num in enumerate(nums):
            d[num] = index

        for index, num in enumerate(nums):
            compliment = target - num
            if compliment in d and d[compliment] != index:
                return [index, d[compliment]]
        return [None]


nums = [3,2,4]
target = 6

sol = Solution().twoSum(nums, target)
for i in sol:
    print(i)
        
