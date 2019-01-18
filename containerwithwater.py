class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if height == []:
            return 0
        def vol(i,j):
            return (j-i) * (min(height[i],height[j]))
        
        maxvol = 0
        
        i = 0
        j = len(height)-1
        
        while i < j:
            if vol(i,j) > maxvol:
                maxvol = vol(i,j)
            
            if height[i] > height[j]:
                j = j -1
            else:
                i = i + 1
        return maxvol