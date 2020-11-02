# -*- coding: utf-8 -*-
"""
Created on Wed May  6 11:31:00 2020

@author: santhilata

find the elements in the array and print a minimum continuously
"""


arr = [77, 22, 53, 46,13, 42,56, ]


mini = 999999
for  idx, val in enumerate(arr):
    
    if (val < mini):
        mini = val
        
        print('current min:', val)