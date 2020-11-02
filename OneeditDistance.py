# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 20:56:59 2020

@author: santhilata
"""

"""
Given two strings S and T, determine if they are both one edit distance apart
"""


# S and T are not of same length

def _oneEditDistance(S,T):

    if S == None or T == None:
        return False
    
    if abs(len(S) - len(T)) != 1:
        
        return False
    
    count = 0
    length = len(S) if len(S) < len(T) else len(T)
    
    for i in range(length):
        
        if S[i] != T[i]:
            count = count+1
            
        if i==len(S)-1 and count != 0:
            return False
        
        if i == len(T)-1 and count != 0:
            return False
        
        
    
    return True   

S= 'aaab'        
T = 'acb'
        
print(_oneEditDistance(S,T)    )
