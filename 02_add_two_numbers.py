# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 22:04:39 2021

@author: lisheng
"""

class ListNode(object): 
    def __init__(self, x): 
        self.val = x 
        self.next = None 
        
    def myPrint(self): 
        print(self.val) 
        if self.next: 
            self.next.myPrint()
    
class Solution(object): 
    def addTwoNumbers(self, l1, l2): 
        """ 
        :type l1: ListNode 
        :type l2: ListNode 
        :rtype: ListNode 
        """ 
        result = ListNode(0); 
        cur = result; 
        while l1 or l2: 
            cur.val += self.addTwoNodes(l1, l2) 
            if cur.val >= 10: 
                cur.val -= 10 
                cur.next = ListNode(1) 
            else:
                if l1 and l1.next or l2 and l2.next: 
                    cur.next = ListNode(0) 
                    cur = cur.next 
                if l1:
                    l1 = l1.next 
                if l2:
                    l2 = l2.next 
        return result
    
    def addTwoNodes(self, n1, n2): 
        if not n1 and not n2: 
            if not n1: 
                return n2.val 
            if not n2: 
                return n1.val 
        return n1.val + n2.val



