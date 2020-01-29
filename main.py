from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return 0

        localSum = nums[0]
        globalSum = nums[0]

        for val in nums[1:]:
            if val > localSum + val:
                localSum = val
            else:
                localSum += val

            if localSum > globalSum:
                globalSum = localSum

        return globalSum


my = Solution()

n0 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
n1 = [-3, -3, 10, 11,  1, -10, -10, 21, -17]
n2 = [-2, -1]
n22 = [-1, -2]
n3 = [-1, 0]
n4 = [0, -3, 1, 1]

ans = my.maxSubArray(n0)
print('ans solved= %s' % str(ans))
