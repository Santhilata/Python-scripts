# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 16:12:42 2020

@author: santhilata
"""


# Given an array nums, write a function to move all 0’s 
# to the end of it while maintaining the relative order 
# of the non-zero elements. 
# For example, given nums = [0,1,0,3,12], 
# after calling your function, nums should be [1,3,12,0,0]


nums = [1, 0,1,0,3,12]

def _move_zeros(nums):
    # Keep two indices 
    i = 0 # relative position of next 0
    j = 0 
    
    while (j < len(nums)):
        
        if (nums[j] == 0):
            
            j += 1
            
        else:
            nums[i] = nums[j]
            i += 1
            j += 1
            
    while( i < len(nums)):
        
        nums[i] = 0
        i += 1
        

    return nums

nums = _move_zeros(nums)            

print(nums)
        