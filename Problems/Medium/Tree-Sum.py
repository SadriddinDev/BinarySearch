# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        s = 0
        def calc(node):
            if node:
                nonlocal s
                s += node.val
                calc(node.left)
                calc(node.right)
        calc(root)
        return s