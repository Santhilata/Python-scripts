# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 20:22:54 2020

@author: santhilata
"""
'''
Given a sorted linked list, delete all duplicates such that each
 element appear only once.For example,Given 1->1->2, return 1->2
 Given 1->1->2->3->3, return 1->2->3.
'''

class Node:
    
    def __init__(self,val):
        
        self.val = val
        self.next = None

def _printList(head)        :
    p = head.next
    
    while p.next != None:
        print(p.val,end='->')
        p = p.next
        
    print(p.val)
    
    
        
arr = [1,1,1,2,3,3,4]

head = Node(-1)

p = head
for i in arr:
    
    temp = Node(i)
    p.next = temp    
    p = p.next

_printList(head)


def _removeDuplicates(head):
    
    prev = head.next
    p = prev.next
    
    if prev == None or prev.next == None :
        return head
    
    while p != None:
        if p.val == prev.val:
            prev.next = p.next
            p = p.next
            
        else:
            prev = p
            p = p.next
            
    return head

head = _removeDuplicates(head)

_printList(head)
        
    
    
    
    
    