# -*- coding: utf-8 -*-
"""
Created on Wed May  6 12:38:37 2020

@author: santhilata

 amazon-interview-questions


Implement union and intersection of two array(in a efficient way).

Additional information given by the interviewer was: elements of 
the two given array may be repeated but cannot be repeated in union and 
intersection array.
"""

arr1 = [10,2,34,34, 28,22]
arr2 = [89, 6, 34, 22, 22, 12]

set1 = set(arr1)
set2 = set(arr2)

#print( list(set1 & set2))

t = [ num for num in set1 if num in set2]

print(t)