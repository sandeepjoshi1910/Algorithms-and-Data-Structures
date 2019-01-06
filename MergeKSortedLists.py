# Problem from Leetcode : https://leetcode.com/problems/merge-k-sorted-lists/
# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

# Example:

# Input:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# Output: 1->1->2->3->4->4->5->6


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if lists == []:
            return None
        
        newlists = []
        
        for l in lists:
            if l !=  None:
                newlists.append(l)
        
        if newlists == []:
            return None
        
        lists = newlists
        
        if len(lists) == 1:
            return lists[0]
        
        
        while len(lists) != 1:
            newlists = []
            i = 0
            while i < len(lists):
                if i + 1 > len(lists) - 1:
                    newlists.append(lists[i])
                    break
                node = lists[i]
                lnode = lists[i+1]
                newlist = None
                newhead = None

                while node != None or lnode != None:
                    # print(node.val,lnode.val)
                    if node == None:
                        if newlist == None:
                            newlist = lnode
                            newhead = newlist
                        else:
                            newlist.next = lnode
                        break

                    if lnode == None:
                        if newlist == None:
                            newlist = node
                            newhead = newlist
                        else:
                            newlist.next = node
                        break

                    if node.val < lnode.val:
                        if newlist == None:
                            newlist = ListNode(node.val)
                            newhead = newlist
                        else:
                            newlist.next = ListNode(node.val)
                            newlist = newlist.next
                        node = node.next

                    else:
                        if newlist == None:
                            newlist = ListNode(lnode.val)
                            newhead = newlist
                        else:
                            newlist.next = ListNode(lnode.val)
                            newlist = newlist.next
                        lnode = lnode.next
                newlists.append(newhead)
                i = i + 2
            lists = newlists
        return lists[0]