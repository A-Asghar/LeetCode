# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        n1 = ""
        n2 = ""
        a1 = l1
        a2 = l2
        while(a1 != None):
            n1 += str(a1.val)
            a1 = a1.next
        # print(n1)
        while(a2 != None):
            n2 += str(a2.val)
            a2 = a2.next
        
        n1 = n1[::-1]
        n2 = n2[::-1]
        add = int(n1) +int(n2)
        add2 = str(add)[::-1]
        k = ListNode(0)
        l3 = k
        for i in range(len(add2)):
            l3.next = ListNode(int(add2[i]))
            l3 = l3.next
            
            
            
        return k.next
