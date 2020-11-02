# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 20:53:18 2020

@author: santhilata
"""


"""
To some string S, we will perform some replacement operations that replace groups
 of letters with new ones (not necessarily the same size). Each replacement operation
 has 3 parameters: a starting index i, a source word x and a target word y.
 The rule is that if x starts at position i in the original string S,
 then we will replace that occurrence of x with y.
 If not, we do nothing.
 For example,  if we have S = "abcd" and we have some replacement operation 
 i =2,  x = "cd",  y = "ffff",  then because "cd" starts at position 2 in the
 original string S, we will replace it with "ffff"
"""