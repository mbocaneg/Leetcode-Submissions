class Solution:
    def searchInsert(self, nums, target):
        if len(nums) == 0:
            return 0

        low = 0
        high = len(nums) - 1
        pivot = 0
        while low <= high:
            pivot = (low + high ) // 2

            if(nums[pivot] == target):
                return pivot
            if(nums[pivot] < target):
                low = pivot + 1
            else:
                high = pivot - 1

        if nums[pivot] < target:
            return pivot + 1

        return pivot


sol = Solution()
# print(sol.searchInsert([1,3,5,6], 3))
# print(sol.searchInsert([1,3,5,6], 7))
# print(sol.searchInsert([1,3,5,6], 2))
print(sol.searchInsert([1,3,5], 4))
