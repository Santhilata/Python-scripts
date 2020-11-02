# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 22:56:24 2020

@author: santhilata
"""


#Summary ranges

#Given a sorted integer array without duplicates,
# return the summary of its ranges for consecutive numbers.
#For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"]


arr = [0,1,2,4,5,6,8]

right =1
left = 0
result = []
start = left

while (right < len(arr)): 
        
    if arr[right] - arr[left] == 1:
        
        if right != len(arr) -1:
            left += 1
            right += 1  
        else:
            if start != right:
            
                st = str(arr[start])+'->'+str(arr[right])
            else:
                #start == right :
                st = str(arr[start])
                
            result.append(st)
            break
        
        
    else:       
        if right != len(arr) -1:
            if start != right:
                
                st = str(arr[start])+'->'+str(arr[right-1])
            else:
                #start == right :
                st = str(arr[start])
            
            result.append(st)
                
            left = right
            start = left
            
            right +=1    
        
        else:# right == len(arr) -1:
            
            if start != right:
            
                st = str(arr[start])+'->'+str(arr[right])
            else:
                #start == right :
                st = str(arr[start])
                
            result.append(st)
            break
        
    
print(result)
        