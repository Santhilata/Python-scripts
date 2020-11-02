# -*- coding: utf-8 -*-
"""
Created on Wed May  6 10:59:06 2020

@author: santhilata

balanced brackets
"""

arr ='{[()]}'
arr1 = '{[(])}'
arr2 = '{{[[(())]]}}'


def isBalanced(s):
    
    st = list()
    
    
    for ch in s:
        
        
        if ch in ['{','[','(']:
            st.append(ch)
            
        else:
            if len(st) == 0:
                return 'NO'
            else:
                
                
                if ch == ')':
                    check = st.pop()
                    if   check != '(':
                        return 'NO'
                if ch == ']':
                    check = st.pop()
                    if check != '[':
                        return 'NO'
                    
                if ch == '}':
                    check = st.pop()
                    if check != '{':
                        return 'NO'
            
    if len(st) != 0:
        print(st)
        return 'NO'
    
    return 'YES'

    
print(isBalanced(arr2))