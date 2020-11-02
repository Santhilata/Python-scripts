# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 14:50:34 2020

@author: santhilata
"""

# Write a GetNth() function that takes a linked list and an integer index and returns the data value stored in the node at that index position.



class Node:
    
    def __init__(self, data):
        
        self.data = data
        self.next = None
        
def _build_linkedlist(arr):
    
    if len(arr) <1:
        head = None
    else:    
        head = Node(arr[0]) 
        curr = head
        for i in range(1, len(arr)):
            
            temp = Node(arr[i])
            curr.next = temp
            
            curr = temp
        
    return head

def _get_n(head, n):
    
    if head == None:
        return -1
    temp = head
    count = 0
    
    while (temp.next != None):
        temp = temp.next
        
        count += 1
        
        if (count == n-1):
            
            return temp.data
        
    return -1
arr = [1, 2.3, 4, 2, 3, 6, 11, 5, 8, 9, 10,13]  
arr =[1]
print(arr)
head = _build_linkedlist(arr)

a = _get_n(head,17)
print(a)