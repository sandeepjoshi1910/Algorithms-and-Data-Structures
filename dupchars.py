class Solution:
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        last_idx = {c:i for i, c in enumerate(s)}
        ans = []
        seen = set()
        for i, c in enumerate(s):
            if c not in seen:
                while ans and c < ans[-1] and i < last_idx[ans[-1]]:
                    tail = ans.pop()
                    seen.remove(tail)
                ans.append(c)
                seen.add(c)
        return ''.join(ans)

s = Solution()
s.removeDuplicateLetters("bdqcadqabcdq")