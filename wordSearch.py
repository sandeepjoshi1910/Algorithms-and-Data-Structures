# https://leetcode.com/problems/word-search/
class Solution:
    found = False
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.found = False
        if board == [[]]:
            return False
        
        def findWord(word,i,seen,pos):
            if i == len(word)-1:
                print(pos)
                self.found = True

            if pos[0] < len(board) and pos[0] >= 0 and pos[1]+1 < len(board[0]) and pos[1]+1 >= 0 and (pos[0],pos[1]+1) not in seen and not self.found:
                if board[pos[0]][pos[1]+1] == word[i+1]:
                    findWord(word,i+1,seen|{pos},(pos[0],pos[1]+1))

            if pos[0] < len(board) and pos[0] >= 0 and pos[1]-1 < len(board[0]) and pos[1]-1 >= 0 and (pos[0],pos[1]-1) not in seen and not self.found:
                if board[pos[0]][pos[1]-1] == word[i+1]:
                    findWord(word,i+1,seen|{pos},(pos[0],pos[1]-1))
                    
            if pos[0]+1 < len(board) and pos[0]+1 >= 0 and pos[1] < len(board[0]) and pos[1] >= 0 and (pos[0]+1,pos[1]) not in seen and not self.found:
                if board[pos[0]+1][pos[1]] == word[i+1]:
                    findWord(word,i+1,seen|{pos},(pos[0]+1,pos[1]))
                    
            if pos[0]-1 < len(board) and pos[0]-1 >= 0 and pos[1] < len(board[0]) and pos[1] >= 0 and (pos[0]-1,pos[1]) not in seen and not self.found:
                if board[pos[0]-1][pos[1]] == word[i+1]:
                    findWord(word,i+1,seen|{pos},(pos[0]-1,pos[1]))
                    
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    findWord(word,0,set(),(row,col))
                        
                    
        return self.found