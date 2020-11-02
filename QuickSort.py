# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 16:48:31 2020

@author: santhilata
"""
'''
Quicksort  is  a  divide  and  conquer  algorithm.   It  first  divides
  a  large  list  into  two  smaller  sub-lists  and  then
  recursively sort the two sub-lists.
  If we want to sort an array without any extra space, 
  quicksort is a good option.
  On average, time complexity is O(n log(n)).
  The basic step of sorting an array are as follows:
      •  Select a pivot
      •  Move smaller elements to the left and move bigger elements
      to the right of the pivot
      •  Recursively sort left part and right part
'''

# Version1 : right most elementt as pivot

arr = [4,5,1,2,3,3]

def partition(arr, start, end):
    pivot = arr[-1]
    
    for i in range(start, end):
        if arr[i] < pivot:
            
            temp = arr[start]
            arr[start] = arr[i]
            arr[i] = temp
            
            start += 1
    temp = arr[start]
    arr[start] = pivot
    arr[end] = temp
    
    return start

def _quickSort(arr, start, end):
    
    part = partition(arr, start,end)
    
    if part-1 > start:
        _quickSort(arr,start, part-1)
        
    if partition+1 > end:
        _quickSort(arr, part+1, end)
