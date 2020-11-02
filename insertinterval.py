# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 14:12:46 2020

@author: santhilata
"""


"""
Problem:Given a set of non-overlapping & sorted intervals, 
insert a new interval into the intervals (merge if necessary)

Example 1:Given intervals [1,3],[6,9], insert and merge [2,5]
 in as [1,5],[6,9].
 
Example 2:Given [1,2],[3,5],[6,7],[8,10],[12,16], 
insert and merge [4,9] in as [1,2],[3,10],[12,16].
This is because the new interval [4,9] overlaps 
with [3,5],[6,7],[8,10].
"""


arr1 = [[1,3],[6,9]]
to_merge1 = [2,5]

arr2 = [[1,2],[3,5],[6,7],[8,10],[12,16]]
to_merge2 = [4,9]

arr = arr2
to_merge = to_merge2
j = 0
left = arr[j]

temp = left
result = []


while (j <= len(arr)):    

    if left[1]< to_merge[0] or left[0]>to_merge[1]:
         
        if temp not in result:
            
            result.append(temp)
           
           
        if left not in result:
            result.append(left)
        
        j += 1
        if j < len(arr):
            left = arr[j]
            temp = left
          
    else:
        
        if left[0] < to_merge[1] or left[1] > to_merge[0] :
            
            temp = [min(temp[0], left[0]), max(temp[1], left[1])]
            
            temp = [min(temp[0], to_merge[0]), max(temp[1], to_merge[1])]
             
            j +=1
            if j < len(arr):
                left = arr[j]
                
            
            
#result.append(left) 
print(result)      
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
           
        
       
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        