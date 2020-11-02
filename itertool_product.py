# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 20:55:00 2020

@author: santhilata
"""

from itertools import product

A = map(int, list(input().split()))
B = map(int, list(input().split()))

c =product(A,B)
print(*c)