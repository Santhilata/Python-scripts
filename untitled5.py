# -*- coding: utf-8 -*-
"""
Created on Tue May  5 14:54:17 2020

@author: santhilata



Given an array of distinct integers. The task is to count all the triplets 
such that sum of two elements equals the third element.

Input:
The first line of input contains an integer T denoting the number of test cases.
 Then T test cases follow. Each test case consists of two lines.
 First line of each test case contains an Integer N denoting size of array 
 and the second line contains N space separated elements.

Output:
For each test case, print the count of all triplets, in new line. If no such 
triplets can form, print "-1".

Constraints:
1 <= T <= 100
3 <= N <= 105
1 <= A[i] <= 106

Example:
Input:
2
4
1 5 3 2
3
3 2 7
Output:
2
-1

Explanation:
Testcase 1: There are 2 triplets: 1 + 2 = 3 and 3 +2 = 5

"""
from itertools import combinations

#N = 4
N= 3
#arr = [1,5,3,2]
arr = [3,2,7]

sets = list(combinations(arr,3))

result = [sorted(i) for i in sets  ]

l = [i  for i in result if i[0]+i[1]==i[2]]
if (len(l)>0):
    print (len(l))
else:
    print(-1)