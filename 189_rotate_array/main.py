class Solution:
    def rotate(self, nums, k):
        if len(nums) == 0:
            return
        if k == 0:
            return
        
        nums2 = [None] * len(nums)
        j = len(nums) - k

        for i in range(0, len(nums)):
            nums2[i] = nums[j]
            j = (j + 1) % len(nums)

        for i in range(len(nums2)):
            nums[i] = nums2[i]

nums = [1,2,3,4,5,6,7]
k = 3

sol = Solution().rotate(nums, k)

for n in nums:
    print(n)