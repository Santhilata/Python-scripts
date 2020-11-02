# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 16:55:40 2020

@author: santhilata
"""

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    
    for word in note:
        if word in magazine:
            flag = 'Yes'
            magazine.remove(word)
            
        else:
            flag = 'No'
            break
            
    print(flag)
if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
