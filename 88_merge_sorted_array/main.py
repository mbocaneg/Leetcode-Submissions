class Solution:
    def merge(self, nums1, m, nums2, n):
        m -= 1
        n -= 1

        tail = len(nums1) - 1
        while tail >= 0:
            if m < 0:
                nums1[tail] = nums2[n]
                n -= 1
            elif n < 0:
                nums1[tail] = nums1[m]
                m -= 1
            else:
                if nums1[m] > nums2[n]:
                    nums1[tail] = nums1[m]
                    m -= 1
                else:
                    nums1[tail] = nums2[n]
                    n -= 1

            tail -= 1

sol = Solution()

nums1 = [1,2,10,11,0,0,0,0]
nums2 = [1,5,6,12]
sol.merge(nums1, 4, nums2, 4)
print(nums1)
