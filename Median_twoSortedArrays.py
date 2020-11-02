# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 20:04:34 2020

@author: santhilata
"""
"""
There are two sorted arrays A and B of size m and n respectively. 
Find the median of the two sorted arrays. The overall run time complexity 
should be O(log (m+n)).
"""

'''
Solution:
    1. Median is the middle value of the combined values of two arrays
    2. merge two sorted arrays and get the middle value
'''
import numpy as np
B = [2,3,5,7,8]
A = [1,2,3,4,6,7,9,10]


def _merge_sorted_arrays(A,B): # O(m+n)
    
    
    m = len(A)
    n = len(B)
    A.extend(np.ones((len(B))))
    
    while (m > 0 and n > 0):
        
        if A[m-1] > B[n-1]:
            A[m+n-1] = A[m-1]
            m -= 1
            
        elif A[m-1] < B[n-1]:
            A[m+n-1] = B[n-1]
            n -= 1
            
        else: # equal condition
            A[m+n-1] = A[m-1]
            A[m+n-2] = B[n-1]
            
            m -=1
            n -=1
            
    while n >0:
        A[m+n-1] = B[n-1]
        n -= 1
    return A[len(A)//2]

#print(_merge_sorted_arrays(A,B))

def _getMiddle(A):
    if len(A)%2 == 1:
        return len(A)//2, A[len(A)//2]
    else:
        return len(A)//2-1, A[len(A)//2-1]

def _median(A,B):
    
    m = len(A)
    n = len(B)
    
    while (m >1 and n>1):
        
        ind_A, medA = _getMiddle(A)
        
        ind_B, medB = _getMiddle(B)
        print(medA,medB)
        
        if medA > medB:
            
            A = A[:ind_A+1]
            B = B[ind_B+1:]
            
        elif medB > medA:
            A = A[ind_A+1:]
            B = B[:ind_B+1]
            
        else:
            return (medA+medB)//2
        
        m = len(A)
        n = len(B)
        print(A,B)
        
    if m==1 and n>1:
        
        median =( A[0]+B[len(B)//2])//2
    elif n ==1 and m>1:
        median = (A[len(A)//2]+B[0]) //2
        
    else:
        median = (A[0]+B[0])//2
        
    return median

A = [2,3,7,8]
B = [1,4,5,9,10]

p = _median(A,B)

print(p)














