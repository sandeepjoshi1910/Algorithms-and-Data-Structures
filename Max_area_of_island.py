# https://leetcode.com/problems/max-area-of-island/
class Solution:
    def maxAreaOfIsland(self, grid: 'List[List[int]]') -> 'int':
        if len(grid) == 0:
            return 0
        
        # iterate over all 1's, 
        # When a 1 is found, add all the co-ordinates to a queue which are also 1 (avoiding duplicates), once a 1 is processed, mark it as x or -1
        # Once all 1's are processed for a 1 found, record if its max length
        area = 0
        rows = len(grid)
        cols = len(grid[0])
        for r in range(0,rows):
            for c in range(0,cols):
                
                if grid[r][c] == 1:
                    if area < 1:
                        area = 1
                    q = [(r,c)]
                    seen = set((r,c))
                    elem = 0
                    while q != []:
                        cor = q.pop(0)
                        points = [(cor[0]+1,cor[1]),(cor[0]-1,cor[1]),(cor[0],cor[1]+1),(cor[0],cor[1]-1)]
                        for point in points:
                            if point[0] in range(rows) and point[1] in range(cols) and point not in seen:
                                if grid[point[0]][point[1]] == 1:
                                    q.append(point)
                                    seen.add(point)
                                    elem += 1
                                    grid[point[0]][point[1]] = -1
                    if elem > area:
                        area = elem
        return area