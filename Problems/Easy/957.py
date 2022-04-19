# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root, target):
        if root:
            return root.val == target or self.solve(root.left, target) or self.solve(root.right, target)
        return False