# -*- coding: utf-8 -*-
"""
Created on Tue May  5 13:48:53 2020

@author: santhilata



Given an unsorted array A of size N of non-negative integers, find a continuous
 sub-array which adds to a given number S.

Input:
The first line of input contains an integer T denoting the number of test cases.
 Then T test cases follow. Each test case consists of two lines. The first line
 of each test case is N and S, where N is the size of array and S is the sum. 
 The second line of each test case contains N space separated integers denoting
 the array elements.

Output:
For each testcase, in a new line, print the starting and ending positions(1 indexing)
 of first such occuring subarray from the left if sum equals to subarray, else print -1.

Constraints:
1 <= T <= 100
1 <= N <= 107
1 <= Ai <= 1010

Example:
Input:
2
5 12
1 2 3 7 5
10 15
1 2 3 4 5 6 7 8 9 10
Output:
2 4
1 5

Explanation :
Testcase1: sum of elements from 2nd position to 4th position is 12
Testcase2: sum of elements from 1st position to 5th position is 15
** For More Input/Output Examples Use 'Expected Output' option **

"""
N,Sum = (5,12)
#N,Sum = (10, 15)
arr = [1,2,3,7,5]
#arr = [1, 2, 3, 4, 5, 6, 7, 8, 9 ,10]

all_subsets = [arr[i:(i+j)] for i in range(len(arr)) for j in range(1, len(arr)-i+1)]
    
result = [(arr.index(subset[0])+1,arr.index(subset[-1])+1)  for subset in all_subsets if sum(subset) ==Sum]

if len(result)>0:
    print(result)
    
    
else:
    print(-1)
    
