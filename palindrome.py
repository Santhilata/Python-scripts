# -*- coding: utf-8 -*-
"""
Created on Fri May  1 14:27:37 2020

@author: santhilata
"""

def palindrome(text):
    l  = len(text)
    
    flag = True
    
    for i in range(l//2):
        if text[i] == text[l-i-1]:
            flag = True
        else:
            flag = False
            break
    if (flag):
        print('Palindrome')
    else:
        print('Not a  Palindrome')

palindrome('babaabab')