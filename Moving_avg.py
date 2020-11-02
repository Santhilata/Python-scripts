# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 17:12:44 2020

@author: santhilata
"""



arr = [1, 2.3, 4, 2, 3, 6, 11, 5, 8, 9, 10,13]  
arr = [1, 2.3, 4, 2, 3, 6, 11, 5, 8,  10,13]
arr = sorted(arr)
print(arr)
if len(arr)%2 == 0:
    
    mid = len(arr)//2 -1
    
else:
    mid = len(arr)//2 


# get moving average
    

average = []
window = 5
for i in range(len(arr)-window+1):
         
    total = [ arr[j] for j in range(i, i+window)  ]
    print(total)
    
    print('********************')
    '''
    total = []
    for j in range(i, i+window):
        if i+window <= len(arr):
            print(arr[j], end = ',')
            total.append(arr[j])
    '''
    average.append(sum(total)/window)
print()
print(average)