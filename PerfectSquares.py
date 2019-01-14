# https://leetcode.com/problems/perfect-squares/
# So the idea is to see which of all the perfect squares formed till now can be part of the solution and which one of them gives minimum number of squares.

# Iterate from 1 to n
# Keep track of all solutions formed till now
# Keep track of all the squares seen
# For every number n, see which of the perfect squares seen till now can form the minimum solution
class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        def isPerfectSq(num:int) -> bool:
            root = int(num ** (1/2))
            return root * root == num
                
        sol = {1:1,2:2,3:3}
        sqs = [1]
        for i in range(4,n+1):
            if isPerfectSq(i):
                sol[i] = 1
                sqs.append(i)
            else:
                res = []
                for sq in sqs:
                    res.append(sol[sq]+sol[i-sq])
                sol[i] = min(res)
        return sol[n]