# -*- coding: utf-8 -*-
"""
Created on Tue May  5 17:24:03 2020

@author: santhilata

Given a sorted array arr[] of n elements, 
write a function to search a given element x in arr[].
"""

arr = [ 2, 3, 4, 10, 40 ] 
x = 10

#o(n) is the linear search

result = [arr.index(i) for i in arr if i == x ]
print(result[0])

#o(log n) - binary search

arr = [ 1, 2, 3, 4, 10, 40 ] 
x = 10

def bst(arr,x, low, high):
    
    
    
    if (low == high):
        return low
    
    mid = (low+high)//2
    
    if arr[mid]==x:
        return mid
    
    if (arr[mid] < x):
         return bst(arr,x,mid+1,high)
    else:
         return bst(arr, x, low, mid-1)
     
    return -1
         
print(bst(arr,x,0,len(arr)-1))    
         
    
    