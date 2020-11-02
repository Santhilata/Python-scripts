# -*- coding: utf-8 -*-
"""
Created on Sat May  2 09:38:26 2020

@author: santhilata

Given an Array of numbers & a target value, return indexes of two numbers
 such that their Absolute difference is equal to the target
 
 Given two dates D1 & D2. count number of days, months?
"""

from datetime import datetime
date_format = "%m/%d/%Y"
a = datetime.strptime('8/18/2008', date_format)
b = datetime.strptime('9/26/2008', date_format)
delta = b - a
print( delta.days) # that's it