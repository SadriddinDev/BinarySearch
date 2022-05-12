from collections import deque

class Solution:
    def solve(self, ops):
        stack = deque()
        for op in ops:
            if op == "DUP":
                if not stack:
                    return -1
                t = stack.pop()
                stack.append(t)
                stack.append(t)
            elif op == "POP":
                if not stack:
                    return -1
                stack.pop()
            elif op == "+":
                if stack:
                    t1 = stack.pop()
                    if stack:
                        t2 = stack.pop()
                        stack.append(t2 + t1)
                    else:
                        return -1
                else:
                    return -1
            elif op == "-":
                if stack:
                    t1 = stack.pop()
                    if stack:
                        t2 = stack.pop()
                        stack.append(t1 - t2)
                    else:
                        return -1
                else:
                    return -1
            else:
                stack.append(int(op))
        if stack:
            return stack.pop()
        return -1
        