# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 13:02:17 2020

@author: santhilata
"""

import math
import os
import random
import re
import sys

# Complete the balancedSums function below.
def balancedSums(arr):
    if (len(arr) == 1 or len(arr) == 0):
        return 'YES'
    
    mid = len(arr)//2     
    flag = 'NO'
    mid_list = []
    
    while (mid >=0 and mid <len(arr) and mid not in mid_list ):
        mid_list.append(mid)
        left_sum = sum(arr[0:mid])
        right_sum = sum(arr[mid+1:])
        
        if (left_sum == right_sum):
            flag = 'YES'
            break
        elif (left_sum < right_sum  ):
            mid = mid+1
        else :
            mid = mid-1
        
        
    return (flag)
    
    
        

        

if __name__ == '__main__':
    

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

    print(result)
