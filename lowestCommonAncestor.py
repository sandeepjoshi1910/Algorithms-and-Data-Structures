# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    ancestor = None
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.ancestor = None
        self.getAncestor(root,p.val,q.val)
        return self.ancestor
    
    def getAncestor(self,node,p,q):
        
        if node == None:
            return False, False
        pr = False
        qr = False
        if node.val == p:
            pr = True
        
        if node.val == q:
            qr = True
        
        l1,r1 = self.getAncestor(node.left,p,q)
        
        l2,r2 = self.getAncestor(node.right,p,q)
        
        if (l1 or l2) and (r1 or r2) and self.ancestor == None:
            self.ancestor = node
            return True,True
        elif (((l1 or l2) and (qr)) or ((pr) and (r1 or r2))) and self.ancestor == None:
            self.ancestor = node
            return True,True
        else:
            return l1 or l2 or pr , r1 or r2 or qr