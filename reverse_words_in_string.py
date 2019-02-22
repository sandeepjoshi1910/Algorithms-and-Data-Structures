# https://leetcode.com/problems/reverse-words-in-a-string/
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s.replace(' ','') == '':
            return ''
        
        words = s.split(" ")
        for i in range(len(words)):
            words[i] = words[i].replace(' ','')
        
        new_words = words[::-1]
        while ' ' in new_words:
            new_words.remove(' ')
        while '' in new_words:
            new_words.remove('')
        ans = ' '.join(word for word in new_words)
        return ans
        