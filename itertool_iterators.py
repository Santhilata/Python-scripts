# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 22:31:57 2020

@author: santhilata
"""

from itertools import combinations

n1 = int(input())

l = list(input().split())

n2 = int(input())

combo = list(combinations(l,n2))
 
count = 0
for c in combo:
    if 'a' in c:
        count +=1
print((count*1.0)/len(combo))
     