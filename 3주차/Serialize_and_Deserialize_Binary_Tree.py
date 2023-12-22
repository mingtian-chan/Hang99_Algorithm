# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        ans = ""
        if root is None:
            return ""

        return f"{root.val},{self.serialize(root.left)},{self.serialize(root.right)}"

    def deserialize(self, data):
        if not data:
            return None

        return self.deserialize_list(data.split(","))

    def deserialize_list(self, data):
        val = data.pop(0)
        if not val:
            return None

        root = TreeNode(val)
        root.left = self.deserialize_list(data)
        root.right = self.deserialize_list(data)

        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))