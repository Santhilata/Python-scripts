# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 09:12:50 2020

@author: santhilata
"""

"""
Given n non-negative integers a1, a2, ..., an, where each represents a point
 at coordinate (i, ai). 
 n vertical lines are drawn such that the two endpoints of line i is at (i, ai)
 and (i,0).
 Find two lines, which together with x-axis forms a container, 
 such that the container contains the most water.
"""

heights = [1,1,2,4,2,1]

left = 0
right = len(heights)-1
volume = 0

while left < right:
    
    volume = max(volume, (right - left)*min(heights[left], heights[right]))
    if heights[left] < heights[right]:
        
        
        left += 1
    else:
        right -= 1
        
print(volume)