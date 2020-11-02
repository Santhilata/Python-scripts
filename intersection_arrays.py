# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 11:37:56 2020

@author: santhilata
"""


# Intersection of two arrays

arr1 = [2,3,7,8]
arr2 = [4,5,3,2, 1]

result = set()
arr1 = sorted(list(set(arr1)))
arr2 = sorted(list(set(arr2)))



for i in range(len(arr2)):
    
    if arr2[i] in arr1:
        result.add(arr2[i])
    
print(list(result) )  