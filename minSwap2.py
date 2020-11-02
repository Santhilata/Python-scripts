# -*- coding: utf-8 -*-
"""
Created on Tue May  5 22:43:17 2020

@author: santhilata

Minimum Swaps 2
https://www.hackerrank.com/challenges/minimum-swaps-2/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
"""

def minimumSwaps(arr):
    
    
    temp = [0] * (len(arr) + 1)
    for pos, val in enumerate(arr):
        
        temp[val] = pos
        pos += 1
    
    swaps = 0
    for i in range(len(arr)):
        #print(temp,'--temp')
        print(arr, '--arr')
        if arr[i] != i+1:
            
            swaps += 1
            t = arr[i]
            arr[i] = i+1
            arr[temp[i+1]] = t
            temp[t] = temp[i+1]
    
    
    return swaps
            

arr = [7,1,3,2,4,5,6]
arr = [1,3,5,7,2,4,6,8]
print(minimumSwaps(arr))
            
'''
            runfile('C:/Users/santh/OneDrive/Documents/Python Scripts/minSwap2.py', wdir='C:/Users/santh/OneDrive/Documents/Python Scripts')
[7, 1, 3, 2, 4, 5, 6] --arr
[1, 7, 3, 2, 4, 5, 6] --arr
[1, 2, 3, 7, 4, 5, 6] --arr
[1, 2, 3, 7, 4, 5, 6] --arr
[1, 2, 3, 4, 7, 5, 6] --arr
[1, 2, 3, 4, 5, 7, 6] --arr
[1, 2, 3, 4, 5, 6, 7] --arr
5

runfile('C:/Users/santh/OneDrive/Documents/Python Scripts/minSwap2.py', wdir='C:/Users/santh/OneDrive/Documents/Python Scripts')
[0, 1, 3, 2, 4, 5, 6, 0] --temp
[0, 1, 3, 2, 4, 5, 6, 1] --temp
[0, 1, 3, 2, 4, 5, 6, 3] --temp
[0, 1, 3, 2, 4, 5, 6, 3] --temp
[0, 1, 3, 2, 4, 5, 6, 4] --temp
[0, 1, 3, 2, 4, 5, 6, 5] --temp
[0, 1, 3, 2, 4, 5, 6, 6] --temp
5

'''