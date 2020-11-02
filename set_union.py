# -*- coding: utf-8 -*-
"""
Created on Fri May  1 06:39:42 2020

@author: santhilata
"""

n = int(input().rstrip())

roll_english = set(map(int, input().rstrip().split()))

b = int(input().rstrip())


roll_french = set(map(int, input().rstrip().split()))

sub_set = roll_english.union(roll_french)
print(len(sub_set))