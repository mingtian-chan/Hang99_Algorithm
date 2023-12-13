from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []

        for i in range(0, len(nums)):
            ans
            for j in range(0, len(nums)):
                for k in range(0, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0 and i != j and j != k and k != i:
                        ans.append([i,j,k])

        return []


