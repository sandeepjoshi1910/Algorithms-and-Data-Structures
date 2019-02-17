class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # Elements of which index/indices are needed to compute median -> x or x,y
        #   a. Calculate the length of arr1 and arr2 to find out x, y
        # Once we have x/x,y merge the two arrays until we have elements of indices x and y
        # return x or avg of x,y
        
        total_len = len(nums1) + len(nums2)
        isodd = total_len % 2 != 0
        indices = []
        
        if isodd:
            indices.append(((total_len+1) >> 1)-1)
        else:
            middle = (total_len+1) >> 1
            indices.append(middle-1)
            indices.append(middle)
            
        elems = 0
        i = 0
        j = 0
        merged = []
        
        while elems-1 < indices[-1]:
            if i > len(nums1)-1:
                merged = merged + nums2[j:]
                break
            elif j > len(nums2)-1:
                merged = merged + nums1[i:]
                break
            elif i > len(nums1)-1 and j > len(nums2)-1:
                break
            
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1
            elems += 1
        
        if isodd:
            return merged[indices[0]]
        else:
            return (merged[indices[0]]+merged[indices[1]])/2.0