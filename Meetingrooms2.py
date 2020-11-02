# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 09:51:16 2020

@author: santhilata
"""


'''
generic multiset
'''

from heapq import heappush, heappop
arr = [[2,15],[36,45],[9,29],[16,23],[4,9]]

'''
if len(arr) == 0:
    print( 0);

heap = []
for item in arr:
    print(item, end=' ')
    heappush(heap,item)

print()   
for item in heap:
    print(item, end = ' ')
    heappop(heap)
print()
'''

def peek(arr):
    if len(arr) >0:
        
        return arr[0]
    
    else:
        return None
    
def _schedule(arr):
    
    if len(arr) == 0:
        return 0
    
    
    #arr = sorted(arr)
    arr.sort(key = lambda x:x[1])
    print(arr)
    queue = []
    queue.append(arr[0][1])
    count =1
    
    for i in range(1,len(arr)):
        
        head = peek(queue)
        
        if arr[i][0] >= head:          
            
            queue.pop()
            
        else:
            print(arr[i][0])
            count += 1
            
        queue.append(arr[i][1])
        
    return count
        
print(_schedule(arr))        
        
def _schedule2(arr):
    
    
    count = 0
    arr = sorted(arr)
    
    while len(arr)>0:
        head = arr[0]
        count +=1
        to_schedule = []
        for m in arr[1:]:
            if head[1] <= m[0]:
                
                continue
            else:
                to_schedule.append(m)
        arr = to_schedule
        
    return count

print(_schedule2(arr))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
        
        