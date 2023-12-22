from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def dfs(idx, path):
            ans.append(path)

            for i in range(idx, len(nums)):
                dfs(i + 1, path + [nums[i]])

        dfs(0, [])

        return ans
