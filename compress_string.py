# -*- coding: utf-8 -*-
"""
Created on Fri May  1 06:02:34 2020

@author: santhilata
"""



from itertools import groupby


  
print(*[(len(list(c)), int(k)) for k, c in groupby(input())])
