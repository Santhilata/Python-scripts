# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 23:47:40 2020

@author: santhilata
"""
"""
Given an unsorted array of integers, find the length of longest increasing 
subsequence. For example, given [10,9,2,5,3,7,101,18], 
the longest increasing subsequence is [2,3,7,101].  Therefore the length is 4
"""

# Naive method
import numpy as np

arr = [10,9,2,5,3,7,101,18]

def _lis_naive(arr):
    
    if len(arr)==0:
        return [0]
    
    result = np.zeros((len(arr)))    
    
    for i in range(len(arr)-1):
        result[i] = 1
        
        for j in range(i):
            
            if arr[i] > arr[j]:
                
                result[i] = max(result[i], result[j]+1)
    
    print(result)
    max_val =  max(result)
    
    return max_val
    
print(_lis_naive(arr))

# binary search method

def _binarySearch(arr): # log(n)
    if len(arr) == 0:
            return 0
    if len(arr) == 1:
        return 1
    
    result = []
   
    for num in range(len(arr)):
        
        if len(result) == 0 or num> result[-1]:
            result.append(num)
        
        
        l = 0
        r= len(result) -1
        while (l < r):
            
            mid = l + (r-l)//2
            
            if result[mid] < num:
                l = mid+1
                
            else:
                r = mid
                
        result.append(r)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        