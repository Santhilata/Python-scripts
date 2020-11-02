# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 21:16:55 2020

@author: santhilata
"""
'''
Given a singly linked list, determine if it is a palindrome.
'''

class Node:
    def __init__(self,val):
        
        self.val = val
        self.next = None
        

arr = ['a','b','c','b','a']
arr = ['a']
arr = ['a','b']
#arr = ['a','b','b','a']
#arr =[]

def _createLinkedList(arr):
    
    head = Node('zz')
    p = head
    
    for ch in arr:        
        temp = Node(ch)
        p.next = temp
        p = p.next
        
    return head

def _printList(head):
    
    if head and head.next :
        p = head.next
        
        while p.next != None:
            print(p.val, end='->')
            p = p.next
        print(p.val)
        
def _reverseList(head): # create a new reverse list
    if head.next:
        p = head.next
        tail = Node(p.val)    
        tail.next = None   
        
        while p.next != None:  
            p = p.next
            curr = Node(p.val)
            curr.next = tail
            tail = curr
        
        curr = Node('zz')
        curr.next = tail
        tail = curr
            
        return tail

def _isPalindrome(head1, head2):
    
    flag = True
    while (head1 !=None and head2 != None):
        flag = False
        if head1.val != head2.val:
            return False
        
        else:
            flag = True
            head1 = head1.next
            head2 = head2.next
    return flag
     

head = _createLinkedList(arr)
_printList(head)
tail = _reverseList(head)
_printList(tail)
print(_isPalindrome(head,tail))
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    