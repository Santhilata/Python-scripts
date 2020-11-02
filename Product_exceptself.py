# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 20:41:32 2020

@author: santhilata
"""

import numpy as np
arr = [1, 2,3,4,5]

# find product of all values execept zeroes
l = np.ones(len(arr))
r = np.ones(len(arr))
result = np.ones(len(arr))

l[0]= arr[0]

r[len(arr)-1] =   arr[len(arr)-1]



for i in range(1, len(arr)):
    l[i] = l[i-1]*arr[i]
    
for i in range(len(arr)-2, -1, -1):
    r[i] = r[i+1]*arr[i]
    
print(l)
print(r)
result[0] = r[1]
result[len(arr)-1] = l[len(arr)-2]

for i in range(1,len(arr)-1 ):
    result[i] = l[i-1] * r[i+1]
    
    
print(result)