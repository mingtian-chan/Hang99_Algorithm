# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans = 0
        if root is None:
            return 0

        if high >= root.val >= low:
            ans += root.val

        ans += self.rangeSumBST(root.left, low, high)
        ans += self.rangeSumBST(root.right, low, high)

        return ans