# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 22:17:13 2020

@author: santhilata
"""
'''
Serialization is the process of converting a data structure or object into a sequence of bits 
so that it can be stored in a file or memory buffer, or transmitted across a network connection
 link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction 
on how your serialization/deserialization algorithm should work. You just need to ensure
 that a binary tree can be serialized to a string and this string can be deserialized to
 the original tree structure.
 
 [1,2,3,null,null,4,5]
'''

class Tree :
    
    def __init__(self, val, left=None, right=None):
        
        self.val = val
        self.left = left
        self.right = right
        
root = Tree(1)
root.left = Tree(2)
root.right = Tree(3)
root.right.left = Tree(4)
root.right.right = Tree(5)


def _serialize(root, out):
    
    if root == None:
        out.append('null')
        return out
    
    
    out.append(root.val)
    _serialize(root.left, out)
    _serialize(root.right, out)


out = []
_serialize(root, out)
print(out)




def _deserialize( out):
    val = next(out)
        
    if  val == 'null' :
        return None
        
    root = Tree(val)    
    root.left = _deserialize(out)    
    root.right = _deserialize( out)
    
    return root
    
    
     
out = iter(out)
root =_deserialize( out)        


def preOrderTraversal(root): #recursive method
    
    if root is None:
        return
    
    print(root.val,end = ' ')
    
    if root.left is not None:
        preOrderTraversal(root.left)
    if root.right is not None:
        preOrderTraversal(root.right)
    
    
preOrderTraversal(root)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    