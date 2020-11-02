# -*- coding: utf-8 -*-
"""
Created on Sun May  3 13:15:37 2020

@author: santhilata
"""

# Collections_counter

from collections import Counter


n = int(input().rstrip())
shoe_sizes = list(map(int,input().rstrip().split()))

num_purchases = int(input().rstrip())




purchases = [(map(int,input().rstrip().split())) for i in range(num_purchases)]



shoes_available = Counter(shoe_sizes)


total_amount = 0
for size, value in purchases:
    if shoes_available[size] > 0:
        total_amount += value
        shoes_available[size] -= 1
print(total_amount)