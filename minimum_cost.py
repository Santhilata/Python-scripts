# -*- coding: utf-8 -*-
"""
Created on Fri May  1 21:49:47 2020

@author: santhilata

 bloomberg-lp-interview-questions


A company wants to fly in a total of 100 candidates for the interview. 
The company has two office location, one in NY and other 
in SF and max capacity at each location is 50 candidates.
 You are given the cost it incurs to fly in each candidate to NY and SF.
 
 [500, 300],[540, 600],[550, 600],[300, 50]..so on

Write an algorithm for the minimum total cost?
"""


costs = [[500, 300],[540, 600],[550, 600],[300, 50]]

minimum = sum([ min(i) for i in costs  ])
print(minimum)