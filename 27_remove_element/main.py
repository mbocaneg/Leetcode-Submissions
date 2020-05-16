class Solution:
    # def removeElement(self, nums, val):

    #     tail = 0
    #     for i in range(len(nums)):
    #         if nums[i] != val:
    #             nums[tail] = nums[i]
    #             tail += 1

    #     # print(nums[:head])
    #     return tail

    def removeElement(self, nums, val):

        tail = len(nums)
        head = 0
        while head < tail:
            if nums[head] == val:
                nums[head] = nums[tail-1]
                tail -= 1
            else:
                head += 1
        # print(nums[:tail])
        return tail

sol = Solution()
print(sol.removeElement([2,3,2,3], 3))
print(sol.removeElement([0,1,2,2,3,0,4,2], 2))