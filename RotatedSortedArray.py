# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 21:26:39 2020

@author: santhilata
"""
'''
Suppose a sorted array is rotated at some pivot unknown to you beforehand. 
(i.e.,0 1 2 4 5 6 7might become4 56 7 0 1 2).Find the minimum element.
You may assume no duplicate exists in the array.

'''
arr = [10,10,11,12, 4, 4 ,5,5,6, 7, 8,9]
def _bruteForce(arr): #o(n)
    for i in range(1,len(arr)): 
        
        if arr[i-1]> arr[i]:
            return arr[i]

def _binarySearch(arr, l, r):
    
    if len(arr)==0:
        return -1
    
    mid = l+(r-l)//2
    if arr[mid-1] > arr[mid]:
        return arr[mid]
    
    if arr[mid] > arr[mid+1]:
        return arr[mid+1]
    
    if arr[mid] > arr[r]:
        return _binarySearch(arr, mid+1, r)
    
    if arr[mid] < arr[r]:
        return _binarySearch(arr, l,mid)
    
def _binarySearch_iteration(arr):
    
    if len(arr) == 0:
        return -1
    l = 0
    r = len(arr)-1
    
    while (l < r):
        
        mid = l +(r-l)//2
        
        if arr[mid-1] > arr[mid]:
            return arr[mid]
    
        if arr[mid] > arr[mid+1]:
            return arr[mid+1]
        
        if arr[mid] > arr[r]:
            l = mid+1
            
        elif arr[mid] < arr[r]:
            r = mid
    return -1

print(_bruteForce(arr))
print(_binarySearch(arr, 0, len(arr)-1))
print(_binarySearch_iteration(arr))

'''
Find the minimum in the rotated array with duplicates
'''
arr = [10,10,4,5,5,6,9]
# get the list of the set and find minimum













