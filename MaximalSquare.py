# https://leetcode.com/problems/maximal-square/
class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if matrix == [[]]:
            return 0
        elif matrix == [["1"]]:
            return 1
        
        def forms_sq(r,c,size):
            nr = r + size - 1
            nc = c + size - 1
            nums = set()
            for i in range(c,c+size):
                if i < len(matrix[0]) and nr < len(matrix):
                    nums.add(matrix[nr][i])
                else:
                    nums.add(0)
            for i in range(r,r+size-1):
                if i < len(matrix) and nc < len(matrix[0]):
                    nums.add(matrix[i][nc])
                else:
                    nums.add(0)
            # print(nums,r,c,size)
            return nums == {'1'}
                
            
            
        maxarea = 0
        for row in range(0,len(matrix)):
            for col in range(0,len(matrix[0])):
                if matrix[row][col] == "1":
                    if maxarea == 0:
                        maxarea = 1
                    i = 2
                    while forms_sq(row,col,i):
                        if i * i > maxarea:
                            maxarea = i * i
                        i = i + 1
        return maxarea