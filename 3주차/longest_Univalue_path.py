class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def longestUnivaluePath(self, root: TreeNode) -> int:

        def dfs(node):
            """Return longest univalue branch and longest univalue path (post-order traversal)."""
            nonlocal ans
            if not node: return 0
            lx, rx = dfs(node.left), dfs(node.right)
            if not node.left or node.left.val != node.val: lx = 0
            if not node.right or node.right.val != node.val: rx = 0
            ans = max(ans, 1 + lx + rx)
            return 1 + max(lx, rx)

        ans = 0
        dfs(root)
        return max(0, ans - 1)