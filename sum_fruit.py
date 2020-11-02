# -*- coding: utf-8 -*-
"""
Created on Wed May  6 12:59:01 2020

@author: santhilata

 amazon-interview-questions
0
of 0 votes
0
Answers

A co-ordinate plane was given. On each point (x, y) there are x+y number of 
apples on it. A person is standing on (0, 0) and he wants to buy a square plot
 having N number of apples inside it (including the periphery). Question was to
 return the value of perimeter of that square plot given N.
"""

import math

N = 50

def sum_fruit(n):
    sum =0
    for i in range(n):
        for j in range(n):
            
            sum += (i+j)  
            
    
    return sum


for i in range(int(math.sqrt(N)), 0,-1):
    if sum_fruit(i) < N:
        
        print(sum_fruit(i), i)
        break
        
    
    
    