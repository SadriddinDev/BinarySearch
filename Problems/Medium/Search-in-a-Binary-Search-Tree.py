# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: # recursive
    def solve(self, root, val):
        if root is None:
            return False
        return root.val == val or self.solve(root.left, val) or self.solve(root.right, val) 