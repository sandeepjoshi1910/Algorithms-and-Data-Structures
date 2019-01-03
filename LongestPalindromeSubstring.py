
# Problem from leetcode : https://leetcode.com/problems/longest-palindromic-substring/

# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

# Example 1:

# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:

# Input: "cbbd"
# Output: "bb"
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 1:
            return s
        if s == '':
            return s
        ans = ''
        
        if s.replace(s[0],'') == '':
            return s
        
        for i in range(1,len(s)-1):
            j = 1
            while True:
                if i-j < 0 or i+1+j > len(s):
                    break
                if s[i-j] == s[i+j]:
                    if len(s[i-j:i+j+1]) > len(ans):
                        ans = s[i-j:i+j+1]
                    j = j + 1
                else:
                    break
        print(ans)
        for i in range(0,len(s)):
            if i != len(s)-1:
                if s[i] == s[i+1]:
                    if len(ans) < 2:
                        ans = s[i]+s[i+1]
                    j = 1
                    while True:
                        if i-j < 0 or i + 1 + j > len(s)-1:
                            break
                        if s[i-j] == s[i+1+j]:
                            if len(s[i-j:i+1+j+1]) > len(ans):
                                ans = s[i-j:i+1+j+1]
                            j = j + 1
                        else:
                            break
        if ans == '':
            ans = s[0]
        
        return ans