# -*- coding: utf-8 -*-
"""
Created on Tue May  5 16:14:23 2020

@author: santhilata

Find the starting point of the array in a rotated array

example [6,7,8,0,1,2,3,4,5]
"""

arr = [6,7,8,0,1,2,3,4,5]
arr =[5,6,7,8,0,1,2,3,4]

def find_start(arr, low, high):
    if high < low: 
        return arr[0] 
    
    if (high == low):
        return arr[low]
    
    mid = (high+low)//2
    
    if (mid <high  and arr[mid] > arr[mid]+1):
        return arr[mid+1]
    
    if (mid > low and arr[mid] < arr[mid-1]):
        return arr[mid]
    
    if arr[high] > arr[mid]:
        return find_start(arr,low,mid-1)
    
    return find_start(arr,mid+1,high)

print(arr.index(find_start(arr,0,len(arr)-1)))