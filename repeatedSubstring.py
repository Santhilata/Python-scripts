# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 09:01:59 2020

@author: santhilata
"""
"""
Given two strings A and B, find the minimum number of times A has to be 
repeated such that B is a substring of it. 
If no such solution, return -1.
For example, with A = "abcd" and B = "cdabcdab".
Return 3, because by repeating A three times (“abcdabcdabcd”),
 B is a substring of it; and B is not a substringof A repeated two 
 times ("abcdabcd").
 Note: The length of A and B will be between 1 and 10000.
"""

A = "abcd"
B = "cdabcdab"
count = 1

while B not in A:
    
    A = A + A
    count += 1
    
print( count)

    
