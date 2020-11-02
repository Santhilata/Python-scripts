# -*- coding: utf-8 -*-
"""
Created on Tue May  5 17:56:08 2020

@author: santhilata

Bubble Sort is the simplest sorting algorithm that 
works by repeatedly swapping the adjacent elements if they are in wrong order.
"""


arr = [64, 34, 25, 12, 22, 11, 90] 

#o(n^2)



def bubble_sort(arr):
    
    for i in range(len(arr)-1):
        for j in range(i, len(arr)):
            if (arr[i]> arr[j]):
                temp = arr[i]
                arr[i]= arr[j]
                arr[j] = temp
    return arr            

print(bubble_sort(arr))

