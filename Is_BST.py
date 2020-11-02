# -*- coding: utf-8 -*-
"""
Created on Wed May  6 08:58:13 2020

@author: santhilata

Is this a BST?


"""
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        

class BST:
    def __init__(self, root):
        self.root = root

    def  is_a_BST(root):
        
        if (root == None):
            return True
        
        if (root.left != None and root.data > root.left.data):
            return is_a_BST(root.left)
        
        if (root.right != None and root.data  < root.rigth.data):
            return is_a_BST(root.right)
        
        return False