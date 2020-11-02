# -*- coding: utf-8 -*-
"""
Created on Tue May  5 21:54:57 2020

@author: santhilata

Recursion: Davis' Staircase
https://www.hackerrank.com/challenges/ctci-recursive-staircase/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=recursion-backtracking
"""




def stepPerms(n):
    
    if n==0:
        return 0
    
    if n==1 :
        return 1
    
    if n==2:
        return 2
    
    if n == 3:
        return 4
        
    
    
    return(stepPerms(n-1)+stepPerms(n-2)+stepPerms(n-3))
    

print(stepPerms(5))   

from collections import defaultdict

steps = defaultdict()
steps[1] = 1
steps[0] = 0
steps[2] = 2
steps[3] = 4
    
def stePerms_dp(n):
    
    if n in steps.keys():
        return steps[n]
    else:
        steps[n] = stePerms_dp(n-3)+stePerms_dp(n-2)+stePerms_dp(n-1)
        
    return steps[n]
    
    