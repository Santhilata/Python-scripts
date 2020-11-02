# -*- coding: utf-8 -*-
"""
Created on Fri May  1 20:56:23 2020

@author: santhilata

 amazon-interview-questions
1
of 1 vote
0
Answers

Given an unsorted array A of size N of non-negative integers,
 find a continuous sub-array which adds to a given number S.
"""

#from itertools import combinations

n  = list(map(int,input().rstrip().split()))

s = int(input())

#all_combinations = []
#all_combinations.extend(list(combinations(n, i)) for i in range(len(n+1)))

#print(all_combinations)

all_subsets = [n[i:i+j] for i in range(0,len(n)) for j in range(1,len(n)-i+1)]

result = [subset for subset in all_subsets if sum([i for i in subset]) == s]

print(result)