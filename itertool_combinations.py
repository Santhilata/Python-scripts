# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 22:11:25 2020

@author: santhilata
"""

from itertools import combinations

s = input()
n1 = s.split()[0]
n2 = int(s.split()[1])


for i in range(1, n2+1):
    l = combinations(sorted(n1), i)
    for j in l:
        print (''.join(j))
  
'''   
[print(''.join(ch) for x in range(1, n2+1) for ch in combinations(sorted(n1),x))]
'''