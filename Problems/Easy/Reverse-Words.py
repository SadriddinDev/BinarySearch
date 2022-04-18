class Solution: # v1
    def myreverse(self, start, end, massiv):
        while start < end:
            massiv[start], massiv[end] = massiv[end], massiv[start]
            start += 1
            end -= 1
        
    def solve(self, sentence):
        letters = list(sentence)
        self.myreverse(0, len(letters)-1, letters)
        start = 0
        end = 0
        for i in range(len(letters)):
            if letters[i] == " ":
                end = i-1
                self.myreverse(start, end, letters)
                start = i + 1
            if i == len(letters)-1:
                self.myreverse(start, i, letters)
        ans = ""
        for i in letters:
            ans+=i
        return ans
class Solution: # v2
    def solve(self, sentence:str):
        words = sentence.split()[::-1]
        for word in words:
            word = word[::-1]
        return " ".join([word for word in words])