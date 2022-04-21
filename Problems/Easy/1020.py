class LLNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
class Solution:
    def solve(self, head, pos, val):
        index = 0
        Head = None
        if pos == 0:
            Head = LLNode(val, head)
            return Head
        while head:
            index += 1
            if Head is None:
                Head = head
            if index == pos:
                head.next = LLNode(val, head.next)
                return Head
            head = head.next
