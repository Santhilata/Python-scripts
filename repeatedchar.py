# -*- coding: utf-8 -*-
"""
Created on Wed May  6 13:12:24 2020

@author: santhilata

Given a binary matrix of 0 and 1 where we can move in 4 directions
left, right, top, down and we can only pass through 1's.
 Find the shortest path from given source coordinate (a,b) to destination (m,n)
 given we can flip any one of the zero to one.

"""

from collections import Counter, OrderedDict

s = "interviewquery"

res = Counter(s)

orde = OrderedDict(res)
print(list(orde.keys())[0])
