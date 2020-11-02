# -*- coding: utf-8 -*-
"""
Created on Fri May  1 21:37:32 2020

@author: santhilata

 bloomberg-lp-interview-questions


Find the two elements that have the smallest difference in a given array.
"""

from itertools import combinations

num = list(map(int, input().rstrip().split()))



combi = list(combinations(num,2))


diff = sorted([(abs(c[0] - c[1]),( c[0], c[1]))  for c in combi ])
print(diff)
print(diff[0][1])