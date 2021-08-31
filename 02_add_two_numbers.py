# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 22:04:39 2021

@author: lisheng
"""

# class ListNode(object): 
#     def __init__(self, x): 
#         self.val = x 
#         self.next = None 
        
#     def myPrint(self): 
#         print(self.val) 
#         if self.next: 
#             self.next.myPrint()
    
# class Solution(object): 
#     def addTwoNumbers(self, l1, l2): 
#         """ 
#         :type l1: ListNode 
#         :type l2: ListNode 
#         :rtype: ListNode 
#         """ 
#         result = ListNode(0); 
#         cur = result; 
#         while l1 or l2: 
#             cur.val += self.addTwoNodes(l1, l2) 
#             if cur.val >= 10: 
#                 cur.val -= 10 
#                 cur.next = ListNode(1) 
#             else:
#                 if l1 and l1.next or l2 and l2.next: 
#                     cur.next = ListNode(0) 
#                     cur = cur.next 
#                 if l1:
#                     l1 = l1.next 
#                 if l2:
#                     l2 = l2.next 
#         return result
    
#     def addTwoNodes(self, n1, n2): 
#         if not n1 and not n2: 
#             if not n1: 
#                 return n2.val 
#             if not n2: 
#                 return n1.val 
#         return n1.val + n2.val



class Solution(object): 
    def addTwoNumbers(self, l1, l2): 
        """ 
        :type l1: ListNode 
        :type l2: ListNode 
        :rtype: ListNode 
        """ 
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        
        dummy = ListNode(0)
        p = dummy
        carry = 0
        
        while l1 and l2:
            p.next = ListNode((l1.val + l2.val + carry) % 10)
            carry = (l1.val + l2.val + carry) // 10
            l1 = l1.next
            l2 = l2.next
            p = p.next
            
        if l2:
            while l2:
                p.next = ListNode((l2.val + carry) % 10)
                carry = (l2.val + carry) // 10
                l2 = l2.next
                p = p.next
                
        if l1:
            while l1:
                p.next = ListNode((l1.val + carry) % 10)
                carry = (l1.val + carry) // 10
                l1 = l1.next
                p = p.next
                
        if carry == 1:
            p.next = ListNode(1)
        
        return dummy.next


