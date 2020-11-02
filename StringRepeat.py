# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 16:09:23 2020

@author: santhilata
"""


def repeatedString(s, n):

    return(s.count("a") * (n // len(s)) + s[:n % len(s)].count("a"))
    
        
    

if __name__ =='__main__':
    s = input()

    n = int(input())

    result = repeatedString(s, n)
    print(result)