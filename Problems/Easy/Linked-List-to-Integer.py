# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node):
        n = 0
        while node:
            n = n*2 + node.val
            node = node.next
        return n