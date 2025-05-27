class Solution(object):
    def maxSumBST(self, root):
        self.max_sum = 0

        def dfs(node):
            if not node:
                # Empty node is considered BST with neutral min/max and sum = 0
                return float('inf'), float('-inf'), 0

            left_min, left_max, left_sum = dfs(node.left)
            right_min, right_max, right_sum = dfs(node.right)

            # Check if current subtree is a BST
            if left_max < node.val < right_min:
                curr_sum = left_sum + right_sum + node.val
                self.max_sum = max(self.max_sum, curr_sum)
                return min(left_min, node.val), max(right_max, node.val), curr_sum
            else:
                # Invalid BST, return a neutral min/max and reset sum to 0
                return float('-inf'), float('inf'), 0

        dfs(root)
        return self.max_sum
