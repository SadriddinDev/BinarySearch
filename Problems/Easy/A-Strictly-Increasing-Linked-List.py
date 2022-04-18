# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, head):
        l = float("-inf")
        while head:
            if head.val <= l:
                return False
            l = head.val
            head = head.next
        return True