# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 18:10:26 2020

@author: santhilata
"""


# search for a value in the sorted array 

arr1= [1,3,2,6,4,7,8,9]
s1 = -8
s2 = 6
arr2 =[]


arr = sorted(arr1)
print(arr)
"""
print(arr)
pos = -1

for i in range(len(arr)):
    
    if arr[i] == s2:
        
        pos = i
        
print(pos)
"""
# binary search


low = 0
high = len(arr)-1

def _bsearch(arr, h,l, s):
    if (h-l) <= 0:   
        return -1
    
    mid = l +(h-l)//2

    if arr[mid] == s:
        return mid
    
    if  arr[mid] > s:
        return _bsearch(arr, mid,l, s)
        
    if  arr[mid] < s:
        return _bsearch(arr, h, mid+1, s)
        
        
    #return -1

a = _bsearch(arr, high, low, s2)        
    
print(a)