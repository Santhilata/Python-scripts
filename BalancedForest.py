# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 08:49:35 2020

@author: santhilata

input

2
5
1 2 2 1 1
1 2
1 3
3 5
1 4
3
1 3 5
1 3
1 2

output
2
-1

"""


    

def balancedForest(c, edges):
    if (len(edges) < 2):
        return -1 # The tree is far too small
    
    n = len(c)
    for node in range(n):
        

if __name__ == '__main__':
    

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        c = list(map(int, input().rstrip().split()))

        edges = []

        for _ in range(n - 1):
            edges.append(list(map(int, input().rstrip().split())))

        result = balancedForest(c, edges)

        