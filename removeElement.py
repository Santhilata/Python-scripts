#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 21:28:35 2020

@author: santhilataKV
"""
'''
Given an array and a value, remove all instances of that value in place and return the new length. 
(Note: The
order of elements can be changed. It doesn’t matter what you leave beyond the new length.)
'''

arr1= [1,1,1,2,2,3]
arr2=[]

arr = arr1
num= 2

pos = 0
i=0

while (i <len(arr)):
    
    if arr[i] != num:       
        arr[pos] = arr[i]
        pos +=1
        
    i = i+1
        
         
        
print(arr[:pos])