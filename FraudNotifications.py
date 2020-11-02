# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 11:35:50 2020

@author: santhilata
"""

import math
import os
import random
import re
import sys

from statistics import median
# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    
    notifications = 0
    for i in range(d,len(expenditure)):
        
        day_median = median(expenditure[i-d:i])
        if day_median*2 <= expenditure[i]:
            notifications +=1
    
    return notifications


if __name__ == '__main__':
   

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    print(result)