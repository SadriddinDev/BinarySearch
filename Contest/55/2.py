# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        a = float("-inf")
        def sub_sum(node):
            if not node:
                return 0
            nonlocal a
            currSum = (node.val + sub_sum(node.left) + sub_sum(node.right))
            if currSum>a:
                a = currSum
            return currSum
        sub_sum(root)
        return a if a > 0 else 0
