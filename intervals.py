# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        def is_present(i,ints):
            for k in ints:
                if i.start == k.start and i.end == k.end:
                    return True
            return False
        
        def does_intersect(i1,i2):
            first = None
            second = None
            if i1.start == i2.start:
                return True
            elif i1.start < i2.start:
                if i1.end < i2.start:
                    return False
                else:
                    return True
            elif i1.start > i2.start:
                if i2.end < i1.start:
                    return False
                else:
                    return True
            else:
                return True
            
        filtered = []
        for interval in intervals:
            if not (is_present(interval,filtered)):
                filtered.append(interval)
        
        intervals = filtered.copy()
        final_intervals = []
        
        while True:

            merged_intervals = []
            intervals_copy = []
            
            for i in range(0,len(intervals)):
                for j in range(i+1,len(intervals)):
                    if does_intersect(intervals[i],intervals[j]):
                        new_interval = Interval(min(intervals[i].start,intervals[j].start),max(intervals[j].end,intervals[i].end) )
                        if not is_present(new_interval,merged_intervals):
                            merged_intervals.append(new_interval)
                        if not is_present(intervals[i] ,intervals_copy):
                            intervals_copy.append(intervals[i])
                        if not is_present(intervals[j] ,intervals_copy):
                            intervals_copy.append(intervals[j])
                        
            
            for i in intervals_copy:
                intervals.remove(i)
            
            for i in intervals:
                merged_intervals.append(i)
            
            if merged_intervals == intervals:
                final_intervals = merged_intervals
                break
            
            intervals = merged_intervals.copy()
            merged_intervals = []
        
        return final_intervals
            

# data = [[1,3],[2,6],[8,10],[15,18]] 
data = [[321,336],[421,427],[170,184],[6,21],[178,193],[412,417],[136,141],[244,247],[0,3],[172,175],[223,234],[368,376],[180,197],[101,108],[442,460],[213,216],[153,159],[369,385],[481,488],[411,430],[363,378],[197,216],[453,454],[463,476],[256,271],[336,355],[186,203],[47,65],[254,254],[458,474],[238,249],[311,315],[10,22],[272,275],[259,262],[354,356],[211,222],[474,478],[492,509],[117,117],[424,430],[79,81],[363,370],[180,197],[479,489],[165,183],[14,30],[314,318],[8,14],[367,386],[121,122],[242,246],[125,141],[348,357],[5,23],[70,71],[124,133],[243,250],[128,143],[456,464],[266,279],[178,178],[449,461],[156,165],[430,433],[428,439],[96,98],[88,89],[90,106],[191,206],[106,119],[376,386],[114,125],[69,72],[247,264],[203,208],[350,363],[145,156],[225,226],[460,467],[176,177],[410,414],[263,281],[346,360],[287,296],[301,314],[354,364],[124,132],[1,6],[211,211],[275,281],[465,470],[499,501],[129,145],[115,124],[83,94],[182,188],[416,434],[344,358],[4,15],[355,360],[377,386],[187,200],[29,30]]   

inters = []

for i in data:
    inters.append(Interval(i[0],i[1]))

s = Solution()
ans = s.merge(inters)
for i in ans:
    print("["+str(i.start)+","+str(i.end)+"]")