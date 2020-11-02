# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 10:00:07 2020

@author: santhilata
"""
"""
Write a function that takes a string as input and reverse only the vowels of a string.
"""
# assume: all lowercase

s = ['s','a','n','a','t','h','i','l','u']
def _reverseVowels(s):
    
    vowel_list = ['a','e','i','o','u']
    
    i = 0
    j = len(s) - 1
    
    while (i < j):
        
        if s[i] not in vowel_list:
            i += 1
            print(s[i])
            continue
            
        if s[j] not in vowel_list:
            j -= 1
            print(s[j])
            continue
        
        
        temp = s[i]
        s[i] = s[j]
        s[j] = temp
        
        i += 1
        j -= 1

_reverseVowels(s)        
print(s)