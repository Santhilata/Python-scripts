# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import itertools

(K, N) = map(int, input().split())

L = list()
for i in range(K):
    l = list(map(int, input().split()))
    n = l[0]
    L.append(l[1:])
    assert len(L[i]) == n # check

S_max = 0
L_max = None

for l in itertools.product(*L):
    
    s = sum([x**2 for x in l]) % N
    print(l, '=', s)
    if s > S_max:
        S_max = s
        L_max = l

print (S_max)