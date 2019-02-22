# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        
        # Copy the list without random pointers
        # Find the random node for each node in original list
            # Find that node in the list and set random node
            
        
        if head == None:
            return head
        
        # Copy default list
        nhead = RandomListNode(head.label)
        cur = head
        ncur = nhead
        cur = cur.next
        while cur != None:
            ncur.next = RandomListNode(cur.label)
            cur = cur.next
            ncur = ncur.next
        
        cur = head
        ncur = nhead
        while cur != None:
            # Random node is None
            if cur.random == None:
                cur  = cur.next
                ncur = ncur.next
                continue
                
            # Random node is not None
            it = nhead
            val = cur.random.label
            # Iterate list to find the random node
            while it != None:
                if it.label == val:
                    ncur.random = it
                    break
                else:
                    it = it.next
            
            cur = cur.next
            ncur = ncur.next
        return nhead