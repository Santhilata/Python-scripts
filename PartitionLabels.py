# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 18:09:14 2020

@author: santhilata
"""


"""
A string S of lowercase letters is given. 
We want to partition this string into as many parts as possible so that each 
letter appears in at most one part, and return a list of integers representing
 the size of these parts.
 For example:Input: S = "ababfefefhijkh" 
 Output: [4,4,5]
 Explanation: The partition is "abab", "feef", "hijkh". This is a partition 
 so that each letter appears in at most onepart.
"""

s = "ababfefefhijkh" 
ranges = {}


for i in range(len(s)):
      
    if s[i] in ranges.keys():
        
        temp = ranges[s[i]]
        
        temp[1] = max(temp[1], i)
                
        ranges[s[i]] = temp
    else:
        temp =[]
        temp.append(i) 
        temp.append(i)
        ranges[s[i]] = temp
        
print(ranges)        
# now merge intervals
arr = []
for key, val in ranges.items()   :
    arr.append(val)
    
#print(arr)

left = arr[0]
j = 1
right = arr[j]
result = []
while (j < len(arr)):
    
    if (left[1]> right[0]): # overlap
        
        left = [min(left[0], right[0]), max(left[1], right[1])]
        
        j += 1
        if (j < len(arr)):
            right = arr[j]
            
    else:
        if left [1] <right[0]: # no overlap
            result.append(left)
        
            left = right
            j += 1
            if (j < len(arr)):
                right = arr[j]
                
result.append(left)

print(result)
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            