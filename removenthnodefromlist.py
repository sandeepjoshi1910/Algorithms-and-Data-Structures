# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head == None:
            return None
        cur = head
        delnode = head
        
        i = 1
        j = 1        
        while cur != None:
            if i - j > n:
                delnode = delnode.next
            cur = cur.next
            
            i = i + 1
        
        if i-1 == n:
            return head.next
        
        delnode.next = delnode.next.next
        

        return head
        