from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        if not digits:
            return ans
        lst = {
            "2": ['a', 'b', 'c'],
            "3": ['d', 'e', 'f'],
            "4": ['g', 'h', 'i'],
            "5": ['j', 'k', 'l'],
            "6": ['m', 'n', 'o'],
            "7": ['p', 'q', 'r', 's'],
            "8": ['t', 'u', 'v'],
            "9": ['w', 'x', 'y', 'z']}

        curr = []

        def DFS(idx):
            if idx == len(digits):
                ans.append("".join(curr))
                return

            for i in lst[digits[idx]]:
                curr.append(i)
                DFS(idx+1)
                curr.pop()


        DFS(0)
        return ans


