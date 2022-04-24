class Solution:
    def solve(self, words):
        c = words[0][0]
        t = ""
        i = 1
        in_all = True
        while in_all:
            for word in words:
                in_all = in_all and word.startswith(c)
            if in_all:
                t = c
                c += words[0][i]
            i += 1
        return t

class Solution:
    def solve(self, words):
        min_word = min(words, key=len, default="")
        for end in range(len(min_word), -1, -1):
            if all(word.startswith(min_word[:end]) for word in words):
                return min_word[:end]
        return ""