# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 17:26:26 2020

@author: santhilata
"""
'''
Find length of longest path in the matrix with consecutive characters.

Given MxN matrix of characters, find the length of the longest path in the matrix 
starting from a given character. All characters in the longest path should be 
increasing and consecutive to each other in alphabetical order.

We are allowed to search the string in all eight possible directions 
i.e, N,E,W,S,NE,SE,NW,SW

Example, matrix :
    [D,E,H,X,B]
    [A,O,G,P,E]
    [D,D,C,F,D]
    [E,B,E,A,S]
    [C,D,Y,E,N]
length of the longest path with consecutive characters starting from character C is 6

The longest path is c(2,2)->D(2,1)->E(3,2)->F(2,3)->G(1,2)->H(0,2)
'''

# All possible movements
row = [-1,-1,-1,0,0,1,1,1]
col = [-1,0,1,-1,1,-1,0,1]

def _isvalid(x,y):
    return 0 <= x<M and 0 <= y < N

# Find length of longest path in the matrix mat with consecutive characters
# The path should continue from the previous character
# (i,j) denote the coordinates of the current cell
def findMaxlength(mat, x,y, previous):
    #base case
    if not _isvalid(x,y) or chr(ord(previous)+1) != mat[x][y]:
        return 0
    
    max_len = 0 # maximum length
    
    # recur for all 8 adjacent cells from the current cell
    
    for k in range(8):
        length = findMaxlength(mat, x+row[k],y+col[k], mat[x][y])
        
        max_len = max(max_len, 1+length)
    
    return max_len

def findMaximumLength(mat,ch):
    max_len = 0
    
    #traverse the matrix
    for x in range(M):
        for y in range(N):
            # start from the current cell if its value matches with the given character
            if mat[x][y] ==ch:
                # recur from all 8 adjacent cells from the current cell
                for k in range(8):
                    length = findMaxlength(mat, x+row[k], y+col[k], ch)
                    
                    max_len = max(max_len, 1+length)
    
    return max_len
                    
    
if __name__ == '__main__':
    mat =[
        ['D','E','H','X','B'],
        ['A','O','G','P','E'],
        ['D','D','C','F','D'],
        ['E','B','E','A','S'],
        ['C','D','Y','E','N']
        ]
    
    # size of the given matrix
    (M,N) = (len(mat), len(mat[0]))
    
    #starting character
    ch = 'C'
    
    print('from ',ch, 'is',findMaximumLength(mat,ch))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    