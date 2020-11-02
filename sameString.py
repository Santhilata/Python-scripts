# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 22:17:07 2020

@author: santhilata
"""
"""
Given  two  strings  S  and  T,  return  if  they  are  equal  when  both  are
  typed  into  empty  text  editors.  
  #  means  abackspace character.
  Example1: 
      Input: S = "ab#c", T = "ad#c"
      Output: true
      Explanation: Both S and T become "ac".
  Example2:
      Input: S = "a##c", T = "#a#c"
      Output: true
      Explanation: Both S and T become "c".
"""
S = "ab#c"
T = "#a#c"

def _sameString(S,T):

    i = len(S)-1
    j = len(T)-1
    s_flag = False
    t_flag = False
    ch_s = ''
    ch_t = ''
    
    while (i >=0 or j >=0):
        
        while i >=0 and S[i] == '#':
            s_flag = True
            i -= 1
        if s_flag:
            i -= 1   
            s_flag = False
        if i>=0 and S[i] != '#':
            ch_s = S[i]
            print('s= ',ch_s)
        
        
        while (j >=0 and T[j] == '#'):
            t_flag = True
            j -= 1
        if t_flag:
            j -= 1
            t_flag = False
        if j >=0 and T[j] != '#':
            
            ch_t = T[j]
            print('t= ',ch_t)
            
            
            
        if ch_s != ch_t: 
        
            return 'not same'
            
        i -= 1
        j -= 1
        
    return 'same'    

print(_sameString(S,T))
    
    
    
    
