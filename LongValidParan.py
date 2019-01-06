# Problem from LeetCode
# Longest Valid Parantheses: https://leetcode.com/problems/longest-valid-parentheses/
class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # Edge cases
        if s == "":
            return 0
        
        # () => 1. Search () on right 2. Search for ( on left and ) on right
        # If both conditions fail, then move on
        # Merge all possible ranges.
        # Get final paran length
        parans = []
        i = 0
        while i < len(s) - 1:
            next = i + 1
            if s[i:i+2] == '()':
                l = i
                r = i + 1
                while True:
                    patternFound = False
                    if l - 1 >= 0 and r + 1 <= len(s)-1:
                        # ( () )
                        if s[l-1] == '(' and s[r+1] == ')':
                            l = l - 1
                            r = r + 1
                            patternFound = True
                    if r + 2 <= len(s) - 1 and not patternFound:
                        if s[r+1] + s[r+2] == '()':
                            r = r + 2
                            patternFound = True
                    
                    if not patternFound:
                        break
                parans.append((l,r))
                next = r + 1
            i = next
        
        # Need to merge intervals
        merged = []
        i = 0
        maxlen = 0
        while i < len(parans):
            if i == len(parans) - 1:
                merged.append(parans[i])
                break
            else:
                paran = parans[i]
                j = i + 1
                while True:
                    shouldBreak = True
                    if j <= len(parans) - 1:
                        if paran[1] + 1 == parans[j][0]:
                            paran = (paran[0],parans[j][1])
                            j = j + 1
                            shouldBreak = False
                    if shouldBreak:
                        break
                merged.append(paran)
                i = j
        while True:
            parans = []
            for interval in merged:
                if interval[0]-1 >= 0 and interval[1]+1 < len(s):
                    l = interval[0]
                    r = interval[1]
                    while True:
                        shouldBreak = True
                        if l - 1 >= 0 and r + 1 < len(s):
                            if s[l-1] == '(' and s[r+1] == ')':
                                l = l - 1
                                r = r + 1
                                shouldBreak = False
                        if shouldBreak:
                            break
                    parans.append((l,r))
                    if r - l + 1 > maxlen:
                        maxlen = r - l + 1
                else:
                    parans.append(interval)
                    if interval[1] - interval[0] + 1 > maxlen:
                        maxlen = interval[1] - interval[0] + 1
            # Need to merge intervals
            merged = []
            i = 0
            maxlen = 0
            while i < len(parans):
                if i == len(parans) - 1:
                    merged.append(parans[i])
                    if parans[i][1] - parans[i][0] + 1 > maxlen:
                        maxlen = parans[i][1] - parans[i][0] + 1 
                    break
                else:
                    paran = parans[i]
                    j = i + 1
                    while True:
                        shouldBreak = True
                        if j <= len(parans) - 1:
                            if paran[1] + 1 == parans[j][0]:
                                paran = (paran[0],parans[j][1])
                                j = j + 1
                                shouldBreak = False
                        if shouldBreak:
                            break
                    merged.append(paran)
                    if paran[1]-paran[0] + 1 > maxlen:
                        maxlen = paran[1]-paran[0] + 1
                    i = j
            if len(parans) == len(merged):
                break
        
        
        return maxlen