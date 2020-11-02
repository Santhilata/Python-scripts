# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 20:32:40 2020

@author: santhilata
"""


# Check whether inorder traversal of a tree is palindrome or not

class Tree:
    
    def __init__(self, data, left = None, right = None, level =0):
        
        self.data = data
        self.left = left
        self.right = right
        self.level = level
        
    def _set_level(self, level):
        self.level = level

def _inOrderTraversal(root):
    
    if root == None:
        return -1
    
    if root.left != None:
        
        _inOrderTraversal(root.left)
        
    print(root.data, end='->')
    
    if root.right != None:
        _inOrderTraversal(root.right)
 
def _preOrderTraversal(root)       :
    
    if root == None:
        return -1
    
    print(root.data, end='->')
    if root.left != None:
        _preOrderTraversal(root.left)
    if root.right != None:
        _preOrderTraversal(root.right)
        


# similarly write post order code also        
        
#test code
root = Tree(1)

root.left = Tree(2)
root.left.left = Tree(3)
root.left.right = Tree(17)

root.right = Tree(11)
root.right.left = Tree(7)
root.right.right = Tree(31)
    
_inOrderTraversal(root)  
print()
print('*******************')
_preOrderTraversal(root)  
print()
print('*******************')
