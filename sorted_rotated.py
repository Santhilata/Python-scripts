# -*- coding: utf-8 -*-
"""
Created on Tue May  5 17:36:24 2020

@author: santhilata
"""

arr = [ 40, 45,56, 66,77,99, 178, 200, 3, 4,  10, 12 ] 
arr = [250, 251, 252, 40, 45,56, 66,77,99, 178, 200]

# approach find the smallest element in O(n)

result = [arr[i+1] for i in range(len(arr)-1) if arr[i]> arr[i+1]]

#print(result[0])

#approach to do recursion


def find_smallest(arr, low, high):
    
    if (low > high):
        return arr[low]
    
    mid = (low+high)//2
    
    if (arr[mid] > arr[mid+1]):
        return arr[mid+1]
    
    if (arr[mid-1] > arr[mid]):
        return arr[mid]
    
    if ( arr[mid] > arr[high] ):
        return find_smallest(arr, mid+1, high)
    
    if (arr[low] > arr[mid]):
        return find_smallest(arr, low, mid-1)

#print(find_smallest(arr, 0,len(arr)-1))

def find_smallest2(arr, low, high):
    
    if low >high :
        return arr[low]
    
    mid = low + (high - low )//2
    
    if (arr[mid] > arr[mid+1]):
        return arr[mid+1]
    
    if (arr[mid-1] > arr[mid]):
        return arr[mid]
    
    if ( arr[mid] > arr[high] ):
        return find_smallest(arr, mid+1, high)
    
    if (arr[low] > arr[mid]):
        return find_smallest(arr, low, mid-1)


print(find_smallest2(arr, 0,len(arr)-1))