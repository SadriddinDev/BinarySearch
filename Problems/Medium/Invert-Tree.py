# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        def func(node):
            if node:
                node.left, node.right = node.right, node.left
                func(node.left)
                func(node.right)
        func(root)
        return root