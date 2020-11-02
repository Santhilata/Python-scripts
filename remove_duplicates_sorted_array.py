# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Remove duplicates from sorted array

arr = [23, 11, 4, 45, 98, 72, 23.3, 18, 16]
arr = [1,1,1,2,2,3]
arr_sort = sorted(arr)

def _remove_duplicates_array( arr):
    
    # O(n) method
    
    if len(arr) < 2:
        return len(arr)
    
    j = 0
    i=1
    
    while (i < len(arr)):
        print(i, j, arr[i], arr[j],'**before**',arr)
        if arr[i] != arr[j]:
            
            j += 1
            arr[j] = arr[i]
        
        print(i, j, arr[i], arr[j],'**after**',arr)    
        i += 1
        
        
    return j+1
    
    
#a = _remove_duplicates_array(arr_sort) 
#print(arr_sort, a)  


def _remove_given_element(a, val):
    
    i=0
    j = 0
    
    while (j < len(a)):
        
        if (a[j] != val):
            
            a[i] = a[j]
            
            i += 1
        j += 1
        
    
    return a      

            
            
a = _remove_given_element(arr_sort, 2) 
print(a)      
    