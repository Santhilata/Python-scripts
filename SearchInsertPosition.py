# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 18:33:33 2020

@author: santhilata
"""
"""
Given a sorted array and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order. 
You may assume no duplicates in the array.
Here are few examples.
[1,3,5,6], 5 -> 2
[1,3,5,6], 2 -> 1
[1,3,5,6], 7 -> 4
[1,3,5,6], 0 -> 0
"""

#search the location. complexity O(n)

def _bruteforce(arr, num):
    i = 0
    while i < len(arr) :
        
        if arr[i] == num:
            return i
        if  arr[i] > num:
            break
        if arr[i] < num:
            i =i+1
    
    if  i ==0:
        return 0
    
    return i
       
arr = [1,3,5,6]            
num =4

#print(_bruteforce(arr,num))


#Using binary search. complexity = O(log(n))

def _searchInsert(arr, num): # without recursion
    
    l = 0
    r = len(arr) -1
    
    if num> arr[r]:
        return r+1
    
    while (l < r):
        
        mid = l + (r-l)//2
        if num==arr[mid]:
            return mid
        if num > arr[mid]:
            l = mid+1
            
        else:
            r = mid
            
    return l

#print(_searchInsert(arr, num))
        
def _searchBST(arr, num, l,r) : # with recursion
    
    if len(arr) == 0:
        return len(arr)   
    
    
    if (l >= r) :
        if num > arr[l]:
            return len(arr)
        else:
            return l
    
    mid = l+(r-l)//2
    
    if arr[mid] == num:
        return mid
    
    if num > arr[mid]:
        return _searchBST(arr, num, mid+1,r)
        
    else:
        return _searchBST(arr, num, l, mid)
    
    
print(_searchBST(arr, num,0, len(arr)-1))   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    