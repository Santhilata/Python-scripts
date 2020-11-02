# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 21:21:05 2020

@author: santhilata
"""


"""
Given two sorted integer arrays A and B, merge B into A as one sorted array.
Note:  You may assume that A has enough space to hold additional elements from B.
 The number of elements initialized in A and B are m and n respectively.
"""

'''
Solution:
    1. compare elements from the bottom
    2. add elements at the appropriate position
    3. add extra elements if any
'''
import numpy as np
B = [2,3,7,8]
A = [1,4,6,9,10]

m = len(A)
n = len(B)

A.extend(np.ones((n))) # extend A to fit B


while (m > 0 and n > 0):
    
    if A[m-1] < B[n-1]:
        
        A[m+n-1] = B[n-1]
        n -= 1
        
    else:
        A[m+n-1] = A[m-1]
        m -= 1
        
while(n >0):
    A[m+n-1] = B[n-1]
    n  -= 1
        
print(A)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
