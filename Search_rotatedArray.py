j# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 22:31:49 2020

@author: santhilata
"""
"""
Following two are asked in the Bloomberg rounds
"""

# for fun sake, find the moving averages of sliding window w upto 7

arr = [2,3.4,4,2,1,5,3.2,0,0,1,6,8]

def _movingaverages_(arr):
        
    w_total = []
    for w in [3,5,7]:
        
        total = []
        
        for i in range(len(arr)-w+1):
            
            t  = sum([arr[j] for j in range(i,i+w)])/w
            total.append(t)
            
        #print(total)  
        
        w_total.append(sum(total))
        
    return w_total
        
a = [round(x,2) for x in _movingaverages_(arr)]

#print(a)          
            
# search in rotated array

def _search_recursive(arr,l,r,target)  :
    
    if l > r:
        return -1
    
    mid = l+ (r-l)//2
    
    if target == arr[mid]:
        return mid
    
    if (arr[mid] > arr[l]): # shift is on right
        
        if target > arr[l] and target < arr[mid]:
            return _search_recursive(arr, l, mid-1, target)
        else:
            return _search_recursive(arr, mid+1, r, target)
    else: # shift is on left
        if target < arr[r] and target > arr[mid]:
            return _search_recursive(arr, mid+1, r, target)
        else:
            return _search_recursive(arr, l, mid-1, target)
        
arr = [4,5,6,7,0,1,2,3]
arr = [7,8,1,2,3,4,6]
l =0
r = len(arr) -1
target = 4
print(_search_recursive(arr, l, r, target))