# -*- coding: utf-8 -*-
"""
Created on Fri May  1 22:32:36 2020

@author: santhilata

 amazon-interview-questions


Giving a the following:

A list of a store items T={t_1, t_2,...,t_n}.

A list of prices of each item P={p_1, p_2,...,p_n}.

A list of quantities of each item Q={q_1, q_2,...,q_n}, respectively.

And total bill M.

Our goal is to find any possible list of items that its total value is 
equal to M using dynamic problem.

Write down a recursive solution.
"""

## store keys in the dictionary, if the keys are found in a dictionary, add values

from collections import OrderedDict

d = OrderedDict()
d[(1,0)] = 17
d[(1,0,7)] = 18

print(d[(1,0)])
