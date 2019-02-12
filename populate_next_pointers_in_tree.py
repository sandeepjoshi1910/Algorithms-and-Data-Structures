# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root == None:
            return
        root.next = None
        q = [root]
        
        
        while q != [None]:
            next_lvl = []
            for node in q:
                if node != None:
                    if node.left != None:
                        next_lvl.append(node.left)
                    if node.right != None:
                        next_lvl.append(node.right)
                
            next_lvl.append(None)
            for it,node in enumerate(next_lvl):
                if node != None:
                    node.next = next_lvl[it+1]
            
            q = next_lvl