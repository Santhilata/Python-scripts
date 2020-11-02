# -*- coding: utf-8 -*-
"""
Created on Tue May  5 22:28:12 2020

@author: santhilata

Arrays: Left Rotation
https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
"""

def rotLeft(a,d):
    
    if d > len(a):
        return a  
    
    
    a1 = list()
    a1.extend(a[d:])
    a1.extend(a[:d])
    
    
    return a1

a = [1,2,3,4,5]
d=2

print(rotLeft(a,d))
    
    