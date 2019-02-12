# https://leetcode.com/problems/sum-root-to-leaf-numbers/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        elif root.left == None and root.right == None:
            return root.val
        
        ans = self.sumnum(root)
        res = 0
        for num in ans:
            res = res + int(num)
        return res
        
    def sumnum(self,node):
        if node.left == None and node.right == None:
            return [str(node.val)]
        
        ans = []
        val = str(node.val)
        
        if node.left != None:
            [ans.append(x) for x in self.sumnum(node.left)]
        if node.right != None:
            [ans.append(x) for x in self.sumnum(node.right)]
        
        res = []
        [res.append(val+x) for x in ans]
        return res