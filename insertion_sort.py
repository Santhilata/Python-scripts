# -*- coding: utf-8 -*-
"""
Created on Tue May  5 18:05:34 2020

@author: santhilata

Insertion sort is a simple sorting algorithm that works
the way we sort playing cards in our hands.
"""

arr = [64, 34, 25, 12, 22, 11, 90] 

def insertion_sort(arr):
    
    for i in range(1, len(arr)):
        
        for j in range(0,i) :
            
            if( arr[j]> arr[i]):
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
    return arr

print(insertion_sort(arr))           