# -*- coding: utf-8 -*-
"""
Created on Sat May  2 13:07:54 2020

@author: santhilata

Given an array a, return the indices i,j that minimize |a_i -a_j|
"""

from itertools import combinations

arr = [23, 45, 3, -9,0, 43, 22, 8432, 13,-77]

combo = list(combinations(arr,2))



#re  = 0

re =sorted([(abs(i[0] -i[1] ),arr.index(i[0]), arr.index(i[1]) ) for i in combo])

print(re[0][1],re[0][2] )

