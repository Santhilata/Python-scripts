# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 19:36:55 2020

@author: santhilata
"""


# find the middle in the linked list


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

def _get_middle(head):
    
    slow = head
    fast = head
    temp = slow
    
    while (fast != None and fast.next != None):
        temp = slow
        slow = slow.next
        fast = fast.next.next
        
    return temp

def _get_n_fromLast(head, n):
    
    slow = head
    count = 1
    temp = head
    while (count <= n and temp != None):
        count +=1
        temp = temp.next
        
      
    while (temp.next != None):
        
        slow = slow.next
        temp = temp.next
        
    return slow
    

arr = [1, 2.3, 4, 2, 3, 6, 11, 5, 8, 9, 10,13]  
#arr =[1]
print(arr)
head = _build_linkedlist(arr)

a = _get_middle(head)

print('middle: ', a.data)

b = _get_n_fromLast(head, 3)
print('n from last: ',b.data)