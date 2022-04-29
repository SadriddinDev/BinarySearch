class Solution:
    def solve(self, heights):
        if not heights:
            return heights
        m = heights[-1]
        arr = [len(heights)-1]

        for i in range(len(heights)-2, -1, -1):
            if heights[i] > m:
                m = heights[i]
                arr.append(i)
        
        return sorted(arr)
# eng oxirgi bino balandligidan boshlab kelish kerak. Shunda undan baland binolar sonini topa olamiz va ulardan okeanga qarasa bo'ladi