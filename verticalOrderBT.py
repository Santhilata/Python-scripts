#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 10:54:14 2020

@author: santhilataKV
"""

'''
Given a binary tree, return the vertical order traversal of its nodes values.

For each node at position (X, Y), its left and right children respectively will be
at positions (X-1, Y-1) and (X+1, Y-1).

Running a vertical line from X = -infinity to X = +infinity, whenever the vertical
line touches some nodes, we report the values of the nodes in order from top to bottom
(decreasing Y coordinates).

If two nodes have the same position, then the value of the node that is reported first
is the value that is smaller.

Return an list of non-empty reports in order of X coordinate.  Every report will have a list
of values of nodes.


Input: [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Explanation:
Without loss of generality, we can assume the root node is at position (0, 0):
Then, the node with value 9 occurs at position (-1, -1);
The nodes with values 3 and 15 occur at positions (0, 0) and (0, -2);
The node with value 20 occurs at position (1, -1);
The node with value 7 occurs at position (2, -2).
'''

arr = [3,9,20,'null','null',15,7]
arr = [3,9,'null','null',20,15,'null','null',7,'null','null']

class Node:

    def __init__(self,val,left = None, right = None,x=0,y=0 ):
        self.val = val
        self.left = left
        self.right = right
        self.x = x
        self.y = y




def preOrderTraversal(root,x,y): #recursive method

    if root is None:
        return

    root.x = x
    root.y = y
    print(root.val,root.x, root.y ,end = '; ')

    if root.left is not None:
        preOrderTraversal(root.left, x-1, y-1)
    if root.right is not None:
        preOrderTraversal(root.right,x+1, y-1)


#


def _buildTree(arr):

    val = next(arr)


    if  val == 'null'  :
        return None

    root = Node(val)
    root.left = _buildTree(arr)
    root.right = _buildTree( arr)

    return root

arr = iter(arr)
root = _buildTree(arr)
preOrderTraversal(root,0,0)



def _printVertical(node, dist,dict):

    if node is None:
        return

    _printVertical(node.left, dist-1, dict)
    dict.setdefault(dist,[]).append(node.val)

    _printVertical(node.right, dist+1, dict)

dict = {}
_printVertical(root,0,dict)

result = []
for value in dict.values():
    print(value)
    result.append(value)

print(result)



