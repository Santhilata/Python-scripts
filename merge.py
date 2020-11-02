# -*- coding: utf-8 -*-
"""
Created on Sat May  2 22:42:10 2020

@author: santhilata
1.Find 1st missing positive number (must do in O(1) memory & O(n) time)

# 2. Merge array b into array a given that array a contains len(b) extra space at
# the end.


"""
'''
import numpy as np

num = list(input().rstrip().split())



'''
# Solution to 2

def sorted_merge(a, b):
    bix = len(b) - 1
    aix = len(a) - len(b) - 1
    while aix >= 0 and bix >= 0:
        if a[aix] > b[bix]:
            a[aix + bix + 1] = a[aix]
            aix -= 1
        else:
            a[aix + bix + 1] = b[bix]
            bix -= 1
    while bix >= 0:
        a[bix] = b[bix]
        bix -= 1
        
a = [33, 44, 55, 66, 88, 99, None, None, None]
b = [11, 22, 77]
sorted_merge(a, b)
print(a)
    
 

import unittest

class Test(unittest.TestCase):
  
    def test_sorted_merge(self):
        a = [33, 44, 55, 66, 88, 99, None, None, None]
        b = [11, 22, 77]
        sorted_merge(a, b)
        print(a)
        self.assertEqual(a, [11, 22, 33, 44, 55, 66, 77, 88, 99])
        a = [11, 22, 55, 66, 88, None, None, None]
        b = [33, 44, 99]
        sorted_merge(a, b)
        print(a)

        self.assertEqual(a, [11, 22, 33, 44, 55, 66, 88, 99])

if __name__ == "__main__":
    unittest.main()
