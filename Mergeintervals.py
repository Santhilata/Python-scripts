# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 13:08:39 2020

@author: santhilata
"""


#Given a collection of intervals, merge all overlapping 
#intervals.For example, Given [1,3],[2,6],[8,10],[15,18], 
#return [1,6],[8,10],[15,18].

arr = [[1,3],[2,5],[4,7],[8,10],[9,16],[15,18]]

j= 1

left = arr[0]
right = arr[j]
result = []
temp = left


while (j <= len(arr)):
    
    if (temp[1] > right[0]): # overlap
        temp = [left[0], right[1]]
        
        j +=1
        if (j < len(arr)):
            right = arr[j]
        
    else:
        result.append(temp)
        
        left = right
        temp = left
        
        j +=1
        if (j < len(arr)):
            right = arr[j]

result.append(temp)        
print(result)