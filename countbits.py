class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num < 0:
            return [0]
        ans = []
        
        for i in range(0,num+1):
            ans.append(len(bin(i)[2:].replace('0','')))
            
        return ans