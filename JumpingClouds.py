# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 15:49:59 2020

@author: santhilata
"""

def jumpingOnClouds(c):
    index = 0
    n = len(c)
    steps = 0
    while (index != n):
        if (index+2 < n) and c[index+2] ==0:
            steps+=1
            index += 2
        elif (index+1< n) and c[index+1] ==0:
            steps+=1
            index += 1
        else:
            index += 1
    return(steps)
    
if __name__ == '__main__':
    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)
    
    print(result)