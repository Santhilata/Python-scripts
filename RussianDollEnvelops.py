# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 11:43:01 2020

@author: santhilata
"""
"""
You have a number of envelopes with widths and heights given as a pair of 
integers (w, h).  One envelope can fit into another if and only if both the 
width and height of one envelope is greater than the width and height of the 
other envelope. What is the maximum number of envelopes can you Russian doll?
 (put one inside other)
"""
import numpy as np
def _is_bigger(e1,e2):
    # e1 = tuple of length, width
    
    if e1[0]>e2[0] and e1[1] > e2[1]:
        
        return True
    
    return False

envs = [(1,1),(2,2),(3,3),(4,4),(1,2),(2,1)] # output should be 3
envs = sorted(envs) # first sort by length and by width

def _naive(envs):
    
    result = np.zeros((len(envs))) # how many  envelops can fit into this envelop
    
    for i in range(len(envs)):
        
        for j in range(i):
            
           if (_is_bigger(envs[i], envs[j]) ) :
               result[i] = max(result[i],result[j]+1)
    
    return int(max(result))
    
#print(_naive(envs))
envs = [(1,1),(6,4),(2,2),(3,3),(4,4),(1,2), (2,3)] # output should be 3
envs = sorted(envs) # first sort by length and by width
print(envs)
def _binary_search(envs):
    
    result = [] # how many  envelops can fit into this envelop
    
    for e in envs:
        target = e
        
        if len(result) == 0 or _is_bigger(target,result[-1]):
            result.append(target)
            
        else:
            l=0
            r = len(result) -1
            
            while (l <r):
                
                mid = l + (r-l)//2
                
                if _is_bigger(result[mid], target):
                    r = mid
                    
                else:
                    l = mid+1
            #print(r,target)
            result[r] = target
        
    return result
            
        
print(_binary_search(envs))      
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        