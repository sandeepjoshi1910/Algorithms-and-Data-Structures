class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        d = [False for _ in range(len(s)+1)]
        d[0] = True
        for i in range(1,len(s)+1):
            for j in range(i):
                tmp = s[j:i]
                if (d[j] and tmp in wordDict):
                    d[i] = True
        return d[-1]

s= Solution()
s.wordBreak("catsandog",["cats", "dog", "sand", "and", "cat"])