# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 16:04:06 2020

@author: santhilata
"""
'''
Sort a linked list in O(n log n) time using constant space complexity
'''

# break the list in the middle
# recursively sort the two sub lists
# merge the two sublists

class Node:
    
    def __init__(self, val):
        self.val = val
        self.next = None
        
 #get the list partition point       
def getfirstEnd(head):
    
    # find the middle point
    slow = head
    fast = head
    
    while fast.next != None or fast.next.next != None:
        slow = slow.next
        fast = fast.next.next
        
    return slow

def merge(n1, n2):
    
    head = Node(0)
    p1 = n1
    p2 = n2
    p = head
    
    while (p1 != None and p2 != None):
        
        if p1.val < p2.val:
            p.next = p1
            p1 = p1.next
            
        else:
            p.next = p2
            p2 = p2.next
            
        
        p = p.next
        
    if p1 != None:
        p.next = p1
    if p2 != None:
        p.next = p2
        
    return head.next
    

def _sortlist(head):
    
    if head ==None or head.next == None:
        return head
    
    p1 = head
    firstEnd = getfirstEnd(head)
    p2 = firstEnd.next
    firstEnd.next = None
    
    p1 = _sortlist(p1)
    p2 = _sortlist(p2)
    
    return merge(p1,p2)
    
    
    