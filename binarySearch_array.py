# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 14:30:43 2020

@author: santhilata
"""

arr = [1, 2.3, 4, 2, 3, 6, 11, 5, 8, 9, 10,13]  

arr = sorted(arr)
#print(arr)

def _bst(arr, key, start, end):
    print(arr[start:end])
    length = end-start #len(arr[start:end])
    
    if (length == 0 )   :
        return 'not found'
    if (length ==1 ):
        if (key == arr[0]):
            return 0
        else:
            return 'not found'
    
    if (length%2 == 0) :
        mid = length//2 -1
        
    else:
        mid = length//2
        
    
    if (key == arr[mid]):
        
        return start+mid
    
    
    if (key > arr[mid]):
        
        return _bst(arr[mid+1: ], key)
        
    else:
        
        return _bst(arr[:mid+1], key)
    
    return 'not found'


#a = _bst(arr, 2, 0, len(arr))

#print(a)

## Not working for numbers outside
def binarySearch(arr, l, r, x):
    
    # Check base case 
    if r >= l: 
  
        mid = l + (r - l) // 2
  
        # If element is present at the middle itself 
        if arr[mid] == x: 
            return mid 
          
        # If element is smaller than mid, then it  
        # can only be present in left subarray 
        elif arr[mid] > x: 
            return binarySearch(arr, l, mid-1, x) 
  
        # Else the element can only be present  
        # in right subarray 
        else: 
            return binarySearch(arr, mid + 1, r, x) 
  
    else: 
        # Element is not present in the array 
        return -1
        
#a = binarySearch(arr, 0, len(arr), 22)
#print(a)

def binarySearch1(arr, l, r, x): 
  
    while l < r: 
  
        mid = l + (r - l) // 2; 
          
        # Check if x is present at mid 
        print(mid)
        if arr[mid] == x: 
            return mid 
  
        # If x is greater, ignore left half 
        elif arr[mid] < x: 
            l = mid + 1
  
        # If x is smaller, ignore right half 
        else: 
            r = mid - 1
      
    # If we reach here, then the element 
    # was not present 
    return -1

a = binarySearch1(arr, 0, len(arr), 17)
print(a)


def _bst_compact(arr, key, l, r):
    
    print(arr)
    
    length = r-l
    
    if length > 0:
        
        mid = l+(r-l) //2
        print (mid)
        if arr[mid] == key:
            return mid
        
        elif arr[mid] > key:
            return _bst_compact(arr, key, l, mid)
        
        else: 
            return _bst_compact(arr, key, mid+1, r )
        
    else:
        return -1
    
#a = _bst_compact(arr, 22, 0, len(arr))
#print(a)
        
        