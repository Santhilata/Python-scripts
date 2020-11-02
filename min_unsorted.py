# -*- coding: utf-8 -*-
"""
Created on Tue May  5 20:23:57 2020

@author: santhilata

Find min/max in an unsorted array
"""

arr = [ 40, 77, 2, 45, 4, 10, 56, 66, 3 ] 


def get_min(arr): #O(n)
    mini = 99999
    for i in arr:
         if i < mini:
             mini=i
             
    return mini
print(get_min(arr))




