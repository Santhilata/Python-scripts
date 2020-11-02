# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 21:33:29 2020

@author: santhilata
"""
#Given an array of n positive integers and a positive integer s,
# find the minimal length of a subarray of which the sum≥s.
# If there isn’t one, return 0 instead.
#For example, given the array [2,3,1,2,4,3] and s =7, 
#the subarray [4,3] has the minimal length of 2 under the problem constraint.


def _find_min(arr, s):
    
    result = len(arr)
    exists = False
    left =0
    right = 0
    
    sum = 0
    
    while right < len(arr):        
        
        if sum >= s:
        
            exists = True
            
                      
            print(right, left, sum)
            result = min(result, (right-left))
            
            sum = sum - arr[left]
            left +=1
            
        else:
            
            
            sum = sum + arr[right]
            right +=1
            
            
    if exists:
        return result
    else:
        return -1

arr = [2,3,1,2,4,3]
s = 7
a = _find_min(arr, s)
print(a)