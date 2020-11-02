# -*- coding: utf-8 -*-
"""
Created on Tue May  5 21:20:36 2020

@author: santhilata

print fibonacci series 


"""


#recursion solution
'''
n = 5


fibo= []    
fibo.append( 0)
fibo.append(  1)

for i in range(2, n):
    fibo.append(fibo[i-1] + fibo[i-2])
    
print(fibo)
'''

'''
#recursive

def fibonacci(n):
    
    if n ==0:
        return 0
    if n==1:
        return 1
    
    return(fibonacci(n-1)+fibonacci(n-2))

n= 5
print(fibonacci(n))
'''

## DP

from collections import defaultdict

fib = defaultdict()
fib[0] = 0
fib[1] = 1

def fibonacci_dp(n):
    
    if n in fib.keys():
        return fib[n]
    else:
        fib[n] = fibonacci_dp(n-1)+fibonacci_dp(n-2)
    
    return fib[n]

print(fibonacci_dp(8))