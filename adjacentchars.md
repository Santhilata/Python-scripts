# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 21:34:34 2020

@author: santhilata
"""
'''
Given a string S, check if the letters can be rearranged so that two characters that are adjacent
 to each other are not the same.

If possible, output any possible result.  If not possible, return the empty string.
'''
st1 ='aaab'
st2 ='abcaa'

from collections import Counter
def _adjacentChar(st):
    
    counter_st = Counter(st)
    
    for key, val in counter_st.items():
        if val > len(arr)//2+1:
            
            return ''
        
    pos = 0
    i=1
    while i < len(st):
        
        if st[i] == st[i-1]:
            
    
            



