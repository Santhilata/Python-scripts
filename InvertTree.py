# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 13:34:25 2020

@author: santhilata
"""


class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.data = val
        

def invertTree(root):
    if root == None:
            return None
    
    right = invertTree(root.right)
    left = invertTree(root.left)  
    
    
    root.left = right
    root.right = left
    
    return root
            
def _printTree(root):
        
        if root.left != None:
            _printTree(root.left)
            
        print(root.data)
        
        if root.right != None:
            _printTree(root.right)
            
            
root = Node(4)
root.left = Node(2)
root.left.left = Node(1)
root.left.right = Node(3)
root.right = Node(7)
root.right.left = Node(6)
root.right.right = Node(9)
_printTree(root)

invertTree(root)
_printTree(root)