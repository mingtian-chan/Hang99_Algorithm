class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []

        def dfs(used, left):
            i = len(left)
            if i == 0:
                self.res.append(used)
                return
            for j in range(i):
                n = left.pop(0)
                dfs(used + [n], left)
                left.append(n)
            return

        dfs([], nums)
        return self.res