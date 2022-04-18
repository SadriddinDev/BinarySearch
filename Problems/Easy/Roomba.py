class Solution:
    def solve(self, moves, x, y):
        cord = [0, 0]
        for move in moves:
            if move == "NORTH":
                cord[1]+=1
            elif move == "SOUTH":
                cord[1]-=1
            elif move == "WEST":
                cord[0]-=1
            else:
                cord[0]+=1
        return cord == [x, y]