# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 12:41:10 2020

@author: santhilata
"""
"""
Given an array S of n integers, are there elements a, b, c in S 
such that a + b + c =0?
 Find all unique triplets in the array which gives the sum of zero.
 Note:  Elements in a triplet (a,b,c) must be in non-descending order. 
 (ie, a≤b≤c)
 The solution set must not contain duplicate triplets.
 For example, given array S = {-1 0 1 2 -1 -4},
 A solution set is:(-1, 0, 1)(-1, -1, 2)
"""

#arr = [(1,1,2),(1,1,2),(2,1,2)]

s = [-1,0,1,2,-1,-4]
s = sorted(s)
print(s)
result = []
'''
0. sort the array
1. initialize i =0 -> left pointer
2. j = i+1 -> one pointer ahead of i(left)
3. k = len(arr) -1 -> right pointer
'''

for i in range(len(s)-2):
    
    j = i+1
    k = len(s ) - 1
    
    if (i > 0 and s[i] == s[i-1]):
        continue
    
    while (j < k):
        if (k < len(s)-1 and s[k] == s[k+1]):
            k -= 1
            continue
        
        if s[i]+s[j]+s[k] > 0:
            k -=1
            
        elif s[i]+s[j]+s[k] < 0:
            j +=1
            
        else:
            result.append((s[i],s[j],s[k]))
            
            j+=1
            k -= 1
            
print(result)
    