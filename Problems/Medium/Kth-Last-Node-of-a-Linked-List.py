# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution: # version 1
    def solve(self, node, k):
        head, past = node, None
        while head:
            head.next, past, head = past, head, head.next
        c = 0
        while past:
            if k == c:
                return past.val
            c+=1
            past = past.next

"""
In here, node is last element which we can keep in memory
and if current index is greater than k we mode last index to one right
"""
class Solution: # best solution
    def solve(self, node, k):
            t, i = node, 0
            while t:
                if i > k:
                    node = node.next
                i += 1
                t = t.next
            return node.val