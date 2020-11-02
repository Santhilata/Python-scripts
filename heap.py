# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 08:00:01 2020

@author: santhilata
"""


# Create max and min heaps

class Node:
    
    def __init__(self, val, left = None, right = None):
        
        self.val = val
        self.left = left
        self.right = right

arr = [1, 2.3, 4, 2, 3, 6, 11, 5, 8, 9, 10,13]  
#arr =[1]
print(arr)        
root = Node(arr[0])


    
