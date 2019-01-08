class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        num_palindromes = len(s)
        
        for i in range(2,len(s)+1):
            j = 0
            while j + i <= len(s):
                if s[j:j+i] == s[j:j+i][::-1]:
                    num_palindromes = num_palindromes + 1
                j = j + 1
        return num_palindromes