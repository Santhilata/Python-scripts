# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 22:03:15 2020

@author: santhilata
"""
'''
Binary Tree Preorder Traversal
Preorder binary tree traversal is a classic interview problem. 
The key to solve this problem is using a stack tostore left and right
 children, and push right child first so that it is processed after the
 left child
'''

class Tree:
    
    def __init__(self,val, left =None, right = None):
        self.val = val
        self.left = left
        self.right = right
        
root = Tree(9)

root.left = Tree(4)
root.right = Tree(7)
root.left.left = Tree(8)
root.left.right = Tree(3)
root.right.left = Tree(5)

def _isleaf(node)       :
    
    if node.left == None and node.right ==None:
        return True
    else:
        return False
    
    
def _preOrderTraversal(root): #non recursive method
    
    if root is None:
        return
    
    nodeStack = []
    nodeStack.append(root)
    
    while (len(nodeStack)>0):
        
        node = nodeStack.pop()
        print(node.val, end=' ')
        
        if node.right is not None:
            nodeStack.append(node.right)
        if node.left is not None:
            nodeStack.append(node.left)
    print('******************************************')  
_preOrderTraversal(root)

def preOrderTraversal(root): #recursive method
    
    if root is None:
        return
    
    print(root.val,end = ' ')
    
    if root.left is not None:
        preOrderTraversal(root.left)
    if root.right is not None:
        preOrderTraversal(root.right)
    
    
preOrderTraversal(root)
print('******************************************')


def _inOrderTraversal(root): # non recursive method
    
    if root is None:
        return
    
    current = root
    stack = []
    
    while current != None:
        stack.append(current)
        current = current.left
        
    while (len(stack ) >0):
        
        t = stack.pop()
        print(t.val, end = ' ')
        
        t = t.right
        while(t is not None):
            stack.append(t)
            t = t.left
            
            
    print('******************************************')
    
_inOrderTraversal(root)

def inOrderTraversal(root): # recursive
    
    if root is None:
        return
    
    inOrderTraversal(root.left)
    print(root.val, end = ' ')
    inOrderTraversal(root.right)
    
inOrderTraversal(root)
print('******************************************')

def peek(stack):
    if stack:
        return stack[-1]
    return None

def _postOrderTraversal(root)  :
    
    if root is None:
        return
        
    stack = []
    stack.append(root)
    
    while len(stack) > 0:
        curr = peek(stack)
                
        if curr.left is None and curr.right is None:
            t = stack.pop()
            print(t.val, end=' ')
            
        else:
            if curr.right is not None:
                stack.append(curr.right)
                curr.right = None
                
            if curr.left is not None:
                stack.append(curr.left)
                curr.left = None
            
    print('******************************************')
_postOrderTraversal(root)


root = Tree(9)

root.left = Tree(4)
root.right = Tree(7)
root.left.left = Tree(8)
root.left.right = Tree(3)
root.right.left = Tree(5)

def postOrderTraversal(root): # recursive method
    
    if root is None:
        return
    
    
    postOrderTraversal(root.left)
    
    postOrderTraversal(root.right)
    print(root.val,end = ' ')

postOrderTraversal(root)

print('******************************************')
























        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        