# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def check(self, node):
        if node is None:
            return 0

        left= self.check(node.left)
        right = self.check(node.right)
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1

        return max(left, right) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        return self.check(root) != -1



# 디버깅용
    def make_tree_by(self, lst, idx):
        parent = None
        if idx < len(lst):
            value = lst[idx]
            if value is None:
                return

            parent = TreeNode(value)
            parent.left = self.make_tree_by(lst, 2 * idx + 1)
            parent.right = self.make_tree_by(lst, 2 * idx + 2)
        return parent


solution_instance = Solution()
root = solution_instance.make_tree_by([1], 0)
print(solution_instance.isBalanced(root))
