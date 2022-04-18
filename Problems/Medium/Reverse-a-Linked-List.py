class LLNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
class Solution: # v1
    def solve(self, node):
        n = node
        reversedNode = None
        while n:
            if not reversedNode:
                reversedNode = LLNode(n.val)
            else:
                reversedNode = LLNode(n.val, reversedNode)
            n = n.next
        return reversedNode


class Solution: # version best
    def solve(self, node):
        head, past = node, None
        while head:
            head.next, past, head = past, head, head.next
        return past