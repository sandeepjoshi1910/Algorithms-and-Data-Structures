# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        nums = []
        cur = head
        while cur != None:
            nums.append(cur.val)
            cur = cur.next
        nums = sorted(nums)
        cur = head
        for num in nums:
            cur.val = num
            cur = cur.next
        return head