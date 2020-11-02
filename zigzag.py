# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 09:25:25 2020

@author: santhilata
"""




def convert(s, numRows):
    
    i = 0 # index of the character in the string
    left_to_right = True
    
    
    list_str = []
    
    while ((len(s) - i) > 0):
   
        temp = ''
        
        for j in range(numRows):
            if  (left_to_right) and (i < len(s)):
                temp = temp+s[i]
                i += 1
        left_to_right = False
        for k in range(numRows-len(temp)):
            temp = temp+ ' '
        list_str.append(temp)
        
        # right to left        
        temp = ' '
        for j in range(numRows-1, 1, -1):
            if ( left_to_right == False) and (i < len(s)):
                temp = temp+s[i]
                i +=1
                    
        for k in range(numRows-len(temp)):
            temp = temp+ ' '
        temp = ''.join([ch for ch in temp[::-1]])
        
        left_to_right = True
        if temp != '  ':
            list_str.append(temp)
        
    print(list_str)
    
    output = ''
    for j in range(numRows):
        for i in range(len(list_str)):            
             
            ch = list_str[i][j]
            if ch !=  ' ':
                output = output+ch
    
    print(output)
convert(s = "PAYPALISHIRING", numRows = 5)