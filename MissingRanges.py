# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 23:24:18 2020

@author: santhilata
"""


#Given a sorted integer array nums, where the range of elements
# are in the inclusive range [lower, upper], 
#return its missing ranges.
#Example:Input: nums = [0,1,3,50,75], lower =0 and upper =99, 
# Output: ["2", "4->49", "51->74", "76->99"]


arr = [0,1,3,50,75,76,99]

lower = 0
upper = 1
temp_lower = lower
output = []
cont = False

missingranges = []

while (upper < len(arr)):
    
    if (arr[upper] - arr[temp_lower]) == 1:
        temp_lower += 1
        cont = True
        
        
    else:
        if arr[temp_lower]+1 == arr[upper]-1: # only one number
            st = str(arr[temp_lower]+1)
        else:
            st = str(arr[temp_lower]+1)+'->'+str(arr[upper]-1)
        output.append(st)
        
        temp_lower += 1
    upper = upper+1


print(upper)        
if arr[upper-1] != 99:
    st = str(arr[upper-1]+1)+'->99'
    

    output.append(st)
        
print(output)            
            
        