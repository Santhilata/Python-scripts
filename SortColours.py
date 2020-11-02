# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 18:30:50 2020

@author: santhilata
"""
'''
Given an array with n objects colored red, white or blue, 
sort them so that objects of the same color are adjacent,
with the colors in the order red, white and blue.
Here, we will use the integers 0,1, and 2 to represent the 
color red, white, and blue respectively.
'''
from collections import Counter
arr =[0,1,2,1,1,2,0,1,0,2,1,2,0,1]

t = Counter(arr)

start = 0
for key,val in t.items():
    
    for i in range(val):
        arr[start+i] = key
    start += val

print(arr)