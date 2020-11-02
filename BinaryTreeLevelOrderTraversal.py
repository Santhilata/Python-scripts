# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 15:21:36 2020

@author: santhilata
"""
'''
Given a binary tree, return the level order traversal of its nodes’
 values. (ie, from left to right, level by level).
 For example: Given binary tree3,9,20,#,#,15,7
'''

class Tree:
    
    def __init__(self,val,level=0, left =None, right = None):
        self.val = val
        self.left = left
        self.right = right
        self.level = level
        
root = Tree(9)

root.left = Tree(4)
root.right = Tree(7)
root.left.left = Tree(8)
root.left.right = Tree(3)
root.right.left = Tree(5)

def _setLevelInOrder (root, level):
    
    if root is None:
        return
    
    _setLevelInOrder(root.left, level+1)
    
    root.level = level
    print(root.val, root.level)
    _setLevelInOrder(root.right, level+1)
    
_setLevelInOrder(root, root.level)

print('**************************')
def levelOrderTraversal(root):
    
    if root == None:
        return
    
    stack =[]
    
    stack.append(root)
    
    while len(stack)>0:
        
        node = stack.pop()
        print(node.val, node.level)
        
        if node.left is not None:
            stack.append(node.left)
        if node.right is not None:
            stack.append(node.right)
            
levelOrderTraversal(root)            
'''           
def _levelOrderTraversal(root):
    
    if root==None:
        return
'''   
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
    
    
    