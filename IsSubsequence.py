# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 21:59:55 2020

@author: santhilata
"""

"""
Given a string s and a string t, check if s is subsequence of t.
You may assume that there is only lower case English letters in both s and t.
 t is potentially a very long (length=500,000) string,
 and s is a short string (<=100).
 A  subsequence  of  a  string  is  a  new  string  which  is  formed 
 from  the  original  string  by  deleting  some  (canbe  none)
  of  the  characters  without  disturbing  the  relative  positions 
  of  the  remaining  characters.  
  (ie,  "ace"  is  a subsequence of "abcde" while "aec" is not).
  
"""

s = 'aec'
t = 'abcde'

def _is_subsequence(s,t):
    pos_t = -1
        
    for ch in s:
        
        if ch in t[pos_t+1:]:
            pos_t = t.index(ch)
            
        else:
            return False
    return True
        
print(_is_subsequence(s,t))    
    