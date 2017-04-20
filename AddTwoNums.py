# problem 2 : Add Two Numbers

# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    head = None
    tail = None

    ans = None


    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # len1 = self.sizeOfList(l1)
        # len2 = self.sizeOfList(l2)
        #
        # exponent = 0
        # if len1 > len2:
        #     exponent = len1
        # else:
        #     exponent = len2

        carry = 0

        while l1 != None or l2!=None:

            if l1 == None:
                val1 = 0
            else:
                val1 = l1.val
            if l2 == None:
                val2 = 0
            else:
                val2 = l2.val

            sum = val1 + val2 + carry
            carry = 0
            if sum % 10 != sum:
                sum = sum %10
                carry = 1

            sumNode = ListNode(sum)
            self.setNextResNode(sumNode)
            try:
                l1 = l1.next
            except:
                print("l1 not available")
                l1 = None
            try:
                l2 = l2.next
            except:
                print("l2 not available")
                l2 = None
        if carry != 0:
            self.setNextResNode(ListNode(carry))
        return self.head


    def setNextResNode(self,node):
        if self.ans == None:
            self.head = self.tail = self.ans = node
            return

        self.tail.next = node
        self.tail = self.tail.next

    def printAns(self):
        currenNode = self.head
        while currenNode != None:
            print(currenNode.val)
            currenNode = currenNode.next

    def sizeOfList(self,lList):
        size = 1
        while lList.next != None:
            lList = lList.next
            size = size + 1
        return size
