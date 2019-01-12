# https://leetcode.com/problems/course-schedule/
class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if prerequisites == []:
            return True
        
        pre_dict = {}
        for req in prerequisites:
            if req[0] in pre_dict:
                pre_dict[req[0]].append(req[1])
            else:
                pre_dict[req[0]] = [req[1]]
                
        course_taken = set()
        
        # 1. len(course_taken) == numCourses
        # 2. pre_dict does not change
        
        # Add all courses not needing pre-requisites
        for course in range(0,numCourses):
            if course not in pre_dict.keys():
                course_taken.add(course)
        
        if len(course_taken) == 0 and numCourses > 0:
            return False
        
        icourses = course_taken.copy()
        
        while True:
            
            for c in icourses:
                for k in pre_dict.keys():
                    if c in pre_dict[k]:
                        pre_dict[k].remove(c)
            
            freed = set()
            for course,pre_reqs in pre_dict.items():
                if pre_reqs == []:
                    freed.add(course)
            
            if len(freed) == 0:
                return False
            
            for course in freed:
                del pre_dict[course]
            
            icourses = freed.copy()
            [course_taken.add(course) for course in freed]
            
            if len(course_taken) == numCourses:
                return True
