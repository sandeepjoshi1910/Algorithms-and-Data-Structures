# Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# Output: true

# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
# Output: false

class Solution:
    memo = {}
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        self.memo = {}
        if len(s3) != (len(s1) + len(s2)):
            return False

        return self.interl(s1,s2,s3,"")
    
    def interl(self,s1,s2,s3,sol):
        if (sol != "") and (sol == s3):
            self.memo[s1,s2,s3]
            return (s1 == "") and (s2 == "")
        
        if s1 == "":
            return self.interl("","",s3,sol+s2)
        elif s2 == "":
            return self.interl("","",s3,sol+s1)
        else:
            return self.interl(s1[1:],s2,s3,sol+s1[0]) or self.interl(s1,s2[1:],s3,sol+s2[0])
                
s = Solution()
print(s.isInterleave("bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa","babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab","babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab"))



