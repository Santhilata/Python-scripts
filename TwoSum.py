# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 12:21:21 2020

@author: santhilata
"""
"""
Given an array of integers, find two numbers such that they add up to a specific 
target number.

The function twoSum should return indices of the two numbers such that they add
 up to the target, where index1 must be less than index2.
 Please note that your returned answers (both index1 and index2) are not 
 zero-based.
 
 Input: numbers={2, 7, 11, 15}, target=9
Output: index1=0, index2=1
"""
numbers=[1, 2, 7,8, 11, 15]
target=9
flag = False

left = 0
right = len(numbers)-1

while (left < right):
    
    if numbers[left]+numbers[right] < target:
        left += 1
        
    elif numbers[left]+numbers[right] > target:
        right -= 1
        
    elif numbers[left]+numbers[right] == target:
        print(left, right)
        flag = True
        break
        
if  not flag:
    print('No solution')
        
