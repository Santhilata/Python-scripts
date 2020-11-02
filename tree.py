# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 11:42:34 2020

@author: santhilata
"""

class Node:
    
    def __init__(self, data, left = None, right = None):
        
        self.data = data
        self.left = left
        self.right = right  
        
    def _printTree(self):
        
        if self.left != None:
            self.left._printTree()
            
        print(self.data)
        
        if self.right != None:
            self.right._printTree()


    def _insert(self, node):
        
        if node.data < self.data:
            if self.left != None:
                self.left._insert(node)
            else:
                self.left = node
                
        else:
            if self.right != None:
                self.right._insert(node)
            else:
                self.right = node

def _traverseBST(root):
    
    if (root == None):
        return None
    
    if root.left != None:
        _traverseBST(root.left)
        
    print(root.data)
    
    if root.right != None:
        _traverseBST(root.right)

def _countNodes(root):
    """
    if root == None:
        return 0
    else:
        
        return _countNodes(root.left) +_countNodes(root.right)+1
    """
    
    count = 1
    if root == None:
        return 0
    
    if root != None:
        if root.left != None:
            count += _countNodes(root.left)
        if root.right != None:
            count += _countNodes(root.right)
            
    return count
        
    
  
def _buildBST(root, arr):
    # assume the input contains all integers non repeated
    
    for i in range(len(arr)):
        
        root._insert(Node(arr[i]))
    
    return root




tree = Node(1)

_buildBST(tree, [0.5, 3, 4, 2.5, 11, 10])

_traverseBST(tree)

print(_countNodes(tree))