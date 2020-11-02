# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 18:53:30 2020

@author: santhilata
"""
'''
Group Anagrams
Given an array of strings, return all groups of strings that are anagrams.
An anagram is a type of word play, the result of rearranging the letters
 of a word or phrase to produce a new word or phrase, using all the original
 letters exactly once; for example, Torchwood can be rearranged into 
 Doctor Who
'''

arr = ['ana','aan','bcd','iamlordvoldemort','dcb','cdb','szs','dbc','bdc','cbd','naa','zss',
       'tommarvoloriddle']

def _groupAnagrams(arr):
    
    result = {}
    
    for st in arr:       
        
        chArr = [0]*26
        
        for ch in st:
            chArr[ord(ch) -97] += 1
        
        k = ''    
        for ch in chArr:
            k = k +str(ch)
        print( k)
            
        if k in result.keys():
            result[k].append(st)
            
        else:
            result[k] = [st]
            
    return result
        
result = _groupAnagrams(arr)

for key, val in result.items():
    
    for st in val:
        print(st,end=',')
        
    print()