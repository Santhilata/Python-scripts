# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 13:42:34 2020

@author: santhilata
"""

"""
Given an array S of n integers, are there elements a, b, c, and d in S 
such that a + b + c + d = target?  
Find all unique quadruplets in the array which gives the sum of target.
Note: Elements in a quadruplet (a,b,c,d) must be in non-descending order.
 (ie, a≤b≤c≤d) The solution set must not contain duplicate quadruplets.
 For example, given array S = {1 0 -1 0 -2 2}, and target = 0.
 A solution set is:(-1, 0, 0, 1)(-2, -1, 1, 2)(-2, 0, 0, 2)
"""

'''
approach:
    0. typical k sum problem. complexity is  n power k-1.
    1. sort the original array
    2. start  i1 with 0, i2 = i1+1
    3. k -> right pointer from len(s)-1
    4. a pointer to run from i2 to k
'''
s = [1,0, -1,0,-2,2]
s = sorted(s)
print(s)