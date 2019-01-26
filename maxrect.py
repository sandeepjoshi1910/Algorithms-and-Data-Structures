class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        
        if heights == []:
            return 0
        elif len(heights) == 1:
            return heights[0]
        
        maxr = 0
        
        i = 0
        minh = heights[0]
        leng = 0
        area = 0
        while i < len(heights):
            if heights[i] > area and (min(minh,heights[i]) * (leng+1)) <= heights[i]:
                area = heights[i]
                leng = 1
                minh = heights[i]
                if area > maxr:
                    maxr = area
            elif (min(minh,heights[i]) * (leng+1)) >= area:
                area = (min(minh,heights[i]) * (leng+1))
                minh = min(minh,heights[i])
                leng += 1
                if area > maxr:
                    maxr = area
            else:
                area = heights[i]
                leng = 1
                minh = heights[i]
                if area > maxr:
                    maxr = area
            i = i + 1
        
        return maxr
        
        

s = Solution()
print(s.largestRectangleArea([1,2,3,4,5]))