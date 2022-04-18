# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root, lo, hi):
        count = 0
        def func(tree):
            if tree:
                nonlocal count
                count += lo <= tree.val <= hi
                func(tree.left) 
                func(tree.right)
        func(root) 
        return count