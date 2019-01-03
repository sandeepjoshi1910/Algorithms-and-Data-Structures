class Solution:
    seen = []
    trans = 0
    
        
    def transfor(self,beginWord,endWord,wordList,trans,seen):
        def getFilterFun(w1):
            def oneCharDiff(w2):
                diff = 0
                for i in range(0,len(w1)):
                    if w1[i] != w2[i]:
                        diff = diff + 1
                return diff == 1
            return oneCharDiff
        if getFilterFun(beginWord)(endWord):
            if trans+1 < self.trans or self.trans == 0:
                self.trans = trans + 1
            return
            
        diffwords = list(filter(getFilterFun(beginWord),wordList))
        
        for word in diffwords:
            if word not in seen:
                # self.seen.append(word)
                self.transfor(word, endWord, wordList, trans + 1,seen+[word])
                
        
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        
        """
        Solution:
            1) Check if end word is in wordlist and one dist words from beginword in wordlist
            2)  a. Find all words which are at 1 char diff from begin word. 
                b. Maintain a seen list to avoid circular looping
                c. For all transformations, go to next transformations at 1 char diff which are not in seen
                d. Keep doing this till endWord is at 1 char diff from current word
        """

        

        self.seen = [beginWord]
        self.trans = 0
        
        self.transfor(beginWord,endWord,wordList,1,[beginWord])
        if self.trans == 0:
            return 0
        else:
            return self.trans
        

s = Solution()
print(s.ladderLength("qa","sq",["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"]))
# print(s.ladderLength("hit","cog",["hot","dot","dog","lot","log","cog"]))


