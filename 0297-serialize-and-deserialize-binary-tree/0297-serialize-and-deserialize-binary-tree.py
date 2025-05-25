from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        if not root:
            return ""

        q = deque([root])
        result = []

        while q:
            node = q.popleft()
            if node:
                result.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                result.append("#")

        return ",".join(result)

    def deserialize(self, data):
        if not data:
            return None

        values = data.split(',')
        root = TreeNode(int(values[0]))
        q = deque([root])
        i = 1

        while q and i < len(values):
            node = q.popleft()

            if values[i] != "#":
                node.left = TreeNode(int(values[i]))
                q.append(node.left)
            i += 1

            if i < len(values) and values[i] != "#":
                node.right = TreeNode(int(values[i]))
                q.append(node.right)
            i += 1

        return root
