# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 16:27:55 2020

@author: santhilata
"""
'''
Write a function to find the longest common prefix string amongst
 an array of strings.
 
 Input: ["flower","flow","flight"]
Output: "fl"

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''



Input = ["flower","flow","flight"]

def _longestCommonPrefix(Input):
    min_str = ''
    min_len = 9999999
    
    
    for st in Input:
        if len(st) < min_len:
            min_len = len(st)
            min_str = st
            
    for i in range(min_len, 0, -1):  
        found = True
        for st in Input:
            if st[:i] != min_str[:i]:
                found = False
                break
           
        if  found:
            min_len = i
            min_str = min_str[:i]
            
            break
    return min_len, min_str

a, st = _longestCommonPrefix(Input)
print(a, st)