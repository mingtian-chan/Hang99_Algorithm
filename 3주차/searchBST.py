# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return None

        if root.val == val:
            return root

        if root.val > val:
            return self.searchBST(root.left, val)

        if root.val < val:
            return self.searchBST(root.right, val)

# 디버깅용
#     def make_tree_by(self, lst, idx):
#         parent = None
#         if idx < len(lst):
#             value = lst[idx]
#             if value is None:
#                 return
#
#             parent = TreeNode(value)
#             parent.left = self.make_tree_by(lst, 2 * idx + 1)
#             parent.right = self.make_tree_by(lst, 2 * idx + 2)
#         return parent
#
#
# solution_instance = Solution()
# root = solution_instance.make_tree_by([4,2,7,1,3], 0)
# print(solution_instance.searchBST(root, 2))