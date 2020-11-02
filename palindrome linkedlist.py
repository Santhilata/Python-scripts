# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 10:22:57 2020

@author: santhilata
"""


# slow pointer fast pointer

class Node:
    
    def __init__(self, data):
        
        self.data = data
        self.next = None
        
def _build_linkedlist(arr):
    
    head = Node(arr[0]) # assumption there is  atleast one node
    curr = head
    for i in range(1, len(arr)):
        
        temp = Node(arr[i])
        curr.next = temp
        
        curr = temp
        
    return head

# reverse linked list    
def _reverse_linked_list(head):   
    
    prev = head
    temp = prev.next
    
    
    
    while (temp != None ):
        
        curr = temp.next
        temp.next = prev
        prev = temp
        temp = curr
        
    head.next = None
    head = prev

    return head

def _print_ll(head):
    
    while (head != None):
        print(head.data,  end= '->')
        
        head = head.next
    print('null')


def get_middle_tail(head):
    
    slow = head
    fast = head
    tail = head
    
    if (slow == None):
        return True
       
    while( fast != None and fast.next != None):
        
        tail = fast.next
        fast = fast.next.next        
        slow = slow.next
    
    if fast != None:
        tail = fast
        #print(fast.data)
    else:
        
        print('fast is null')
    
    print('mid: ',slow.data)    
    print('tail: ', tail.data)
    
    return slow, tail


def _is_ll_palindrome(head):
    
    if head == None:
        return True
    
    mid, tail = get_middle_tail(head)
    
    #reverse 2nd half 
    print(mid.data, tail.data)
    
     
    second_head = _reverse_linked_list(mid.next)
    
    print(second_head.data)
    print(tail.data)
    
    prev = head
    
    
    while (prev != None):
        
        if prev.data == tail.data:
            prev = prev.next
            tail = tail.next
            
        else:
            return False
        
    return True
        
    
    
    
    

# Testing
arr = [1, 2.3, 4, 2, 3, 6, 11, 5, 8, 9, 10,13]  

arr = [1,2,3,4,5]

head = _build_linkedlist(arr)  
_print_ll(head)

head = _reverse_linked_list(head)
_print_ll(head)
#print(head.data)

get_middle_tail(head)
    
_is_ll_palindrome(head)   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        