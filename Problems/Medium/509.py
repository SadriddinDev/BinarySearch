class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def solve(self, root):
        count = 0

        def recursive(node):
            if not node:
                return
            nonlocal count
            if (node.left and not node.right) or (not node.left and node.right):
                count += 1
            recursive(node.left)
            recursive(node.right)
        recursive(root)
        return count
