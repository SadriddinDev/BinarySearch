# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution: # v1
    def solve(self, node):
        n = node
        node = node.next
        while node:
            n = n.next
            node = node.next
            if node:
                node = node.next
        return n.val


# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution: # v2
    def solve(self, node):
        slow = node
        fast = node
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.val