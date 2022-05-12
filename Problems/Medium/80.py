class Solution:
    def solve(self, root):
        if root:
            if root.val == 0 and ((root.left is None and root.right is None) or ((root.left and root.left.val == 0) and (root.right and root.right.val == 0))):
                return None
            else:
                root.left = self.solve(root.left)
                root.right = self.solve(root.right)
                return root
        else:
            return None
