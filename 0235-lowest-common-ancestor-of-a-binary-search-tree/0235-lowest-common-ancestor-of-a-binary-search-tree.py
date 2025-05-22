# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if not root: return None
        #if both of then want to go left then go left
        if p.val<root.val and q.val<root.val:
            lowestCommonAncestor(self, root.left, p, q)
        #if both of then want to go right then go  right
        if p.val>root.val and q.val>root.val:
            lowestCommonAncestor(self, root.left, p, q)  
        return root    
            


        